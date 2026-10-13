import streamlit as st
import json
import os
from auth import signup, login, logout
from refill import check_refill_status
import google.generativeai as genai

st.set_page_config(page_title="PharmaPal", layout="centered")

genai.configure(api_key=st.secrets["gemini"]["api_key"])

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text

if not st.session_state.logged_in:
    login()
else:
    st.title("💊 PharmaPal Assistant")

    logout()

    user_query = st.text_input("Ask a healthcare question")

    if st.button("Ask"):
        if user_query:
            response = get_gemini_response(user_query)
            st.write(response)

    st.markdown("---")
    st.subheader("📦 Refill Status")

    refill_info = check_refill_status(st.session_state.username)

    if refill_info:
        st.success(
            f"""
Medicine: {refill_info['medicine']}

Last Refill: {refill_info['last_refill']}

Next Due: {refill_info['next_refill_due']}

Status: {refill_info['status']}
"""
        )
    else:
        st.warning("No refill information found.")