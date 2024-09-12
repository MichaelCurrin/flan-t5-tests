"""
Request script.

HuggingFace Inference API test.

Based on model card View Code sample here:
    https://huggingface.co/google/flan-t5-small
"""

import os

import requests


TOKEN = os.getenv("TOKEN")
MODEL = os.getenv("MODEL", "google/flan-t5-small")
PROMPT = os.getenv("PROMPT", "The answer to the universe is")

API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def query(payload: dict) -> list[dict]:
    response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=2)

    return response.json()


output = query({"inputs": PROMPT})
print(output)
