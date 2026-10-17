# Masterclass Churn Kit

Kit pédagogique **GOMYCODE** — *De la donnée à l’IA* : prédire le risque de départ (churn) d’un client télécom, puis exposer le modèle via une interface Streamlit.

## Objectif

Répondre à la question :

> Peut-on identifier *avant qu’il parte* un client à risque, pour lui proposer une offre de fidélisation ?

Le parcours couvre l’exploration des données, la fuite de variables, un pipeline scikit-learn (préparation + régression logistique), l’évaluation, puis une démo interactive.

## Contenu du projet

| Fichier | Rôle |
|---------|------|
| `Masterclass_ml.ipynb` | Notebook de la masterclass (EDA → modèle → sauvegarde) |
| `churn_telecom.csv` | Jeu de données (~5 000 clients) |
| `modele_churn.joblib` | Modèle entraîné (pipeline prêt à prédire) |
| `app.py` | Application Streamlit de démonstration |
| `requirements.txt` | Dépendances Python |

## Données

Variables principales :

- **Numériques** : `anciennete_mois`, `conso_data_go`, `minutes_appels`, `recharge_mensuelle_fcfa`, `nb_appels_service_client`, `nb_pannes_reseau`
- **Catégorielles** : `type_forfait`, `region`, `utilise_mobile_money`
- **Cible** : `churn` (`1` = part, `0` = reste)

> `jours_sans_recharge` est volontairement exclue du modèle : c’est une **fuite de données** (information post-départ).

## Prérequis

- Python 3.10+
- Environnement virtuel recommandé (conda ou venv)

## Installation

```bash
cd masterclass_churn_kit
python -m venv .venv
source .venv/bin/activate   # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

**Important :** le fichier `modele_churn.joblib` doit être chargé avec la **même version** de scikit-learn que celle utilisée à l’entraînement (voir `requirements.txt`). Un écart de version peut provoquer une erreur du type `_fill_dtype`.

Si besoin, réentraînez et resauvegardez le modèle depuis le notebook, puis alignez le nom du fichier avec celui attendu par `app.py` (`modele_churn.joblib`).

## Utilisation

### 1. Notebook

Ouvrir `Masterclass_ml.ipynb` dans Jupyter / VS Code / Cursor et exécuter les cellules dans l’ordre.

### 2. Application Streamlit

```bash
streamlit run app.py
```

Puis ouvrir l’URL locale (en général `http://localhost:8501`).

L’interface permet de saisir le profil d’un client et d’afficher :

- le **risque de départ** (probabilité)
- une alerte si le risque est ≥ 50 %

## Pipeline du modèle

```text
Données brutes
    → imputation (médiane) + StandardScaler (numériques)
    → OneHotEncoder (catégorielles)
    → LogisticRegression (class_weight="balanced")
    → probabilité de churn
```

## Structure recommandée pour la masterclass

1. Charger et explorer `churn_telecom.csv`
2. Visualiser les liens avec le churn
3. Séparer train / test
4. Détecter la fuite (`jours_sans_recharge`)
5. Entraîner le pipeline
6. Évaluer (classification report, AUC, matrice de confusion)
7. Sauvegarder le modèle et lancer la démo Streamlit

