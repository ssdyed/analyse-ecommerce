import pandas as pd

# 1. Visualisation des données

# charger le fichier
data = pd.read_csv("/Users/sdye/Desktop/practice/projet2/ventes_ecommerce.csv")

# voir les types de données et les valeurs manquantes dans chaque colonne
print("\nTypes de données étudiés et valeurs manquantes par colonne :")
print(data.info())

# les valeurs manquantes en pourcentage
pourcentage_manquants = (data.isnull().sum() / len(data)) *100
print("\nPourcentage de valeurs manquantes par colonne :")
print(pourcentage_manquants)

# faire apparaitre le nombre de valeurs uniques par colonnes
print("\nNombre de valeurs uniques par colonne :")
print(data.nunique())

# données statistiques
print("\nRésumé statistiques des données numériques :")
print(data.describe())

# 2. Analyse des performances de vente

# Chiffre d'affaire total
revenu_total = data["Revenu"].sum()
print("\nLe revenu total pour toute cette période de temps est ",revenu_total)

# La quantité du produit le plus vendu
