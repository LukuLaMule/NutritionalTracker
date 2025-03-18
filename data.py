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
    "Petit-déjeuner": "3 œufs\n50g flocons d'avoine\n1 cuillère beurre de cacahuète\n1 fruit",
    "Collation matin": "150g fromage blanc 0%\n20g whey\n20g amandes",
    "Déjeuner": "150g poulet\n150g riz basmati\n100g courgettes sautées\n1 cuillère d'huile d'olive",
    "Collation après-midi": "30g whey\n1 banane\n10g miel",
    "Dîner (Lundi, Mercredi, Vendredi, Dimanche)": "150g steak haché 5%\n100g patate douce\n100g courgettes en purée\n1 cuillère d'huile d'olive",
    "Dîner (Mardi, Jeudi, Samedi)": "150g thon frais\n100g patate douce\n100g courgettes en purée\n1 cuillère d'huile d'olive"
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