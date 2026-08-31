## Project Scope

### Purpose

System Utilities CLI Toolkit is a Python-based CLI application that allows users to run several Bash-based system utilities while handling user input, command-line arguments, and errors consistently.

### Learning Objectives

This project demonstrates the integration of Python and Bash along with automated testing, Continuous Integration (CI), and Continuous Delivery (CD) through package and artifact release without deploying the application to a server.

### Core Application

The Python CLI provides access to five Bash-based system utilities for common system administration tasks:

1. Disk Usage Analyzer
2. Auto Backup
3. Bulk Renamer
4. Log Cleaner
5. Service Health Checker — Linux-based utility using `systemctl`

### In Scope

- Bash scripting and Linux utilities
- Python CLI orchestration
- Command-line argument handling
- Exit codes and error handling
- Git for source code management
- Automated testing
- GitHub Actions for Continuous Integration
- Package creation and artifact release for Continuous Delivery

### CI/CD Scope

CI will perform automated validation and testing of the project whenever changes are pushed to GitHub.

After successful CI validation, CD will package the project and publish the resulting artifact as a release.

No server or cloud deployment is included in the current project scope.

### Future Scope

- Web or graphical interface for the utilities
- Containerization using Docker
- Infrastructure provisioning using Terraform
- Deployment to a cloud-based Linux environment such as AWS

### The application itself is intentionally small. I used it to focus on how software moves from development to a validated and releasable artifact.

# What I learned:

1. Python "import subprocesses"
Python subprocess is a tool built into Python that lets you run other programs directly from your Python code.Think of it like opening your computer's terminal (or Command Prompt) and typing a command, but Python does it for you automatically.

2. Python can execute Bash scripts : subprocess.run(...) --> can launch:
````
bash scripts/disk-usage-analyzer.sh
````
So Python can act as the CLI controller/orchestrator, while Bash performs the Linux operation.

3. capture_output=True changes the CLI experience

We initially had: capture_output=True

That captures the output instead of letting the Bash script interact naturally with the terminal. For an interactive CLI tool, we learned that:
````
subprocess.run(command, shell=True, check=True)
````
is more appropriate.

4. Exit codes — simple version

An exit code is the status a program gives back when it finishes.

Think of it as:

Program runs
    ↓
Program finishes
    ↓
"How did I do?"
    ↓
Exit code
The two most important rules
0     → Success ✅
non-0 → Something went wrong ❌
