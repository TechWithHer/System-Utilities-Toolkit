       
       
       
  # Architechture
       
       
                 Python CLI
                     │
              User selects utility
                     │
        ┌────────────┴─────────────┐
        │                          │
  No arguments                Needs arguments
        │                          │
        │                    Python asks user
        │                          │
        │                    folder / threshold
        │                          │
        └────────────┬─────────────┘
                     ↓
              subprocess.run()
                     ↓
                 Bash script
                     ↓
              Linux commands
                     ↓
                 Exit code
                     ↓
              Python handles result


