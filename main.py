
import streamlit as st




def main():
    st.title("Login Form Severin")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username == "admin" and password == "password":
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")

if __name__ == "__main__":
    main()
