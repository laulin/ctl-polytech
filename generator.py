from hashlib import sha256
from yaml import safe_load
import random
import base64
import secrets

with open("questions.yaml") as f:
    questions = safe_load(f)

NUMBER_OF_QUESTIONS = 1

indexes = random.sample(range(len(questions)), NUMBER_OF_QUESTIONS)
print(indexes)
selected_questions = [k for i, k in enumerate(questions.keys()) if i in indexes]
print(selected_questions)

def create_secret(indexes):

    merged = bytes(".".join(indexes), "utf8")
    mask = secrets.token_bytes(len(merged))
    crypted = [m1 ^ m2]

