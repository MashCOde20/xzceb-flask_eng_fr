import os
from google.cloud import translate_v3 as translate  # Use the correct import for the translation module
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the project ID
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT_ID")  # Ensure you set this in your .env

# Translates English to French
def english_to_french(english_text: str, project_id: str = PROJECT_ID) -> str:
    """Translate English text to French."""
    
    client = translate.TranslationServiceClient()

    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    # Translate text from English to French
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [english_text],
            "mime_type": "text/plain",  
            "source_language_code": "en-US",
            "target_language_code": "fr",
        }
    )

    # Collect translations
    translations = [translation.translated_text for translation in response.translations]
    
    # Return the first translation (assuming only one input text)
    return translations[0] if translations else ""

# Translates French to English
def french_to_english(french_text: str, project_id: str = PROJECT_ID) -> str:
    """Translate French text to English."""
    
    client = translate.TranslationServiceClient()

    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    # Translate text from French to English
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [french_text],
            "mime_type": "text/plain",  
            "source_language_code": "fr",
            "target_language_code": "en",
        }
    )

    # Collect translations
    translations = [translation.translated_text for translation in response.translations]
    
    # Return the first translation (assuming only one input text)
    return translations[0] if translations else ""

# Example usage
if __name__ == "__main__":
    english_text = "Hello"
    french_translation = english_to_french(english_text)
    print(f"Translated '{english_text}' to French: '{french_translation}'")
    
    french_text = "Bonjour"
    english_translation = french_to_english(french_text)
    print(f"Translated '{french_text}' to English: '{english_translation}'")
