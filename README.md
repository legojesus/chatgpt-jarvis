# J.A.R.V.I.S AI in Python (ChatGPT)
This python code allows the user to talk to ChatGPT and hear ChatGPT talk back! Just like JARVIS from Iron Man ;)

The flow is simple: User talks -> speech2text -> ChatGPT -> text2speech -> User. 

Libraries used:
- openAI's python library for ChatGPT completion
- SpeechRecognition library for speech2text abilities via Google.
- pyttsx3 for text2speech abilities. 


### How to run:
1. Install the required libraries in the "requirements.txt" file (`pip install -r requirements.txt`).
2. Get an API key from OpenAI (signup required): https://platform.openai.com/account/api-keys
3. Create a new file called `.env` where the "main.py" file is, and add the following line to it: `API_KEY=xxxxxxxxxxxxxxx`. Replace the "xxxxxxxx" with the API key from OpenAI.
4. Run "main.py". 


Built and tested on Windows 10 with Python 3.10. 
This will have different requirements on Mac/Linux due to different sound card/microphone setups. 
