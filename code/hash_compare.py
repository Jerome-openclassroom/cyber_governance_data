# Valeur de référence SHA-256
reference_hash = "73a938fda187bfe124c528e1c2c44bfc731cf34aa61705df9fd03349c45e9975"

# Récupération du hash généré par le node Crypto
incoming_hash = items[0]['json']['data']

# Comparaison
if incoming_hash == reference_hash:
    result = "fichier intact"
else:
    result = "fichier altéré"

# Sortie
return {
    "hash_reçu": incoming_hash,
    "hash_attendu": reference_hash,
    "résultat": result,
    "sessionid": "12345"
}