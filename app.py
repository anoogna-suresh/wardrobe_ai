import streamlit as st
from chat import ask_ollama  # Make sure your function is in chat.py

# Sample wardrobe — later we’ll pull this from a CSV or UI input
wardrobe = ["grey hoodie", "black joggers", "white sneakers", "beige trench coat", "red scarf"]

st.set_page_config(page_title="AI Wardrobe Assistant", page_icon="🧥")
st.title("👕 AI Wardrobe Assistant")
st.subheader("Let AI help you dress smart!")

# Weather and mood selection
weather = st.selectbox("What's the weather like?", ["sunny", "rainy", "cold", "windy", "cloudy"])
mood = st.selectbox("How are you feeling today?", ["energetic", "lazy", "chill", "cozy", "fashionable"])

# Show wardrobe
st.write("### Your wardrobe:")
st.write(", ".join(wardrobe))

# Generate outfit suggestion
if st.button("Get Outfit Suggestion"):
    with st.spinner("Thinking..."):
        suggestion = ask_ollama(weather, mood, wardrobe)
        st.success("Here's what you should wear:")
        st.markdown(f"> {suggestion}")
