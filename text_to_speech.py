import pyttsx3  # Text to speech synthesizer.


# Init pyttsx3 (Py Text-To-Speech)
talkbot = pyttsx3.init()
talkbot.setProperty('rate', 135)                # Setting the voice's talking speed
talkbot.setProperty('volume',1.0)               # Setting the volume level between 0 and 1
voices = talkbot.getProperty('voices')          # Getting details of current voice
# talkbot.setProperty('voice', voices[0].id)    # Set voice to male 
talkbot.setProperty('voice', voices[1].id)      # Set voice to female



def read_answer_to_user(answer):
    """
    Reads ChatGPT's answer back to the user (text-to-speech).

        Parameters:
            answer (string): ChatGPT's answer to the user's prompt/question/request.

        Returns:
            None.
    """

    talkbot.say(answer)
    talkbot.runAndWait()
    talkbot.stop()