# =============================================================
#  Gestion de fichiers + statistiques NumPy : jeu de données des prêts
# =============================================================

# 1. Importer la bibliothèque nécessaire
import numpy as np

NOM_FICHIER = "Loan_prediction_dataset.csv"
COLONNE_MONTANT = "LoanAmount"   # nom de la colonne des montants de prêt


# 2. Ouvrir le fichier CSV avec open() et assigner le résultat à une variable
fichier = open(NOM_FICHIER, "r", encoding="utf-8")

# Lire la ligne d'en-tête pour trouver la position de la colonne voulue
entete = fichier.readline().strip().split(",")
print("Colonnes du fichier :", entete)

if COLONNE_MONTANT not in entete:
    fichier.close()
    raise SystemExit(f"Colonne '{COLONNE_MONTANT}' introuvable. "
                     f"Modifiez COLONNE_MONTANT avec l'un des noms ci-dessus.")

index_montant = entete.index(COLONNE_MONTANT)

# Lire le reste du fichier avec genfromtxt (delimiter="," : valeurs séparées
# par des virgules). L'en-tête a déjà été lu, donc pas de skip_header ici.
# Les cellules vides deviennent nan (Not a Number).
montants = np.genfromtxt(fichier, delimiter=",", usecols=index_montant)

# Fermer le fichier une fois la lecture terminée
fichier.close()
print("Fichier fermé :", fichier.closed)


# 3. Analyse statistique avec NumPy
nb_total = montants.size
montants = montants[~np.isnan(montants)]     # retirer les valeurs manquantes
nb_manquants = nb_total - montants.size

moyenne = np.mean(montants)
mediane = np.median(montants)
ecart_type = np.std(montants)

print("\n=== Statistiques sur les montants des prêts ===")
print(f"Nombre de prêts           : {nb_total}")
print(f"Valeurs manquantes ignorées : {nb_manquants}")
print(f"Moyenne                   : {moyenne:.2f}")
print(f"Médiane                   : {mediane:.2f}")
print(f"Écart type                : {ecart_type:.2f}")
print(f"Minimum                   : {np.min(montants):.2f}")
print(f"Maximum                   : {np.max(montants):.2f}")
