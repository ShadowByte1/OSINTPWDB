import subprocess

def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
        exit()

# Run OSINTPWD2
run_script("OSINTPWD2")

# Run osint.py
run_script("osint.py")
