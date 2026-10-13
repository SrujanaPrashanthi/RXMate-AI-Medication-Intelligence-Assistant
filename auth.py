import streamlit as st
import json
import os
import hashlib

USER_FILE = "users.json"

# Hash function (SHA-256)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Load users from file
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

# Save users to file
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

# Sign up logic
def signup():
    st.title("📝 Create an Account")
    new_username = st.text_input("Your Username")
    new_password = st.text_input("Your Password", type="password")

    if st.button("Sign Up"):
        users = load_users()
        if new_username in users:
            st.warning("⚠ Username already exists!")
        elif not new_username.strip() or not new_password.strip():
            st.warning("❗ Username and password cannot be empty.")
        else:
            hashed_pw = hash_password(new_password)
            users[new_username] = hashed_pw
            save_users(users)
            st.success("✅ Account created!")
            st.session_state.logged_in = True
            st.session_state.username = new_username
            st.rerun()

# Login logic
def login():
    users = load_users()

    if st.session_state.get("logged_in", False):
        return

    st.title("🔐 PharmaPal Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not username.strip() or not password.strip():
            st.warning("❗ Username and password required.")
        elif username in users and users[username] == hash_password(password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"✅ Welcome back, {username}!")
            st.rerun()
        else:
            st.error("❌ Invalid username or password.")

# Logout logic
def logout():
    if st.button("Logout 🔒"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()