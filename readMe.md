#  DeepL Clipboard Translator

This script translates the content of the clipboard from English to German if it is in English language and vice versa. This is done by detecting a double press of Ctrl+C (within 0.5 seconds) and copying the translation back to the clipboard. The script uses the [DeepL API](https://www.deepl.com/pro#developer) for the translation.

## Usage

1. Start the script with `python3 clipboard_translator.py`
2. Copy some text to your clipboard (e.g. by selecting it and pressing Ctrl+C).
3. Press Ctrl+C twice in a row. The script will translate the text from English to German and copy the result to the clipboard and also automatically Pastes it if possible.

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [pynput](https://pypi.org/project/pynput/)
- [clipboard](https://pypi.org/project/clipboard/)
- [DeepL API Key](https://www.deepl.com/pro#developer)
- [langdetect](https://pypi.org/project/langdetect/)

## Setup

1. Install Python 3.
2. Install the required packages with `pip install deepl pynput clipboard langdetect` (or `pip3` instead of `pip`).
3. Create a .env file to save your API_KEY only locally. 
4. Get a free DeepL API Key by signing up for a DeepL Pro account [here](https://www.deepl.com/pro#developer).
5. Copy the API Key from the [DeepL Pro Account Page](https://www.deepl.com/pro-account/plan) into the `API_KEY` variable in the .env file.
```
API_KEY=your_api_key_as_displayed_by_DeepL
```

1. Start the script with `python clipboard_translator.py`
2. Copy some text to your clipboard (e.g. by selecting it and pressing Ctrl+C). -> *You`re already doing this by double tapping Ctrl+C twice*
3. Press Ctrl+C twice in a row. The script will translate the text from the detected language to English or if detected English to German and copy the result to the clipboard.
4. Press Ctrl+V to paste the translation somewhere.


 *This was created by the help of GPT-4 by OpenAI*