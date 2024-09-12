"""
Request script.

Test a request to the HuggingFace Inference API.

Based on model card View Code sample here:
    https://huggingface.co/google/flan-t5-small
"""

import os

import requests


TOKEN = os.getenv("TOKEN")
MODEL_ID = os.getenv("MODEL", "google/flan-t5-small")
PROMPT = os.getenv("PROMPT", "The answer to the universe is")

API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def query(payload: dict) -> list[dict]:
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    return response.json()


output = query({"inputs": PROMPT})
print(output)
