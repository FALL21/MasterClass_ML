"""App de démo : risque de départ d'un client. Lancer avec : streamlit run app.py"""
from pathlib import Path
import joblib, pandas as pd, streamlit as st

st.set_page_config(page_title="Prédiction du churn", page_icon="📶", layout="centered")
model = joblib.load(Path(__file__).parent / "modele_churn.joblib")

st.title(" Ce client va-t-il partir ?")
st.caption("Masterclass GOMYCODE — De la donnée à l'IA")

c1, c2 = st.columns(2) 
with c1:
    anciennete = st.slider("Ancienneté (mois)", 1, 120, 8)
    forfait = st.radio("Forfait", ["prépayé", "postpayé"], horizontal=True)
    appels_sc = st.slider("Appels au service client (ce mois)", 0, 8, 4)
    pannes = st.slider("Pannes réseau subies (ce mois)", 0, 6, 2)
    momo = st.radio("Utilise Mobile Money", ["oui", "non"], index=1, horizontal=True)
with c2:
    region = st.selectbox("Région", ["Dakar", "Thiès", "Saint-Louis", "Kaolack", "Ziguinchor", "Touba"])
    data = st.number_input("Consommation data (Go / mois)", 0.0, 60.0, 2.5, step=0.5)
    minutes = st.number_input("Minutes d'appel / mois", 0, 1000, 90, step=10)
    recharge = st.number_input("Recharge mensuelle (FCFA)", 0, 100000, 3000, step=500)

client = pd.DataFrame([{
    "anciennete_mois": anciennete, "type_forfait": forfait, "region": region,
    "conso_data_go": data, "minutes_appels": minutes, "recharge_mensuelle_fcfa": recharge,
    "nb_appels_service_client": appels_sc, "utilise_mobile_money": momo, "nb_pannes_reseau": pannes,
}])
risque = model.predict_proba(client)[0, 1]

st.divider()
st.metric("Risque de départ", f"{risque:.0%}")
st.progress(float(risque))
if risque >= 0.5:
    st.error("⚠️ Client à risque : proposer une offre de fidélisation.")
else:
    st.success("✅ Client stable.")
