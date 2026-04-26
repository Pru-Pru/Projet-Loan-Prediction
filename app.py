import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Charger le modèle
model = joblib.load('mon_modele_pret.pkl')

st.title("🏦 Dream Housing Finance - Aide à la décision")
st.write("Saisissez les informations du client pour obtenir une réponse immédiate.")

# 2. Création du formulaire de saisie
col1, col2 = st.columns(2)

with col1:
    credit = st.selectbox("Historique de crédit", options=[1.0, 0.0], format_func=lambda x: "Bon (1)" if x == 1.0 else "Mauvais (0)")
    revenu = st.number_input("Revenu total du foyer ($)", value=5000)
    montant = st.number_input("Montant du prêt souhaité ($)", value=150)
    zone = st.selectbox("Zone géographique", options=[1, 2, 0], format_func=lambda x: ["Urbain", "Semi-Urbain", "Rural"][x])

with col2:
    marie = st.selectbox("Le client est-il marié ?", options=[1, 0], format_func=lambda x: "Oui" if x == 1 else "Non")
    education = st.selectbox("Diplôme", options=[0, 1], format_func=lambda x: "Diplômé" if x == 0 else "Non Diplômé")
    duree = st.slider("Durée du prêt (jours)", 12, 480, 360)

# 3. Bouton pour lancer la prédiction
if st.button("Analyser le dossier"):
    # Préparation des données comme dans le notebook
    client_data = pd.DataFrame({
        'Gender': [1], 'Married': [marie], 'Dependents': [0], 'Education': [education],
        'Self_Employed': [0], 'Loan_Amount_Term': [duree], 'Credit_History': [credit],
        'Property_Area': [zone], 'Total_Income_log': [np.log(revenu)], 'LoanAmount_log': [np.log(montant)]
    })
    
    prediction = model.predict(client_data)[0]
    proba = model.predict_proba(client_data)[0][1]

    # 4. Affichage du résultat
    st.subheader("Verdict :")
    if prediction == 1:
        st.success(f"✅ PRÊT APPROUVÉ (Confiance : {proba*100:.2f}%)")
    else:
        st.error(f"❌ PRÊT REFUSÉ (Confiance : {(1-proba)*100:.2f}%)")