import argparse
import subprocess

def run_sherlock(username):
    try:
        # Run Sherlock using subprocess
        subprocess.run(['sherlock', username])
    except Exception as e:
        print(f"Error running Sherlock: {e}")

def main():
    parser = argparse.ArgumentParser(description='Run Sherlock with a specified username.')
    parser.add_argument('username', metavar='username', type=str, nargs='?', help='The username to search for')

    args = parser.parse_args()

    if not args.username:
        # Ask for a username if not provided
        args.username = input("Enter the username for osint.py: ")

    run_sherlock(args.username)

if __name__ == "__main__":
    main()
