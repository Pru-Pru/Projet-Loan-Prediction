# Dream Housing Finance - Aide à la décision

Ce projet est une application web d'intelligence artificielle permettant de prédire l'éligibilité d'un client à un prêt bancaire.

##  Fonctionnalités
- **Interface interactive** développée avec Streamlit.
- **Modèle prédictif** basé sur la Régression Logistique.
- **Diagnostic en temps réel** avec calcul du score de confiance.

## Structure du dépôt
- `app.py` : Code de l'interface utilisateur.
- `mon_modele_pret.pkl` : Le modèle IA entraîné et sauvegardé.
- `requirements.txt` : Liste des bibliothèques nécessaires.
- `Projet_Loan_Prediction.ipynb` : Le notebook contenant l'analyse et l'entraînement.
- `train_loan_prediction.csv` : Le jeu de données utilisé.

## Installation
1. Cloner le projet : `git clone https://github.com/Pru-Pru/Projet-Loan-Prediction.git`
2. Installer les dépendances : `pip install -r requirements.txt`
3. Lancer l'app : `streamlit run app.py`

---
*Projet réalisé dans le cadre du cours csi1402 Projet en science des donnees de l'universite Teluq.*
