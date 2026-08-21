import subprocess
import time

print("Welcome to the Utility Runner!")
time.sleep(1)
print("This tool allows you to run various system utilities.")
time.sleep(1)

utilities = {
    "1": ("Disk Usage Analyzer", "bash scripts/disk-usage-analyzer.sh"),
    "2": ("Auto Backup", "bash scripts/auto-backup.sh"),
    "3": ("Bulk Renamer", "bash scripts/bulk-renamer.sh"),
    "4": ("Clean Logs", "bash scripts/clean-logs.sh"),
    "5": ("Service Health Check", "bash scripts/service-health-checker.sh"),
}

while True:

    print("\nAvailable utilities:")

    for number, (name, command) in utilities.items():
        print(f"{number}. {name}")

    choice = input("\nEnter utility number (or 'exit'): ")

    if choice == "exit":
        break

    if choice not in utilities:
        print("Invalid choice.")
        continue

    name, command = utilities[choice]

    print(f"\nRunning {name}...")

    try:

        if choice == "1":
            directory = input("Enter directory path: ")
            threshold = input("Enter threshold percentage: ")
            command = f"{command} '{directory}' {threshold}"

        elif choice == "2":
            source = input("Enter source path: ")
            destination = input("Enter backup destination: ")
            command = f"{command} '{source}' '{destination}'"

        elif choice == "3":
            directory = input("Enter directory path: ")
            old_name = input("Enter old text: ")
            new_name = input("Enter new text: ")
            command = f"{command} '{directory}' '{old_name}' '{new_name}'"

        elif choice == "4":
            directory = input("Enter directory path: ")
            pattern = input("Enter file pattern: ")
            days = input("Enter number of days: ")
            command = f"{command} '{directory}' '{pattern}' {days}"

        elif choice == "5":
            service = input("Enter service name: ")
            command = f"{command} '{service}'"

        subprocess.run(
            command,
            shell=True,
            check=True
        )

        print("\nUtility completed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"\nUtility failed with exit code: {e.returncode}")
