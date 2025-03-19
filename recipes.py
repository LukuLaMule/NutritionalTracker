# Recettes détaillées pour chaque plat
recipes = {
    "Petit-déjeuner": {
        "temps_preparation": "10 minutes",
        "instructions": [
            "Faire cuire les œufs selon votre préférence (au plat, brouillés, à la coque)",
            "Préparer les flocons d'avoine avec de l'eau chaude ou du lait",
            "Ajouter le beurre de cacahuète sur les flocons d'avoine",
            "Servir avec un fruit frais de votre choix"
        ],
        "conseils": "Pour plus de saveur, vous pouvez ajouter un peu de cannelle aux flocons d'avoine."
    },
    "Déjeuner": {
        "temps_preparation": "20 minutes",
        "instructions": [
            "Faire cuire le riz basmati selon les instructions",
            "Couper le poulet en morceaux et le faire griller",
            "Laver et couper les courgettes en rondelles",
            "Faire sauter les courgettes à la poêle",
            "Assaisonner avec sel, poivre et huile d'olive"
        ],
        "conseils": "Mariner le poulet à l'avance pour plus de saveur."
    },
    "Dîner": {
        "temps_preparation": "25 minutes",
        "instructions": [
            "Faire cuire la patate douce au four ou à la vapeur",
            "Préparer la purée de courgettes",
            "Cuire le steak haché ou le thon selon le jour",
            "Assaisonner avec sel, poivre et huile d'olive"
        ],
        "conseils": "La patate douce peut être préparée en avance pour gagner du temps."
    }
}

def get_recipe(meal_name):
    """Obtenir la recette détaillée pour un repas donné"""
    base_meal = meal_name.split(" (")[0] if " (" in meal_name else meal_name
    return recipes.get(base_meal, {
        "temps_preparation": "5 minutes",
        "instructions": ["Assembler les ingrédients selon les proportions indiquées"],
        "conseils": "Aucun conseil particulier pour cette préparation simple."
    })
