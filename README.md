# Microsnap

> **Work in progress:** Microsnap is under active development. Features, setup,
> and behavior may change, and the app is not yet a complete nutrition tracker.

Microsnap is a Streamlit app for a friendly AI nutrition companion. The planned
experience is to help people understand meals and estimate nutrition from food
photos or descriptions.

## Current status

The current prototype:

- Collects a user's name and WhatsApp number in an onboarding form.
- Creates a Gemini chat session using the nutrition-focused system prompt.

The food conversation interface, photo analysis, nutrition tracking, and
WhatsApp messaging are **not implemented yet**. The WhatsApp number is currently
collected for the planned experience; the app does not send messages or place
calls.

## Requirements

- Python 3.10 or newer
- A Google Gemini API key

## Run locally

1. Clone this repository and change into its directory.
2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Configure your Gemini API key using Streamlit's secrets file. Create
   `.streamlit/secrets.toml` and add:

   ```toml
   GEMINI_API_KEY = "your-gemini-api-key"
   ```

   Keep API keys private. Do not commit real credentials to the repository.

5. Start the app:

   ```bash
   streamlit run app.py
   ```

## Project files

- `app.py` — Streamlit application and onboarding flow.
- `prompts.py` — Instructions used to guide the nutrition assistant.
- `requirements.txt` — Python dependencies.

## Planned work

- Add a conversation interface for meal descriptions.
- Support food-photo analysis and nutrition estimates.
- Save and display nutrition history.
- Explore WhatsApp integration.

Nutrition estimates are intended as general guidance, not medical advice. They
can vary based on portion sizes, ingredients, and preparation methods.
