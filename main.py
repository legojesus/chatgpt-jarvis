### J.A.R.V.I.S AI in Python - A speech-to-text to ChatGPT to text-to-speech program. 
### Basically allows you to talk to ChatGPT and hear it talking back. 
# Author: Yaron K.
# Date: 2023-02-12

from speech_to_text import get_voice_prompt_from_user
from chatgpt import send_prompt_to_openai
from text_to_speech import read_answer_to_user


# Keep program running non-stop
while True:
    # Get prompt from user's voice and convert to text
    prompt = get_voice_prompt_from_user()

    # Send prompt to OpenAI and get answer
    answer = send_prompt_to_openai(prompt)

    # Read the answer back to the user
    read_answer_to_user(answer)