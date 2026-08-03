import streamlit as st
import random
from datetime import datetime

from responses import (
    greetings,
    goodbye,
    jokes,
    motivation,
    facts,
    thanks,
    quiz,
    ai_info
)

from utils import (
    get_date,
    get_time,
    calculate
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="DecodeLabs Smart AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "commands_used" not in st.session_state:
    st.session_state.commands_used = 0

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "username" not in st.session_state:
    st.session_state.username = "Guest"

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🤖 AI Assistant")

    st.markdown("---")

    st.session_state.username = st.text_input(
        "👤 Your Name",
        value=st.session_state.username
    )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "💬 Chat",
            "🧮 Calculator",
            "🧠 Quiz",
            "📊 Statistics",
            "👨 About"
        ]
    )

    st.markdown("---")

    if st.button("😂 Random Joke"):
        st.session_state.messages.append(
            ("🤖", random.choice(jokes))
        )

    if st.button("💡 Motivation"):
        st.session_state.messages.append(
            ("🤖", random.choice(motivation))
        )

    if st.button("🌍 Fun Fact"):
        st.session_state.messages.append(
            ("🤖", random.choice(facts))
        )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []

# =====================================================
# HEADER
# =====================================================

st.title("🤖 DecodeLabs Smart AI Assistant")

st.caption("Rule-Based AI Chatbot using Python + Streamlit")

st.markdown("---")

# =====================================================
# HOME PAGE
# =====================================================

if page == "💬 Chat":

    st.success(
        f"Welcome {st.session_state.username} 👋"
    )

    st.write(
        f"📅 **Date:** {get_date()}"
    )

    st.write(
        f"🕒 **Time:** {get_time()}"
    )

    st.markdown("---")

    for sender, message in st.session_state.messages:

        with st.chat_message(sender):

            st.write(message)

    user_input = st.chat_input(
        "Type your message..."
    )
    # ==========================================
    # CHAT LOGIC
    # ==========================================

    if user_input:

        st.session_state.commands_used += 1

        st.session_state.messages.append(
            ("user", user_input)
        )

        command = user_input.lower().strip()

        # ----------------------------
        # Greetings
        # ----------------------------

        if command in ["hi", "hello", "hey"]:

            response = random.choice(greetings)

        # ----------------------------
        # Small Talk
        # ----------------------------

        elif command == "how are you":

            response = "😊 I'm doing great! Thanks for asking."

        elif command == "who are you":

            response = "🤖 I am DecodeLabs Smart AI Assistant."

        elif command == "who created you":

            response = "👨‍💻 I was created as a DecodeLabs Internship Project."

        elif command == "what can you do":

            response = """
I can help you with:

✅ Greetings
✅ AI Knowledge
✅ Python Information
✅ Date & Time
✅ Calculator
✅ Jokes
✅ Motivation
✅ Fun Facts
✅ Quiz
"""

        # ----------------------------
        # AI
        # ----------------------------

        elif command == "ai":

            response = ai_info["ai"]

        elif command == "python":

            response = ai_info["python"]

        # ----------------------------
        # Date & Time
        # ----------------------------

        elif command == "date":

            response = f"📅 Today's Date : {get_date()}"

        elif command == "time":

            response = f"🕒 Current Time : {get_time()}"

        # ----------------------------
        # Joke
        # ----------------------------

        elif command == "joke":

            response = random.choice(jokes)

        # ----------------------------
        # Motivation
        # ----------------------------

        elif command in ["motivate", "motivation"]:

            response = random.choice(motivation)

        # ----------------------------
        # Fun Fact
        # ----------------------------

        elif command == "fact":

            response = random.choice(facts)

        # ----------------------------
        # Thank You
        # ----------------------------

        elif command in ["thanks", "thank you"]:

            response = random.choice(thanks)

        # ----------------------------
        # Exit
        # ----------------------------

        elif command in ["bye", "exit", "quit"]:

            response = random.choice(goodbye)

        # ----------------------------
        # Unknown
        # ----------------------------

        else:

            response = (
                "❌ Sorry! I don't understand that.\n\n"
                "Try commands like:\n"
                "• hi\n"
                "• ai\n"
                "• python\n"
                "• date\n"
                "• time\n"
                "• joke\n"
                "• motivate\n"
                "• fact"
            )

        st.session_state.messages.append(
            ("assistant", response)
        )

        st.rerun()
# =====================================================
# CALCULATOR PAGE
# =====================================================

elif page == "🧮 Calculator":

    st.header("🧮 Smart Calculator")

    expression = st.text_input(
        "Enter Expression",
        placeholder="Example: (25+10)*2"
    )

    if st.button("Calculate"):

        if expression.strip() == "":
            st.warning("Please enter an expression.")
        else:
            result = calculate(expression)
            st.success(result)

# =====================================================
# QUIZ PAGE
# =====================================================

elif page == "🧠 Quiz":

    st.header("🧠 AI Quiz")

    st.write(quiz["question"])

    answer = st.radio(
        "Choose your answer",
        ["A", "B", "C"],
        horizontal=True
    )

    if st.button("Submit Answer"):

        if answer.lower() == quiz["answer"]:

            st.success("🎉 Correct Answer!")

            st.balloons()

            st.session_state.quiz_score += 1

        else:

            st.error(
                "❌ Wrong Answer!\n\nCorrect Answer: Artificial Intelligence"
            )

# =====================================================
# STATISTICS PAGE
# =====================================================

elif page == "📊 Statistics":

    st.header("📊 Session Statistics")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Commands Used",
            st.session_state.commands_used
        )

    with col2:

        st.metric(
            "Quiz Score",
            st.session_state.quiz_score
        )

    st.markdown("---")

    st.subheader("Conversation")

    st.write(
        f"Messages : {len(st.session_state.messages)}"
    )

# =====================================================
# ABOUT PAGE
# =====================================================

elif page == "👨 About":

    st.header("👨 About")

    st.markdown("""
# 🤖 DecodeLabs Smart AI Assistant

A professional Rule-Based AI Chatbot built using **Python** and **Streamlit**.

## 🚀 Features

- 👋 Greetings
- 🤖 AI Knowledge
- 🐍 Python Knowledge
- 📅 Date
- 🕒 Time
- 🧮 Calculator
- 😂 Random Jokes
- 💡 Motivation Quotes
- 🌍 Fun Facts
- 🧠 AI Quiz
- 📊 Session Statistics
- 💬 Chat Interface

---

## 🛠 Technologies Used

- Python
- Streamlit
- Random
- Datetime

---

Made for the DecodeLabs AI Internship Project.
""")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "© 2026 DecodeLabs Smart AI Assistant | Python + Streamlit"
)