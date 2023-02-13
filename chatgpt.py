import openai   # OpenAI API for processing text and reply like a human.
import os       # For getting the API key from environment variable.
from dotenv import load_dotenv  # For getting the API key from .env file into the environment.

load_dotenv()

# Init OpenAI
openai.api_key = os.getenv("API_KEY")
model_engine = "text-davinci-003"   # The OpenAI GPT-3 model version. Reference: https://platform.openai.com/docs/models/gpt-3


def send_prompt_to_openai(prompt):
    """
    Sends a text prompt to OpenAI API and returns an answer from ChatGPT.

        Parameters:
            prompt (string): A string of a qustion or request to be sent to OpenAI's ChatGPT.

        Returns:
            reply (string): The answer received from ChatGPT.
    """
    # Send prompt to ChatGPT and get possible replies. Reference: https://platform.openai.com/docs/api-reference/completions/create
    completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=2000, n=1, stop=None, temperature=0.7)

    # Get the first reply
    reply = completion.choices[0].text
    print("Chat GPT says: ", reply)
    print("\n")

    return reply