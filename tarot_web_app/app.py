# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 01:19:40 2026

@author: test
"""

import pandas as pd
import random

df = pd.read_csv("C:/Users/test/OneDrive/Desktop/tarot_data_full_major_arcana.csv")

def detect_topic(question):
    question = question.lower()
    if "exam" in question:
        return "exam"
    elif "love" in question:
        return "love"
    else:
        return "general"

def pull_card():
    card_name = random.choice(df["card_name"].unique())
    orientation = random.choice(["upright", "reversed"])
    return card_name, orientation

def get_meaning(card_name, orientation, topic):
    result = df[
        (df["card_name"] == card_name) &
        (df["orientation"] == orientation) &
        (df["topic"] == topic)
    ]
    return result.iloc[0]["meaning"]

# 🔮 THIS must come before using question
question = input("Ask your tarot question: ")

topic = detect_topic(question)
card, orientation = pull_card()
meaning = get_meaning(card, orientation, topic)

print(card, orientation)
print(topic)
print(meaning)