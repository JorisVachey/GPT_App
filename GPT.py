import streamlit as st
import openai
from openai import OpenAI

# 🔐 Initialisation du client OpenAI
client = OpenAI(api_key="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")

# 🎨 Interface
st.set_page_config(page_title="Hub IA Créatif", layout="centered")
st.title("🤖 Hub IA Créatif")

# 🚀 Choix du mode
mode = st.sidebar.radio("Choisir une fonction :", ["💬 Chat GPT", "🎨 Image DALL·E", "🌐 Générateur de site web"])

# --- 💬 CHAT GPT ---
if mode == "💬 Chat GPT":
    st.subheader("Parle avec ChatGPT")
    user_input = st.text_area("Ton message :", height=150)

    if st.button("Envoyer"):
        if user_input.strip() != "":
            with st.spinner("ChatGPT réfléchit..."):
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": user_input}]
                )
                message = response.choices[0].message.content.strip()
                st.markdown("**Réponse :**")
                st.write(message)
        else:
            st.warning("Écris quelque chose d'abord !")

# --- 🎨 IMAGE DALL·E ---
elif mode == "🎨 Image DALL·E":
    st.subheader("Génère une image à partir d'un prompt")
    prompt = st.text_input("Décris l’image à créer :")

    if st.button("Générer l’image"):
        if prompt.strip() != "":
            with st.spinner("DALL·E est en train de dessiner..."):
                response = client.images.generate(
                    prompt=prompt,
                    n=1,
                    size="512x512"
                )
                image_url = response.data[0].url
                st.image(image_url, caption="Image générée", use_column_width=True)
        else:
            st.warning("Tu dois écrire une description !")

# --- 🌐 GÉNÉRATEUR DE SITE WEB ---
elif mode == "🌐 Générateur de site web":
    st.subheader("Crée un site web (HTML/CSS) à partir d’une description")
    prompt = st.text_area("Décris le site que tu veux :", height=150)

    if st.button("Générer le site"):
        if prompt.strip() != "":
            with st.spinner("Je crée ton site..."):
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "user", "content": f"Crée un site web simple en HTML/CSS basé sur cette description : {prompt}. Ne commente pas le code, retourne uniquement le code HTML complet avec le CSS inclus dans une balise <style>."}
                    ]
                )
                html_code = response.choices[0].message.content.strip()

                # Affiche le code généré
                st.markdown("**Code HTML/CSS généré :**")
                st.code(html_code, language='html')

                # Rendu live
                st.markdown("**Aperçu du site :**")
                st.components.v1.html(html_code, height=600, scrolling=True)

                # Edition manuelle
                st.markdown("**Modifier le code HTML/CSS si besoin :**")
                edited_code = st.text_area("Édite ici :", value=html_code, height=300)

                # Nouveau rendu après édition
                if st.button("Mettre à jour le rendu"):
                    st.components.v1.html(edited_code, height=600, scrolling=True)

                # Téléchargement
                st.download_button("📥 Télécharger le code", edited_code, file_name="site.html")
        else:
            st.warning("Décris ton site pour que je puisse le générer !")
