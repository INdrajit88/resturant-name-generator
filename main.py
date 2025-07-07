import streamlit as st
from langchain_helper import generate_name_and_items

st.title("Restaurant Name Generator")

# Create two columns for input options
col1, col2 = st.columns(2)

with col1:
    st.subheader("Select from predefined cuisines")
    cuisine_select = st.selectbox(
        "Pick a cuisine",
        ("Indian", "Chinese", "Italian", "Mexican"),
        key="select_cuisine"
    )

with col2:
    st.subheader("Or enter your own cuisine")
    cuisine_input = st.text_input(
        "Enter cuisine type",
        placeholder="e.g., French, Japanese, Thai...",
        key="input_cuisine"
    )

# Add a radio button to choose between selection and custom input
input_method = st.radio(
    "Choose input method",
    ["Use predefined selection", "Use custom input"]
)

if st.button("Generate Restaurant Details"):
    try:
        # Determine which cuisine to use based on radio selection
        cuisine = cuisine_select if input_method == "Use predefined selection" else cuisine_input
        
        if cuisine:  # Only proceed if we have a cuisine value
            result = generate_name_and_items(cuisine)
            st.header(result['restaurant_name'].strip())
            menu_items = result['menu_items'].strip().split(',')
            st.subheader("Menu Items:")
            for item in menu_items:
                st.write("-", item.strip())
        else:
            st.warning("Please select or enter a cuisine type")
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")