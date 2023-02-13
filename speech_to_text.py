import speech_recognition   # Speech to text library.

# Init Speech Recognition
listenbot = speech_recognition.Recognizer()


def get_voice_prompt_from_user():
    """
    Records the user's voice via the device's microphone and translates it to a text string (speech-to-text).

        Parameters:
            None.

        Returns:
            new_text (string): The user's voice input converted to a string.
    """

    try:
        # Use the microphone as source for input.
        with speech_recognition.Microphone() as source:
             
            # Wait for a second to let the recognizer adjust the volume threshold based on the surrounding noise level
            listenbot.adjust_for_ambient_noise(source, duration=0.5)
             
            # Listens to the user's voice input
            print("Listening. Please talk now.")
            audio = listenbot.listen(source)
            
            # Using google to convert speech to text
            new_text = listenbot.recognize_google(audio)
            print("Voice input: ",new_text)

            return new_text
             
    except speech_recognition.RequestError as e:
        print("Could not process speech recognition request; {0}".format(e))
         
    except speech_recognition.UnknownValueError:
        print("Could not understand what you said. Maybe there's a lot of background noise.")