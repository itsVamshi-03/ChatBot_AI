"""
=========================================================
            DecodeLabs Smart AI Assistant
                  utils.py
=========================================================
"""

import os
import time
from datetime import datetime

# =========================================================
# DATE
# =========================================================

def get_date():
    """
    Returns current date.
    """
    return datetime.now().strftime("%d %B %Y")


# =========================================================
# TIME
# =========================================================

def get_time():
    """
    Returns current time.
    """
    return datetime.now().strftime("%I:%M:%S %p")


# =========================================================
# TYPING ANIMATION
# =========================================================

def typing(delay=0.03):
    """
    Simple typing animation.
    """

    print("\n🤖 Bot is typing", end="", flush=True)

    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)

    print("\n")


# =========================================================
# CHAT HISTORY
# =========================================================

CHAT_FILE = "chat_history.txt"


def save_chat(user, bot):
    """
    Saves conversation into chat_history.txt
    """

    with open(CHAT_FILE, "a", encoding="utf-8") as file:

        file.write("=" * 50 + "\n")
        file.write(f"Time : {datetime.now()}\n")
        file.write(f"User : {user}\n")
        file.write(f"Bot  : {bot}\n")
        file.write("=" * 50 + "\n\n")


# =========================================================
# SHOW CHAT HISTORY
# =========================================================

def show_history():

    if not os.path.exists(CHAT_FILE):

        print("\nNo chat history found.\n")
        return

    print("\n========== CHAT HISTORY ==========\n")

    with open(CHAT_FILE, "r", encoding="utf-8") as file:

        print(file.read())


# =========================================================
# CLEAR CHAT HISTORY
# =========================================================

def clear_history():

    with open(CHAT_FILE, "w", encoding="utf-8") as file:

        file.write("")

    print("✅ Chat history cleared.")


# =========================================================
# SAFE CALCULATOR
# =========================================================

def calculate(expression):
    """
    Supports:
    +  -  *  /  %  **
    """

    try:

        allowed = "0123456789+-*/%.() "

        for char in expression:

            if char not in allowed:
                return "❌ Invalid character detected."

        answer = eval(expression)

        return f"🧮 Answer = {answer}"

    except ZeroDivisionError:

        return "❌ Cannot divide by zero."

    except Exception:

        return "❌ Invalid expression."


# =========================================================
# FILE LOGGER
# =========================================================

LOG_FILE = "system_log.txt"


def write_log(message):

    with open(LOG_FILE, "a", encoding="utf-8") as log:

        log.write(
            f"[{datetime.now()}] {message}\n"
        )


# =========================================================
# SESSION START
# =========================================================

def session_start():

    write_log("Session Started")


# =========================================================
# SESSION END
# =========================================================

def session_end():

    write_log("Session Ended")


# =========================================================
# PAUSE
# =========================================================

def pause():

    input("\nPress ENTER to continue...")


# =========================================================
# LINE
# =========================================================

def line():

    print("=" * 60)


# =========================================================
# TITLE
# =========================================================

def title(text):

    line()

    print(text.center(60))

    line()


# =========================================================
# FOOTER
# =========================================================

def footer():

    print("\nThank you for using DecodeLabs Smart AI Assistant!")