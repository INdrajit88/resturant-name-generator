import streamlit as st
from langchain_helper import generate_name_and_items

st.set_page_config(
    page_title="Restaurant Name Generator",
    page_icon="🍽️",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align:center; color:#1b5e20;'>🍽️ Restaurant Name Generator</h1>"
    "<p style='text-align:center; color:#0d47a1;'>Unleash AI creativity for your next culinary venture</p>",
    unsafe_allow_html=True
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Select from predefined cuisines")
    cuisine_select = st.selectbox(
        "Pick a cuisine",
        ("Indian 🇮🇳", "Chinese 🇨🇳", "Italian 🇮🇹", "Mexican 🇲🇽"),
        key="select_cuisine"
    )

with col2:
    st.subheader("Or enter your own cuisine")
    cuisine_input = st.text_input(
        "Enter cuisine type",
        placeholder="e.g., French, Japanese, Thai...",
        key="input_cuisine"
    )

st.markdown("")

input_method = st.radio(
    "Choose input method",
    ["Use predefined selection", "Use custom input"],
    horizontal=True
)

st.markdown("---")

if st.button("✨ Generate Restaurant Details", use_container_width=True):
    try:
        cuisine = cuisine_select.split()[0] if input_method == "Use predefined selection" else cuisine_input

        if cuisine:
            with st.spinner('Generating your restaurant concept...'):
                result = generate_name_and_items(cuisine)
            st.success("Your restaurant concept is ready! 🎉")
            st.balloons()

            st.markdown(
                f"<div style='color:#b71c1c; font-size:2.5em; text-align:center; padding:1rem; background:#fff3e0; border-radius:10px; margin:1rem 0; box-shadow:0 2px 4px rgba(0,0,0,0.1);'>{result['restaurant_name'].strip()}</div>",
                unsafe_allow_html=True
            )

            st.markdown("<h3 style='color:#0d47a1; text-align:center;'>📑 Signature Menu Items</h3>", unsafe_allow_html=True)
            menu_items = result['menu_items'].strip().split(',')
            for item in menu_items:
                st.markdown(
                    f"<div style='font-size:1.2em; padding:0.5rem; margin:0.2rem 0; background:#fff; border-radius:5px; color:#333; border:1px solid #ddd; text-align:center;'>{item.strip()}</div>",
                    unsafe_allow_html=True
                )
        else:
            st.warning("Please select or enter a cuisine type")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.markdown(
        "<div style='background:#fff; border-radius:10px; padding:2rem; box-shadow:0 2px 4px rgba(0,0,0,0.1); text-align:center; color:#333;'>"
        "<h3>Welcome to the Restaurant Name Generator! 🎉</h3>"
        "<p>Select a cuisine type or enter your own, then click 'Generate' to get a unique restaurant name and menu items.</p>"
        "</div>",
        unsafe_allow_html=True
    )

st.markdown("<div style='text-align:center; color:#333; padding:2rem;'>Made with ❤️ for food entrepreneurs</div>", unsafe_allow_html=True)