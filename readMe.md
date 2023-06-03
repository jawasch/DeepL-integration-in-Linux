#  DeepL Clipboard Translator

This script translates the content of the clipboard from English to German if it is in English language and vice versa. This is done by detecting a double press of Ctrl+C (within 0.5 seconds) and copying the translation back to the clipboard. The script uses the [DeepL API](https://www.deepl.com/pro#developer) for the translation.

## Usage

1. Start the script with `python3 clipboard_translator.py`
2. Copy some text to your clipboard (e.g. by selecting it and pressing Ctrl+C).
3. Press Ctrl+C twice in a row. The script will translate the text from English to German and copy the result to the clipboard.
4. Press Ctrl+V to paste the translation somewhere.

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [pynput](https://pypi.org/project/pynput/)
- [clipboard](https://pypi.org/project/clipboard/)
- [DeepL API Key](https://www.deepl.com/pro#developer)
- [langdetect](https://pypi.org/project/langdetect/)

## Setup

1. Install Python 3.
2. Install the required packages with `pip install deepl pynput clipboard langdetect` (or `pip3` instead of `pip`).
3. Get a free DeepL API Key by signing up for a DeepL Pro account [here](https://www.deepl.com/pro#developer).
4. Copy the API Key from the [DeepL Pro Account Page](https://www.deepl.com/pro-account/plan) into the `deepl_key` variable at the top of the script.
5. Start the script with `python clipboard_translator.py`
6. Copy some text to your clipboard (e.g. by selecting it and pressing Ctrl+C).
7. Press Ctrl+C twice in a row. The script will translate the text from English to German and copy the result to the clipboard.
8. Press Ctrl+V to paste the translation somewhere.


 *This was created by the help of GPT-4 by OpenAI*