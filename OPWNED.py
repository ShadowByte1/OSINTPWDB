import os
import sys
import requests
import sherlock
from dotenv import load_dotenv

load_dotenv()

def search_hibp(email):
    """
    Searches the Have I Been Pwned API for the given email address.
    """
    url = "https://haveibeenpwned.com/api/v3/breachedaccount/" + email
    headers = {
        "hibp-api-key": os.getenv("HIBP_API_KEY")
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def search_breach_directory(email):
    """
    Searches the Breach Directory API for the given email address.
    """
    url = "https://breachdirectory.p.rapidapi.com/"
    querystring = {
        "func": "auto",
        "term": email
    }
    headers = {
        "X-RapidAPI-Key": os.getenv("BREACH_DIRECTORY_API_KEY"),
        "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    return None

def search_email(email):
    """
    Searches Sherlock for the given email address.
    """
    s = sherlock.Sherlock()
    results = s.find_email(email)
    return results

def main():
    email = "<REQUIRED>"
    hibp_data = search_hibp(email)
    breach_data = search_breach_directory(email)
    email_data = search_email(email)

    print("Have I Been Pwned:")
    if hibp_data is not None:
        print("Found in the following breaches:")
        for breach in hibp_data["Breaches"]:
            print("- " + breach["Name"])
    else:
        print("No breaches found.")

    print("\nBreach Directory:")
    if breach_data is not None:
        if "breaches" in breach_
            print("Found in the following breaches:")
            for breach in breach_data["breaches"]:
                print("- " + breach["Title"])
        else:
            print("No breaches found.")
    else:
        print("No breaches found.")

    print("\nSherlock:")
    if email_data:
        print("Found on the following websites:")
        for website in email_data:
            print("- " + website)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
