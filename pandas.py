# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 11:53:53 2024

@author: Djibril Awa Makhtar FALL

point de controle Nettoyage et transformation des données avec pandas

"""
import pandas as pd

# Données à insérer dans le DataFrame
data = {
    'Nom': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
    'Département': ['IT', 'Marketing', 'Ventes', 'IT', 'Finances', 'Marketing'],
    'Âge': [30, 40, 25, 35, 45, 28],
    'Sexe': ['Homme', 'Femme', 'Homme', 'Femme', 'Homme', 'Femme'],
    'Salaire': [50000, 60000, 45000, 55000, 70000, 55000],
    'Expérience': [3, 7, 2, 5, 10, 4]
}

# Création du DataFrame

employee_df = pd.DataFrame(data)

# Affichage du DataFrame

print(employee_df)

# 1) Utilisez la méthode iloc pour sélectionner les 3 premières lignes du dataframe.

# Sélectionner les 3 premières lignes

trois_premieres_lignes = employee_df.iloc[:3]

# Affichage des 3 premières lignes

print(trois_premieres_lignes)

# 2) Utilisez la méthode loc pour sélectionner toutes les lignes où le département est « Marketing ».

# Sélectionner toutes les lignes où le département est "Marketing"

marketing_df = employee_df.loc[employee_df['Département'] == 'Marketing']

# Affichage des lignes sélectionnées

print(marketing_df)

""" 3) Utilisez la méthode iloc pour sélectionner les colonnes Âge et Sexe 
pour les 4 premières lignes du dataframe. """

# Sélectionner les 4 premières lignes et les colonnes Âge et Sexe

age_sexe_df = employee_df.iloc[:4, [2, 3]]  # Les colonnes Âge et Sexe ont des index 2 et 3

# Affichage du résultat

print(age_sexe_df)

""" 4) Utilisez la méthode loc pour sélectionner les colonnes Salaire et Expérience
 pour toutes les lignes où le sexe est « Homme »."""
 
# Sélectionner les colonnes Salaire et Expérience où le sexe est "Homme"
hommes_df = employee_df.loc[employee_df['Sexe'] == 'Homme', ['Salaire', 'Expérience']]

# Affichage du résultat

print(hommes_df)

