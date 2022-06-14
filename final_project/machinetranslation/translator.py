import os
import json
import six
from dotenv import load_dotenv
from google.cloud import translate

#Api key and url


#Translates english to french
# Initialize Translation client
def english_to_french(english_text="Hello", project_id="ferrous-amphora-352613"):

    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{'ferrous-amphora-352613'}/locations/{'My First Project'}"

    # Translate text from English to French
    response = client.translate_text(
        request={
            "project_id": project_id,
            "location": location,
            "parent": parent,
            "contents": [english_text],
            "mime_type": "text/plain",  
            "source_language_code": "en-US",
            "target_language_code": "fr",
        }
    )

    # Display the translation for each input text provided
    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))
        print('\n')



# Translates french to english
# Initialize Translation client
def french_to_english(french_text="Bonjour", project_id="ferrous-amphora-352613"):
    """Translating Text."""

    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{'ferrous-amphora-352613'}/locations/{'MyFirstProject'}"

    # Translate text from English to French
    response = client.translate_text(
        request={
            "project_id": project_id,
            "location": location,
            "parent": parent,
            "contents": [french_text],
            "mime_type": "text/plain",  
            "source_language_code": "fr",
            "target_language_code": "en",
        }
    )

    # Display the translation for each input text provided
    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))

