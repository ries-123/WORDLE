

# We will use this to suppress some warnings that are not important
import warnings

# Suppress specific Pydantic warnings that clutter the output
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

# We will use dotenv to read the .env file
from dotenv import load_dotenv
load_dotenv()

# This import will return an error if LiteLLM is not installed 
import litellm
import os

# Use this to measure response time
import time

# URL of Ohio State's LiteLLM proxy server
custom_api_base = "https://litellmproxy.osu-ai.org" 

# Our API key for Astronomy 1221 (keep this private to our class)
astro1221_key = os.getenv("ASTRO1221_API_KEY")

guesses_left = 3
word = "EARTH"
if guesses_left == 3:
    hint = input("do you want a hint? yes/no: ").lower()
    if hint == "yes":
        if not astro1221_key:
            print("Cannot get hint: ASTRO1221_API_KEY not set in .env")
        else:
            try:
                response = litellm.completion(
                    model="claude-3-5-sonnet-20241022",
                    messages=[
                        {"role": "user", "content": f"The word is {word}. Give me a hint that will help me guess the word in less than 100 characters."}
                    ],
                    max_tokens=100,
                    api_base=custom_api_base,
                    api_key=astro1221_key,
                )
                print(response.choices[0].message.content)
            except Exception as e:
                err = str(e)
                if "401" in err or "authentication" in err.lower():
                    print("API error: Invalid API key (401). Check that your .env has ASTRO1221_API_KEY set for the OSU LiteLLM proxy.")
                else:
                    print(f"API error: {e}")