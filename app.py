import subprocess

utilities = {
    "1": ("List Files","ls -la"),
    "2": ("Disk Usage","df -h"),
    "3": ("System Information","uname -a"),
    "4": ("Network Status","ping -c 1 google.com"),
    "5": ("Check Memory Usage","free -h"),
    "6": ("Check CPU Usage","top -bn1 | grep 'Cpu(s)'"),
    "7": ("Perform Auto Backup","auto_backup.sh")
}

while True:
    print("Available utilities:")
    for key in utilities.keys():
        print(f"- {key}")
    
    choice = input("Enter the utility you want to run (or 'exit' to quit): ")
    
    if choice == "exit":
        break
    elif choice in utilities:
        command = utilities[choice]
        try:
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while executing the command: {e}")
    else:
        print("Invalid choice. Please try again.")