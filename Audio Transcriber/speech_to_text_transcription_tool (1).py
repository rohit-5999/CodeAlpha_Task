# -*- coding: utf-8 -*-
"""Speech-to-Text Transcription Tool

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1anP0jm4HHg2dNaF0V9GXEywgTyusGedu
"""

import speech_recognition as sr
import os

AUDIO_FILE_PATH = "/content/Demo1.wav"

# --- Main Function for Transcription ---
def transcribe_audio(audio_file):
    """
    Transcribes an audio file into text using Google Web Speech API.

    Args:
        audio_file (str): The path to the audio file to transcribe.

    Returns:
        str: The transcribed text, or an error message if transcription fails.
    """
    # Initialize the recognizer
    r = sr.Recognizer()

    # Check if the audio file exists
    if not os.path.exists(audio_file):
        return f"Error: Audio file not found at '{audio_file}'."

    # Use the audio file as the audio source
    try:
        with sr.AudioFile(audio_file) as source:
            print(f"Loading audio file: {audio_file}...")
            audio = r.record(source) # Read the entire audio file
            print("Audio loaded. Attempting to transcribe...")

        # Recognize speech using Google Web Speech API
        # This requires an internet connection.

        text = r.recognize_google(audio)
        return f"Transcription:\n{text}"

    except sr.UnknownValueError:
        return "Speech Recognition could not understand audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech API service; {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Speech-to-Text Transcription Tool ---")

    # Example call to the transcription function
    transcribed_text = transcribe_audio(AUDIO_FILE_PATH)
    print("\n" + transcribed_text)

    print("\n--- Transcription Process Complete ---")
    print("To transcribe a different file, change the 'AUDIO_FILE_PATH' variable.")
    print("Make sure the audio file is clear and speech is audible for best results.")

!pip install SpeechRecognition

"""You can upload files to your Colab environment using the file upload feature in the left sidebar. Click on the folder icon, then the upload icon (an arrow pointing upwards) to select and upload your audio file. Once uploaded, the file will be available in the `/content/` directory.

After uploading, you'll need to update the `AUDIO_FILE_PATH` in the code to point to the correct location, which will likely be something like `/content/your_audio_file_name.wav`.
"""