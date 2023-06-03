from pynput import keyboard
from time import time
import clipboard
import deepl
# Using langdetect instead of deepl for speech recognition
from langdetect import detect
import os
from dotenv import load_dotenv
load_dotenv()


# The time the last "Ctrl+C" was pressed
last_ctrl_c = 0

# The interval within which two "Ctrl+C" presses are considered a double press
double_press_interval = 0.5

# The DeepL API key stored in .env
deepl_key = os.getenv("API_KEY")
print(f"used DeepL API key: {deepl_key}")

translator = deepl.Translator(deepl_key)


def on_activate():
    text = clipboard.paste()
    if len(text.strip()) > 0:
        print(f"Detected double Ctrl+C. Current clipboard content: {text}")

        # try to check text language with langdetect and make it uppercase

        try:
            language = detect(text).upper()
            print(f"Detected language: {language}")

        except Exception as e:
            print(f"Could not detect language: {e}")
            language = "EN"

        try:
            # if language is English, translate to German
            if language == "EN":
                print("Detected English text, translating to German.")
                translation = translator.translate_text(text, target_lang='DE')
            # if language is German, translate to English
            elif language == "DE":
                print("Detected German text, translating to English.")
                translation = translator.translate_text(
                    text, target_lang='EN-US')
            # if language is neither English nor German, translate to English
            else:
                print(
                    "Detected neither English nor German text, translating to English.")
                translation = translator.translate_text(
                    text, target_lang='EN-US')
        except Exception as e:
            print(f"Could not translate text: {e}")
            translation = text

        print(f"Translation result: {translation.text}")
        # try to copy the translation back to the clipboard
        try:
            thisKbd = keyboard.Controller()

            clipboard.copy(translation.text)
            print("Translated text copied back to clipboard.")
            # then paste it with Ctrl+V
            thisKbd.press(keyboard.Key.ctrl)
            thisKbd.press('v')
            thisKbd.release('v')
            thisKbd.release(keyboard.Key.ctrl)

        except Exception as e:
            print(f"Could not copy translated text to clipboard: {e}")
    else:
        print("Detected double Ctrl+C, but clipboard was empty.")


hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+c'),
    on_activate)


def on_press(key):
    global last_ctrl_c
    if str(key) == "'c'":
        if time() - last_ctrl_c < double_press_interval:
            on_activate()
        last_ctrl_c = time()


with keyboard.Listener(on_press=on_press) as listener:
    print("Starting listener.")

    listener.join()
    print("Listener stopped.")
