import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Python Programs", page_icon="🐍", layout="centered")

# --- Main Title ---
st.title("🐍 Welcome to Python Programs! 🧠")

# --- Creator Credit ---
st.markdown("### 👨‍💻 Created by **Sundram Gupta**")

# --- Description Section ---
st.markdown("""
✨ This web app is specially designed for:
- 🧩 **Practicing Python Programs**
- 🧾 **Creating Lab Files**
- 💡 **Understanding Basic to Intermediate Concepts**
- 📘 **Learning Step-by-Step with Examples**
""")

# --- Divider Line ---
st.markdown("---")

# --- Extra Info / Quote ---
st.info("💬 *“Code is like humor. When you have to explain it, it’s bad.”*")

# --- Next Page Button ---
if st.button("Next ➡️"):
    st.switch_page("lab1.py") # You can change to 'operators.py' or 'data_types.py'

# --- Footer ---
st.markdown("---")
st.caption("🧡 Made with Streamlit | 📚 Practice • Learn • Improve")
