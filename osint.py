import sys
import subprocess

def run_sherlock(username):
    try:
        # Run Sherlock using subprocess
        subprocess.run(['sherlock', username])
    except Exception as e:
        print(f"Error running Sherlock: {e}")

if __name__ == "__main__":
    # Check if the username is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python osint.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    run_sherlock(username)
