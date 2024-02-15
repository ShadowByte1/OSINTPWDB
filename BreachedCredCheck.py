import requests
import json
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def run_breach_directory_query(required_term):
    url = "https://breachdirectory.p.rapidapi.com/"
    
    querystring = {"func": "auto", "term": required_term}
    
    headers = {
        "X-RapidAPI-Key": "18126ca6a6mshbc1f9e90e0292a3p191e71jsnd999a0dc0937",
        "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    return response.json()

def pretty_print(json_data):
    formatted_json = json.dumps(json_data, indent=4)
    colored_json = highlight_json(formatted_json)
    print(colored_json)

def highlight_json(json_string):
    # Highlight keywords in JSON output
    keywords = ["true", "false", "null"]
    for keyword in keywords:
        json_string = json_string.replace(keyword, f"{Fore.CYAN}{keyword}{Style.RESET_ALL}")
    return json_string

if __name__ == "__main__":
    # Prompt the user to enter a username
    username = input("Enter the Email to test for: ")
    
    # Replace "<REPLACE_WITH_ACTUAL_TERM>" with the entered username
    required_term = username
    
    result = run_breach_directory_query(required_term)
    
    # Print the formatted and colored JSON
    pretty_print(result)
