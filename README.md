# System Utilities CLI Toolkit

## Overview
This is a small Python-based CLI application that orchestrates five Bash-based system utilities. The project is designed to demonstrate how a small application can be validated through automated testing and CI, then packaged and released as an artifact through CD without requiring server deployment.

### The application itself is intentionally small. I used it to focus on how software moves from development to a validated and releasable artifact.

## Architecture

The application uses a simple Python-to-Bash architecture.

Python acts as the CLI orchestrator and collects user input and required arguments. It then executes the appropriate Bash script using `subprocess`.

```text
User
  ↓
Python CLI (app.py)
  ↓
Collect arguments
  ↓
Execute Bash script
  ↓
Linux utilities / system commands
  ↓
Exit code
  ↓
Python displays result

```

## Utilities

The toolkit currently provides five Bash-based utilities:
| Utility                | Purpose                                                             |
| ---------------------- | ------------------------------------------------------------------- |
| Disk Usage Analyzer    | Analyzes disk usage and checks usage against a defined threshold.   |
| Auto Backup            | Creates a compressed backup of a specified source directory.        |
| Bulk Renamer           | Renames multiple files based on specified patterns.                 |
| Log Cleaner            | Removes matching log files based on their age.                      |
| Service Health Checker | Checks whether a Linux system service is running using `systemctl`. |


## How It Works

- The user starts the Python CLI.
- The CLI displays the available utilities.
- The user selects a utility.
- Python collects the arguments required by that utility.
- Python executes the corresponding Bash script.
- The Bash script performs the required operation.
- The Bash script returns an exit code.
- Python reports the result or error to the user.

## Project Structure

```text
System-Utilities-CLI/
├── app.py
├── scripts/
│   ├── disk-usage-analyzer.sh
│   ├── auto-backup.sh
│   ├── bulk-renamer.sh
│   ├── clean-logs.sh
│   └── service-health-checker.sh
├── tests/
│   ├── bulkfolder/
│   ├── destination_folder/
│   └── source_folder/
├── logs/
│   └── backup.txt
├── NOTES.md
└── README.md

```

## How to Run

#### Prerequisites
- Python 3
- Bash
- Linux utilities used by the scripts
- Linux environment for the Service Health Checker
- Run the CLI

From the project root:

```
python3 app.py
```
Select a utility and provide the required arguments when prompted.
The Bash scripts can also be executed independently from the command line.

For example:
````
bash scripts/auto-backup.sh <source_path> <backup_destination>
bash scripts/clean-logs.sh <directory> <file_pattern> <days>
````
## Testing

The project will include basic automated tests to verify that:

- Required scripts are present.
- The Python application is valid.
- Bash scripts execute successfully with valid arguments.
- Invalid arguments return appropriate exit codes.
- Core utility operations produce the expected results.

Testing will be executed locally and later integrated into the CI workflow.

## CI/CD

```text 
                  DEVELOPMENT
                       │
                       ▼
                  git push
                       │
                       ▼
                  ┌─────────┐
                  │   CI    │
                  └────┬────┘
                       │
                  Run tests
                       │
                ┌──────┴──────┐
              PASS           FAIL
                │               │
                ▼               ▼
             Continue          STOP
                │
                ▼
           Create v1.0.0 tag
                │
                ▼
              ┌─────┐
              │ CD  │
              └──┬──┘
                 │
                 ▼
             Package
                 │
                 ▼
          GitHub Release
                 │
                 ▼
       .tar.gz artifact

```
#### Continuous Integration

GitHub Actions will automatically validate the project when changes are pushed.

The CI workflow will perform:

- Python validation
- Bash script validation
- ShellCheck checks
- Automated tests

A failed check will cause the CI workflow to fail.

#### Continuous Delivery

After successful CI validation, the project will be packaged into a release artifact.The artifact will be published as a GitHub release.

No server or cloud deployment is included in the current CD scope.

## Future Scope  

Potential future improvements include:

- A web or graphical interface for the utilities.
- Docker-based packaging.
- Infrastructure provisioning using Terraform.
- Deployment to a cloud-based Linux environment such as AWS.
- Extending the delivery pipeline to support cloud deployment.

Feel free to suggest improvements or ideas. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


