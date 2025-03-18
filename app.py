import streamlit as st
import pandas as pd
from data import repas, data_tuna

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

    # Sélecteur de jour
    selected_day = st.selectbox(
        "Sélectionner un jour",
        options=list(data_tuna.keys())
    )

    # Affichage des deux vues
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader(f"Repas du {selected_day}")
        for meal, content in zip(repas, data_tuna[selected_day]):
            st.markdown(f"**{meal}**")
            st.write(content)
            st.write("---")

    with col2:
        st.subheader("Planning hebdomadaire complet")
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
