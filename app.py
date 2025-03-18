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

def main():
    # Configuration de la page
    st.set_page_config(
        page_title="Calendrier Nutritionnel",
        page_icon="🍽️",
        layout="wide"
    )

    # Titre de l'application
    st.title("🍽️ Plan Nutritionnel Hebdomadaire")

    # Création du DataFrame
    df_tuna = pd.DataFrame(data_tuna, index=repas)

    # Obtenir le jour actuel
    current_day = get_current_day()

    # Sélecteur de jour avec le jour actuel par défaut
    selected_day = st.selectbox(
        "Sélectionner un jour",
        options=list(data_tuna.keys()),
        index=list(data_tuna.keys()).index(current_day)
    )

    # Affichage des deux vues
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader(f"Repas du {selected_day}")
        if selected_day == current_day:
            st.info(f"📅 C'est le menu d'aujourd'hui !")

        for meal, content in zip(repas, data_tuna[selected_day]):
            st.markdown(f"**{meal}**")
            st.write(content)
            st.write("---")

    with col2:
        st.subheader("Planning hebdomadaire complet")
        # Mettre en surbrillance la ligne du jour actuel
        st.dataframe(
            df_tuna,
            use_container_width=True,
            height=400
        )

    # Informations supplémentaires
    st.markdown("### Notes importantes")
    st.info("""
    - Les repas sont adaptés pour un déficit calorique
    - Le dîner alterne entre steak haché et thon frais selon les jours
    - Tous les repas incluent les portions recommandées
    """)

if __name__ == "__main__":
    main()