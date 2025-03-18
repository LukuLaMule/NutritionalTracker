import streamlit as st
import pandas as pd
from datetime import datetime
from data import repas, data_tuna

def get_current_day():
    # Obtenir le jour actuel en français
    days = {
        0: "Lundi",
        1: "Mardi", 
        2: "Mercredi",
        3: "Jeudi",
        4: "Vendredi",
        5: "Samedi",
        6: "Dimanche"
    }
    # Ajuster pour que lundi soit 0
    current_weekday = datetime.now().weekday()
    return days[current_weekday]

def format_meal(meal_text):
    # Remplacer les + par des retours à la ligne HTML
    return meal_text.replace(" + ", "<br>")

def main():
    # Configuration de la page
    st.set_page_config(
        page_title="Calendrier Nutritionnel",
        page_icon="🍽️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Titre de l'application
    st.title("🍽️ Plan Nutritionnel Hebdomadaire")

    # Création du DataFrame avec formatage HTML
    df_data = {day: [format_meal(meal) for meal in meals] for day, meals in data_tuna.items()}
    df_tuna = pd.DataFrame(df_data, index=repas)

    # Obtenir le jour actuel
    current_day = get_current_day()

    # Sélecteur de jour avec le jour actuel par défaut
    selected_day = st.selectbox(
        "Sélectionner un jour",
        options=list(data_tuna.keys()),
        index=list(data_tuna.keys()).index(current_day)
    )

    # Ajustement des colonnes pour un meilleur affichage
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader(f"Repas du {selected_day}")
        if selected_day == current_day:
            st.info(f"📅 C'est le menu d'aujourd'hui !")

        # Affichage des repas du jour sélectionné dans un format plus compact
        for meal, content in zip(repas, data_tuna[selected_day]):
            st.markdown(f"**{meal}**")
            st.write(content.replace(" + ", "\n"))
            st.write("---")

    with col2:
        st.subheader("Planning hebdomadaire complet")
        # Optimiser l'affichage du tableau
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

        # Formater le DataFrame pour un meilleur affichage
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

    # Informations supplémentaires en bas de page
    st.markdown("### Notes importantes")
    st.info("""
    - Les repas sont adaptés pour un déficit calorique
    - Le dîner alterne entre steak haché et thon frais selon les jours
    - Tous les repas incluent les portions recommandées
    """)

if __name__ == "__main__":
    main()