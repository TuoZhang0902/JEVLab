import os
from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient, Choice

# 1. Load API key from .env
load_dotenv()

api_key = os.getenv("TYPESAFE_API_KEY")

if not api_key:
    raise ValueError("Missing TYPESAFE_API_KEY")

# 2. Initialize client
client = TypeSafeClient(model="jev-latest")

# 3. Send a test request
response = client.system_one(
    state="Alice is older than Bob. Bob is older than Charlie.",
    questions={
        "reasoning": Choice(
            instructions="Is Alice older than Charlie?",
            criteria={
                "yes": "True",
                "no": "False",
            },
        )
    },
)

# 4. Print result
print(response)

client.close()