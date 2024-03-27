import math

def vitesse_coupe1(diametre_fraise_mm, vitesse_rotation_toupie_rpm):
    # Conversion du diamètre de la fraise en mètres
    diametre_fraise_m = diametre_fraise_mm / 1000

    # Calcul de la vitesse de coupe
    vitesse_coupe_m_min = math.pi * diametre_fraise_m * vitesse_rotation_toupie_rpm / 60

    return vitesse_coupe_m_min

# Exemple d'utilisation de la fonction
diametre_fraise = 12  # en millimètres
vitesse_rotation_toupie = 20000  # en tours par minute

vitesse = vitesse_coupe1(diametre_fraise, vitesse_rotation_toupie)
print("La vitesse de coupe est de", round(vitesse, 2), "m/min")


def vitesse_coupe2(diametre_fraise_mm, vitesse_rotation_toupie_rpm):
    # Conversion du diamètre de la fraise en mètres
    diametre_fraise_m = diametre_fraise_mm / 1000

    # Calcul de la vitesse de coupe
    vitesse_coupe_m_min = math.pi * diametre_fraise_m * vitesse_rotation_toupie_rpm / 60

    return vitesse_coupe_m_min

# Demander à l'utilisateur d'entrer le diamètre de la fraise
diametre_fraise_input = input("Entrez le diamètre de la fraise en millimètres : ")

# Convertir le diamètre de la fraise en entier
diametre_fraise = int(diametre_fraise_input)

# Demander à l'utilisateur d'entrer la vitesse de rotation de la toupie
vitesse_rotation_input = input("Entrez la vitesse de rotation de la toupie en tours par minute : ")
vitesse_rotation_toupie = int(vitesse_rotation_input)

# Calculer la vitesse de coupe en utilisant la fonction vitesse_coupe
vitesse = vitesse_coupe2(diametre_fraise, vitesse_rotation_toupie)

print("La vitesse de coupe est de", round(vitesse, 2), "m/min")
