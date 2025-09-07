import streamlit as st
import openai
from openai import OpenAI

# 🔐 Initialisation du client OpenAI
user_api_key = st.text_input("🔑 Entrez votre clé OpenAI :", type="password")
client = OpenAI(api_key=user_api_key)
if not user_api_key:
    st.warning("Veuillez entrer votre clé API OpenAI pour continuer.")
    st.stop()
else:
    try:
        client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": "Test"}])
    except Exception as e:
        st.error(f"Erreur de connexion {e}: Vérifiez votre clé API.")
        st.stop()
# 🎨 Interface
st.set_page_config(page_title="Hub IA Créatif", layout="centered")
st.title("🤖 Hub IA Créatif")

# 🚀 Choix du mode
mode = st.sidebar.radio("Choisir une fonction :", ["💬 Chat GPT", "🎨 Image DALL·E"])

# --- 💬 CHAT GPT ---
if mode == "💬 Chat GPT":
    st.subheader("Parle avec ChatGPT")
    user_input = st.text_area("Ton message :", height=150)

    if st.button("Envoyer"):
        if user_input.strip() != "":
            with st.spinner("ChatGPT réfléchit..."):
                response = client.chat.completions.create(
                    model="gpt-4o",
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

