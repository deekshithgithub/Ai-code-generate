# 1. Import necessary libraries
import streamlit as st
from pydantic import BaseModel
from typing import List
from helpers import code_generator

[theme]

# Primary accent for interactive elements
primaryColor = '#7792E3'

# Background color for the main content area
backgroundColor = '#001728'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#0C3151'

# Color used for almost all text
textColor = '#fffff'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace) 
# Default: "sans serif"
font = "sans serif"

class GeneratedCode(BaseModel):
    code: str



# 3. Apply dark mode CSS

st.markdown("<h1 style='font-family: Helvetica; text-align: center; color: blue;'>Leocode Ai</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='font-family: Lato, sans-serif; font-weight: 500; font-size: 18px; color: #fffff; text-align: center;'> ARTIFICIAL INTELLIGENCE BASED CODE GENERATING TOOL.</h4>", unsafe_allow_html=True)
input_text = st.text_area("Enter your code prompt:", "")


if st.button("Generate Code"):
    with st.spinner("Generating code..."):
        # 7. Call the code generator function
        result = code_generator("gpt-3.5-turbo", input_text, GeneratedCode)
        # 8. Display the generated code
        st.code(result.code, language="python",)

st.info("Provide a code-related prompt and click 'Generate Code', otherwise you won't get a proper output.")
st.markdown("<h9 style='color: #005094;'> ~@deekshith </h9>", unsafe_allow_html=True)
