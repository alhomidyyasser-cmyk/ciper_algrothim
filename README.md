# Cipher X

Cipher X is a small Streamlit application for encoding and decoding text with a reversible Unicode character shift. It includes an interactive web interface and a command-line example.

> **Security note:** This is a learning and obfuscation tool, not encryption. It does not protect sensitive information and should not be used for passwords, secrets, or secure communications.

## Features

- Encode and decode text using a numeric shift key.
- Works with Unicode text, including Arabic and emoji.
- Provides a Streamlit web interface and reusable `encode` / `decode` functions.

## Requirements

- Python 3.9 or newer
- Dependencies listed in [`requirements.txt`](requirements.txt)

## Installation

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS or Linux, activate the environment with:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the web app

From the project directory, start Streamlit:

```bash
streamlit run app.py
```

Open the local URL printed by Streamlit. Choose **Encode** or **Decode**, enter the same numeric key for both operations, and submit the text.

## Command-line example

Run the command-line demonstration:

```bash
python main.py
```

The command-line example uses key `4`. The web app defaults to key `5`; decoding requires the same key that was used to encode the text.

## Use the functions

```python
from main import decode, encode

ciphertext = encode("Hello, world!", key=5)
plaintext = decode(ciphertext, key=5)
assert plaintext == "Hello, world!"
```

`encode` and `decode` accept an optional `space` offset, which defaults to the `SPACE` constant (`1510`). They operate on valid Unicode scalar values; unpaired surrogate characters are rejected.

## Tests

Run the built-in unit tests from the project directory:

```bash
python -m unittest
```
