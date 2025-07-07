import getpass
import os
import streamlit as st
from langchain.chat_models import init_chat_model
from langchain.chains import SequentialChain, LLMChain
from langchain.prompts import PromptTemplate

if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = st.secrets['GEMINI_API']

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

def generate_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="Generate exactly one fancy restaurant name for {cuisine} cuisine. Provide only the name without any additional text or punctuation.",
    )
    name_chain = LLMChain(llm=model, prompt=prompt_template_name, output_key="restaurant_name")
    
    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="List exactly 5 popular menu items for {restaurant_name}. Return them as a comma-separated list without any additional text or punctuation. For example: Item1, Item2, Item3, Item4, Item5",
    )
    item_chain = LLMChain(llm=model, prompt=prompt_template_items, output_key="menu_items")
    
    chain = SequentialChain(
        chains=[name_chain, item_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"]
    )
    response = chain.invoke({"cuisine": cuisine})  # Using the passed cuisine parameter
    return response
