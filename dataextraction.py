import json
import re
from bs4 import BeautifulSoup


def json_data(file_path):
    try:
        # Step 1: Read the JSON file with proper encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            # Step 2: Parse the JSON data
            data = json.load(file)

        # Step 3: Return the Python data structure
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {file_path}")

def extract_cyrillic(text):
    # Use a regular expression to find all Cyrillic characters
    cyrillic_pattern = r'[а-яА-ЯёЁ]+'
    cyrillic_matches = re.findall(cyrillic_pattern, text)
    return cyrillic_matches

def extract_cyrillic_text_from_html(html_data):
    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_data, 'html.parser')
    # Extract the Cyrillic text from the parsed HTML
    cyrillic_text = soup.get_text()
    return cyrillic_text

def extract_cyrillic_sentences(data):
    cyrillic_sentences = []

    def extract_from_value(value):
        if isinstance(value, str):
            # Extract Cyrillic sentences from HTML content if present
            cyrillic_text = extract_cyrillic_text_from_html(value)
            if cyrillic_text:
                # Use regex to split sentences by a period followed by a space or double space
                sentences = re.split(r'\.\s+|\s{2,}', cyrillic_text)
                cyrillic_sentences.extend(sentences)
            else:
                # Otherwise, extract Cyrillic words from regular text
                cyrillic_matches = extract_cyrillic(value)
                if cyrillic_matches:
                    cyrillic_sentences.append(' '.join(cyrillic_matches))

        elif isinstance(value, list):
            for item in value:
                extract_from_value(item)

        elif isinstance(value, dict):
            for key, val in value.items():
                extract_from_value(val)

    extract_from_value(data)
    return cyrillic_sentences

def find_sentences_with_keywords(sentences_list, keywords):
    matching_sentences = []

    for sentence in sentences_list:
        for keyword in keywords:
            if keyword.lower() in sentence.lower():  # Case-insensitive search
                # Exclude sentences containing "Пари нн", "пари НН", "Пари НН"
                if "Пари нн" not in sentence and "пари НН" not in sentence and "Пари НН" not in sentence:
                    matching_sentences.append(sentence)
                break  # Break out of the inner loop once a match is found for the current sentence

    return matching_sentences


def process_json_files(file_paths, keywords_to_find):
    all_matching_sentences = []  # List to store all matching sentences across all files

    for file_path in file_paths:
        data = json_data(file_path)

        cyrillic_sentences_list = extract_cyrillic_sentences(data)
        matching_sentences_list = find_sentences_with_keywords(cyrillic_sentences_list, keywords_to_find)

        # Add the matching sentences for this file to the overall list
        all_matching_sentences.extend(matching_sentences_list)

    return all_matching_sentences

# Example usage:
file_paths_to_process = [
    "/Users/maximquartly/lstitles/titles/output.json",
    "/Users/maximquartly/lstitles/titles/output2.json",
    "/Users/maximquartly/lstitles/titles/output3.json",
    "/Users/maximquartly/lstitles/titles/output4.json",
    "/Users/maximquartly/lstitles/titles/output5.json",
    "/Users/maximquartly/lstitles/titles/output6.json", 
    "/Users/maximquartly/lstitles/titles/output7.json"
]

keywords_to_find_1 = ["Лига Ставок", "лига ставок", "Liga Stavok", "liga stavok"]
keywords_to_find_2 = ["Фонбет", "фонбет", "Fonbet", "fonbet"]
keywords_to_find_3 = ["Винлайн", "винлайн", "Winline", "winline"]
keywords_to_find_4 = ["Бетбум", "бетбум", "Betboom", "betboom"]
keywords_to_find_5 = ["Пари", "пари", "Pari", "pari"]
keywords_to_find_6 = ["Олимпбет", "олимпбет", "Olimpbet", "olimpbet"]
keywords_to_find_7 = ['Лтга ставок', 'Сочи', 'ФК Сочи', 'ХК Сочи', 'Sochi Hockey Open', 'футбольный клуб сочи', 'хоккейный клуб сочи', 'ФК Ахьат', 'ХК СКА', 'Сборная России', 'ХК Адмирал','ХК Авангард', 'Чемптонат ФХР ЗХЗ - ЛИГА СТАВОК Sochi XHL']

#list by compnay name 
LS_list = process_json_files(file_paths_to_process, keywords_to_find_1)
Fonbet_list = process_json_files(file_paths_to_process, keywords_to_find_2)
Winline_list = process_json_files(file_paths_to_process, keywords_to_find_3)
Betboom_list = process_json_files(file_paths_to_process, keywords_to_find_4)
Pari_list = process_json_files(file_paths_to_process, keywords_to_find_5)
Olimpbet_list = process_json_files(file_paths_to_process, keywords_to_find_6)
list7 = process_json_files(file_paths_to_process, keywords_to_find_7)

# Printing by company 
print( LS_list)
print(Fonbet_list)
print(Winline_list)
print(Betboom_list)
print(Pari_list)
print(Olimpbet_list)
print(list7)