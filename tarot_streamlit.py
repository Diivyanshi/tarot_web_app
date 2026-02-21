# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 02:36:37 2026

@author: test
"""

import streamlit as st
import pandas as pd
import random

# Load CSV
df = pd.read_csv("tarot_data_full_major_arcana.csv")
# Topic detection
def detect_topic(question):
    question = question.lower()
    if any(word in question for word in ["exam", "score", "study", "pass"]):
        return "exam"
    elif any(word in question for word in ["love", "relationship", "crush", "him", "text"]):
        return "love"
    elif any(word in question for word in ["job", "career", "promotion", "work"]):
        return "career"
    else:
        return "general"

# Pull card
def pull_card(used_cards):
    available_cards = [c for c in df["card_name"].unique() if c not in used_cards]
    card = random.choice(available_cards)
    orientation = random.choice(["upright", "reversed"])
    return card, orientation

# Get meaning
def get_meaning(card, orientation, topic):
    result = df[
        (df["card_name"] == card) &
        (df["orientation"] == orientation) &
        (df["topic"] == topic)
    ]
    if not result.empty:
        return result.iloc[0]["meaning"]
    else:
        return "Meaning not found."

# Streamlit interface
st.set_page_config(page_title="3-Card Tarot AI", layout="centered")
st.title("🔮 3-Card Tarot AI Oracle")

question = st.text_input("Ask your question here:")

if st.button("Draw Cards") and question:
    topic = detect_topic(question)
    used_cards = []
    positions = ["Past Energy", "Present Energy", "Outcome Energy"]

    for pos in positions:
        card, orientation = pull_card(used_cards)
        used_cards.append(card)
        meaning = get_meaning(card, orientation, topic)

        st.subheader(f"{pos}")
        st.write(f"**{card}** ({orientation})")
        st.write(f"✨ Interpretation: {meaning}")

    st.success(f"Topic detected: {topic.capitalize()}")