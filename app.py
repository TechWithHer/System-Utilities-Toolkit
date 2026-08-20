import subprocess
import time

print("Welcome to the Utility Runner!")
time.sleep(2)
print("This tool allows you to run various system utilities.")
time.sleep(2)

utilities = {
    "1": "bash scripts/disk-usage-analyzer.sh",
    "2": "bash scripts/auto-backup.sh",
    "3": "bash scripts/bulk-renamer.sh",
    "4": "bash scripts/clean-logs.sh",
    "5": "bash scripts/service-health-checker.sh",
}

while True:
    print("Available utilities:")
    for key in utilities.keys():
        print(f"- {key}: {utilities[key]}")

    choice = input("Enter the utility number you want to run any specific utility(or 'exit' to quit): ")
    
    if choice == "exit":
        break
    elif choice in utilities:
        command = utilities[choice]
        try:
            result = subprocess.run(command, shell=True, check=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while executing the command: {e}")
            print(f"Error output: {e.stderr}")
    else:
        print("Invalid choice. Please try again.")