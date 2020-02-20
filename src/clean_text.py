import re
import string

def text_to_lowercase(text):
    return text.lower()

def text_remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def text_remove_url(text):
    return re.sub(r"http\S+", "", text)

def text_remove_twitter_handle(text):
    return re.sub('@[^\s]+','',text)

def text_remove_leadtrail_spaces(text):
    return text.strip()

def clean_text(text):
    # order matters
    text1 = text_remove_twitter_handle(text)
    text2 = text_remove_url(text1)
    text3 = text_remove_punctuation(text2)
    text4 = text_to_lowercase(text3)
    text5 = text_remove_leadtrail_spaces(text4)
    return text5
    