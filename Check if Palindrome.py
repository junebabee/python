import re

def is_palindarome(text):
    
    text = re.sub('[!@?., \'\"]', '', text)
    if text.lower() == text[::-1].lower():
        return True
    else:
        return False
