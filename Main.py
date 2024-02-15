import subprocess

def run_script(script_name, *args):
    try:
        subprocess.run(["python", script_name, *args], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
        exit()

# Get user input for email
email = input("Enter the email for OSINTPWD2: ")

# Run OSINTPWD2 with the provided email
run_script("OSINTPWD2", "-e", email)

# Run osint.py with the provided username
run_script("osint.py")

# Run BreachedCredCheck.py
run_script("BreachedCredCheck.py")
