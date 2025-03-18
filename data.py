# Liste des repas
repas = [
    "Petit-déjeuner",
    "Collation matin",
    "Déjeuner",
    "Collation après-midi",
    "Dîner"
]

# Menu avec thon
menu_tuna = {
    "Petit-déjeuner": """3 œufs
50g flocons d'avoine
1 cuillère beurre de cacahuète
1 fruit""",
    "Collation matin": """150g fromage blanc 0%
20g whey
20g amandes""",
    "Déjeuner": """150g poulet
150g riz basmati
100g courgettes sautées
1 cuillère d'huile d'olive""",
    "Collation après-midi": """30g whey
1 banane
10g miel""",
    "Dîner (Lundi, Mercredi, Vendredi, Dimanche)": """150g steak haché 5%
100g patate douce
100g courgettes en purée
1 cuillère d'huile d'olive""",
    "Dîner (Mardi, Jeudi, Samedi)": """150g thon frais
100g patate douce
100g courgettes en purée
1 cuillère d'huile d'olive"""
}

# Données pour chaque jour
data_tuna = {
    "Lundi": [menu_tuna[repas[i]] if i != 4 else menu_tuna["Dîner (Lundi, Mercredi, Vendredi, Dimanche)"] for i in range(len(repas))],
    "Mardi": [menu_tuna[repas[i]] if i != 4 else menu_tuna["Dîner (Mardi, Jeudi, Samedi)"] for i in range(len(repas))],
    "Mercredi": [menu_tuna[repas[i]] if i != 4 else menu_tuna["Dîner (Lundi, Mercredi, Vendredi, Dimanche)"] for i in range(len(repas))],
    "Jeudi": [menu_tuna[repas[i]] if i != 4 else menu_tuna["Dîner (Mardi, Jeudi, Samedi)"] for i in range(len(repas))],
    "Vendredi": [menu_tuna[repas[i]] if i != 4 else menu_tuna["Dîner (Lundi, Mercredi, Vendredi, Dimanche)"] for i in range(len(repas))],
    "Samedi": [menu_tuna[repas[i]] if i != 4 else menu_tuna["Dîner (Mardi, Jeudi, Samedi)"] for i in range(len(repas))],
    "Dimanche": [menu_tuna[repas[i]] if i != 4 else menu_tuna["Dîner (Lundi, Mercredi, Vendredi, Dimanche)"] for i in range(len(repas))]
}