import re
import requests

phone_regex = r'^\+{0,1}[1-9][0-9]{0,15}$'

def is_valid_phone_number(phone):
    return bool(re.match(phone_regex, phone))

def find_phone_numbers_in_text(text):
    return re.findall(phone_regex, text)

def find_phone_numbers_in_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return find_phone_numbers_in_text(response.text)
    else:
        raise Exception(f"Не удалось получить данные с URL: {url}")

def find_phone_numbers_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return find_phone_numbers_in_text(text)
