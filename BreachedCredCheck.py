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

def format_breach_info(breach_info):
    formatted_output = ""
    
    for breach in breach_info['result']:
        formatted_output += "\n[+] Breach      : {}".format(breach.get('title', 'N/A'))
        formatted_output += "\n[+] Domain      : {}".format(breach.get('domain', 'N/A'))
        formatted_output += "\n[+] Date        : {}".format(breach.get('breachDate', 'N/A'))
        formatted_output += "\n[+] BreachedInfo: {}".format(breach.get('dataClasses', 'N/A'))
        formatted_output += "\n[+] Fabricated  : {}".format(breach.get('isFabricated', 'N/A'))
        formatted_output += "\n[+] Verified    : {}".format(breach.get('isVerified', 'N/A'))
        formatted_output += "\n[+] Retired     : {}".format(breach.get('isRetired', 'N/A'))
        formatted_output += "\n[+] Spam        : {}".format(breach.get('isSpamList', 'N/A'))
        formatted_output += "\n-----\n"
    
    return formatted_output

if __name__ == "__main__":
    # Prompt the user to enter a username
    username = input("Enter the username to test for: ")
    
    # Replace "<REPLACE_WITH_ACTUAL_TERM>" with the entered username
    required_term = username
    
    result = run_breach_directory_query(required_term)
    
    # Format and print the breach information
    formatted_output = format_breach_info(result)
    print(formatted_output)
