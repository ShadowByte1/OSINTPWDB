import requests

def run_breach_directory_query(required_term):
    url = "https://breachdirectory.p.rapidapi.com/"
    
    querystring = {"func": "auto", "term": required_term}
    
    headers = {
        "X-RapidAPI-Key": "18126ca6a6mshbc1f9e90e0292a3p191e71jsnd999a0dc0937",
        "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    return response.json()

if __name__ == "__main__":
    # Prompt the user to enter a username
    username = input("Enter the username to test for: ")
    
    # Replace "<REPLACE_WITH_ACTUAL_TERM>" with the entered username
    required_term = username
    
    result = run_breach_directory_query(required_term)
    
    print(result)
