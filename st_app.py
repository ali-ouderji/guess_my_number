import streamlit as st
import random

st.set_page_config(page_title="🎯 Number Guessing Game", layout="centered")
st.title("🎯 Number Guessing Game")

# Initialize game state
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Game status
if st.session_state.game_over:
    st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts.")
    if st.button("Play Again"):
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
else:
    guess = st.number_input("Enter your guess (1–100):", min_value=1, max_value=100, step=1)
    if st.button("Submit Guess"):
        st.session_state.attempts += 1

        if guess < st.session_state.number_to_guess:
            st.warning("📉 Too low!")
        elif guess > st.session_state.number_to_guess:
            st.warning("📈 Too high!")
        else:
            st.session_state.game_over = True
            st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts.")
