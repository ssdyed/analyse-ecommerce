import pandas as pd
import matplotlib.pyplot as plt

# 1. Visualisation des données

# charger le fichier
data = pd.read_csv("/Users/sdye/Desktop/practice/projet2/ventes_ecommerce.csv")

# voir les types de données et les valeurs manquantes dans chaque colonne
print("\nTypes de données étudiés et valeurs manquantes par colonne :")
print(data.info())

# les valeurs manquantes en pourcentage
pourcentage_manquants = (data.isnull().sum() / len(data)) * 100
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
print(f"\nLe revenu total pour toute cette période de temps est {revenu_total:.2f}.")

# Le produit le plus vendu
produit_plus_vendu = data.groupby("Produit")["Quantité"].sum().idxmax()
quantite_maximale = data.groupby("Produit")["Quantité"].sum().max()
print(f"\nSur cette période de temps, nous avons vendu {quantite_maximale}"
      f" unités de {produit_plus_vendu}.")

# La catégorie la plus rentable
categorie_rentable = data.groupby("Catégorie")["Revenu"].sum().idxmax()
revenu_maximale = data.groupby("Catégorie")["Revenu"].sum().max()
print(f"\nAyant rapporté {revenu_maximale:.2f}, la catégorie la plus rentable est {categorie_rentable}.")

# Panier moyen des clients
panier_moyen = revenu_total / data["Client_ID"].nunique()
print(f"\nLe panier moyen par client est de {panier_moyen:.2f} dollars")

# 3. Analyse temporelle des ventes

# Tendances mensuelle des ventes

# transformer les dates en format datetime pour faire les calculs
data["Date"] = pd.to_datetime(data["Date"])

# regrouper les ventes et le revenu par mois
ventes_mensuelles = data.groupby(data["Date"].dt.to_period("M"))["Revenu"].sum()

# graphique
plt.figure(figsize=(20, 7))
ventes_mensuelles.plot(kind="line", marker="o", linestyle="-", color="b")
plt.title("Tendance mensuellle des ventes")
plt.xlabel("Mois")
plt.ylabel("Revenu total")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 3. Analyse des ventes par jour de la semaine

# créer une colonne qui convertir les dates en jour
data["Jour_Semaine"] = data["Date"].dt.day_name()

# regrouper les ventes et le revenu par jour
ventes_journalieres = data.groupby("Jour_Semaine")["Revenu"].sum()

# mettre les jours dans l'ordre chronologique
jours_ordre = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ventes_journalieres = ventes_journalieres.reindex(jours_ordre)

# les ventes par jours de la semaine
print("\nVoici les ventes par jour de la semaine :")
print(ventes_journalieres)

# grpahique des ventes par jour de la semaine
plt.figure(figsize=(10, 5))
ventes_journalieres.plot(kind="bar", color="b")
plt.title("Ventes par jour de la semaine")
plt.xlabel("Jour de la semaine")
plt.ylabel("Revenu total")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show() # graphique

