# Récupération du mot de passe saisi depuis l'entrée JSON
mot_de_passe = items[0]['json']['data'].get('Saisie du mot de passe')

# Comparaison avec le mot de passe attendu
resultat = mot_de_passe == "toto84"

# Renvoi du résultat sous forme d'objet JSON
return {
    "match": resultat
}