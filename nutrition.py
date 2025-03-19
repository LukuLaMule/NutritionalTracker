# Valeurs nutritionnelles pour 100g/unité
nutrition_data = {
    "œufs": {"calories": 155, "proteines": 13, "glucides": 1.1, "lipides": 11},
    "flocons d'avoine": {"calories": 389, "proteines": 13.5, "glucides": 66, "lipides": 7},
    "beurre de cacahuète": {"calories": 589, "proteines": 25, "glucides": 20, "lipides": 50},
    "fruit": {"calories": 60, "proteines": 1, "glucides": 15, "lipides": 0},
    "fromage blanc 0%": {"calories": 60, "proteines": 10, "glucides": 4, "lipides": 0},
    "whey": {"calories": 380, "proteines": 75, "glucides": 8, "lipides": 2},
    "amandes": {"calories": 576, "proteines": 21, "glucides": 22, "lipides": 49},
    "poulet": {"calories": 165, "proteines": 31, "glucides": 0, "lipides": 3.6},
    "riz basmati": {"calories": 350, "proteines": 7, "glucides": 77, "lipides": 1},
    "courgettes": {"calories": 17, "proteines": 1.2, "glucides": 3.1, "lipides": 0.3},
    "huile d'olive": {"calories": 884, "proteines": 0, "glucides": 0, "lipides": 100},
    "banane": {"calories": 89, "proteines": 1.1, "glucides": 23, "lipides": 0.3},
    "miel": {"calories": 304, "proteines": 0.3, "glucides": 82, "lipides": 0},
    "steak haché 5%": {"calories": 136, "proteines": 21, "glucides": 0, "lipides": 5},
    "patate douce": {"calories": 86, "proteines": 1.6, "glucides": 20, "lipides": 0.1},
    "thon frais": {"calories": 144, "proteines": 30, "glucides": 0, "lipides": 1}
}

def extract_quantity(ingredient):
    """Extraire la quantité et le nom de l'ingrédient"""
    parts = ingredient.split()
    quantity = 0
    
    for part in parts:
        if part.replace(".", "").isdigit():
            quantity = float(part)
        elif "g" in part and part.replace("g", "").isdigit():
            quantity = float(part.replace("g", ""))
            
    return quantity

def calculate_nutrition(meal):
    """Calculer les valeurs nutritionnelles pour un repas"""
    total = {"calories": 0, "proteines": 0, "glucides": 0, "lipides": 0}
    ingredients = meal.split(" + ")
    
    for ingredient in ingredients:
        quantity = extract_quantity(ingredient)
        
        # Trouver l'ingrédient dans la base de données
        for food, values in nutrition_data.items():
            if food in ingredient.lower():
                factor = quantity / 100 if quantity > 0 else 1
                for key in total:
                    total[key] += values[key] * factor
                break
    
    return total

def format_nutrition_values(values):
    """Formater les valeurs nutritionnelles pour l'affichage"""
    return {k: round(v, 1) for k, v in values.items()}
