""" Translator module, features EN-FR, EN-DE """
import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

API_URL = os.environ.get("api-url")
API_KEY = os.environ.get("api-key")

language_translator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=IAMAuthenticator(API_KEY)
)
language_translator.set_service_url(API_URL)

def englishtofrench(english_text):
    """ Translates EN to FR using the IBM Watson Service """
    return language_translator.translate(
        text=english_text, model_id='en-fr'
    ).get_result()['translations'][0]['translation']

def englishtogerman(english_text):
    """ Translates EN to DE using the IBM Watson Service """
    return language_translator.translate(
        text=english_text, model_id='en-de'
    ).get_result()['translations'][0]['translation']
