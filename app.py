import streamlit as st
import pandas as pd
from datetime import datetime
import re
from data import repas, data_tuna
from nutrition import calculate_nutrition, format_nutrition_values
from recipes import get_recipe

def get_current_day():
    days = {
        0: "Lundi",
        1: "Mardi", 
        2: "Mercredi",
        3: "Jeudi",
        4: "Vendredi",
        5: "Samedi",
        6: "Dimanche"
    }
    current_weekday = datetime.now().weekday()
    return days[current_weekday]

def format_meal(meal_text):
    ingredients = meal_text.split(" + ")
    return "\n".join(ingredients)

def main():
    st.set_page_config(
        page_title="Calendrier Nutritionnel",
        page_icon="🍽️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.title("🍽️ Plan Nutritionnel Hebdomadaire")

    df_data = {day: [format_meal(meal) for meal in meals] for day, meals in data_tuna.items()}
    df_tuna = pd.DataFrame(df_data, index=repas)

    current_day = get_current_day()

    col1, col2 = st.columns([1, 2])

    with col1:
        selected_day = st.select_slider(
            "Sélectionner un jour",
            options=list(data_tuna.keys()),
            value=current_day
        )

        st.subheader(f"Repas du {selected_day}")
        if selected_day == current_day:
            st.info(f"📅 C'est le menu d'aujourd'hui !")

        total_daily = {"calories": 0, "proteines": 0, "glucides": 0, "lipides": 0}

        for meal, content in zip(repas, data_tuna[selected_day]):
            st.markdown(f"**{meal}**")
            st.write(format_meal(content))

            nutrition_values = calculate_nutrition(content)
            formatted_values = format_nutrition_values(nutrition_values)

            for key in total_daily:
                total_daily[key] += nutrition_values[key]

            col_cal, col_prot, col_carb, col_fat = st.columns(4)
            with col_cal:
                st.markdown(f"🔥 **{formatted_values['calories']}** kcal")
            with col_prot:
                st.markdown(f"🥩 **{formatted_values['proteines']}**g")
            with col_carb:
                st.markdown(f"🍚 **{formatted_values['glucides']}**g")
            with col_fat:
                st.markdown(f"🥑 **{formatted_values['lipides']}**g")

            if st.button(f"📝 Voir la recette - {meal}", key=f"recipe_{meal}"):
                recipe = get_recipe(meal)
                st.markdown("#### Instructions de préparation")
                st.info(f"⏱️ Temps de préparation : {recipe['temps_preparation']}")

                st.markdown("##### Étapes :")
                for i, step in enumerate(recipe['instructions'], 1):
                    st.markdown(f"{i}. {step}")

                st.markdown("##### Conseil :")
                st.info(f"💡 {recipe['conseils']}")

            st.write("---")

        st.subheader("Total journalier")
        total_formatted = format_nutrition_values(total_daily)
        st.info(f"""
        🔥 Calories: **{total_formatted['calories']}** kcal
        🥩 Protéines: **{total_formatted['proteines']}**g
        🍚 Glucides: **{total_formatted['glucides']}**g
        🥑 Lipides: **{total_formatted['lipides']}**g
        """)

    with col2:
        st.subheader("Planning hebdomadaire complet")
        st.write(
            """
            <style>
            .stDataFrame {
                width: 100%;
                max-width: none !important;
            }
            .stDataFrame td {
                white-space: pre-wrap !important;
                line-height: 1.5 !important;
            }
            </style>
            """, 
            unsafe_allow_html=True
        )

        styled_df = df_tuna.style.set_properties(**{
            'white-space': 'pre-wrap',
            'text-align': 'left',
            'max-width': '150px',
            'width': '100%'
        })

        st.dataframe(
            styled_df,
            use_container_width=True
        )

        if st.button("📄 Exporter en PDF"):
            st.warning("Fonctionnalité d'export PDF en cours de développement...")

        st.markdown("### Notes importantes")
        st.info("""
        - Les repas sont adaptés pour un déficit calorique
        - Le dîner alterne entre steak haché et thon frais selon les jours
        - Tous les repas incluent les portions recommandées
        """)

if __name__ == "__main__":
    main()