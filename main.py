from counter import process_text, process_file
from pathlib import Path

# Get the data directory path
data_dir = Path("data")

# Check if directory exists
if not data_dir.exists():
    print(f"Error: Directory '{data_dir}' does not exist!")
    exit(1)

# Process all files in the data directory
try:
    files_found = False
    for file_path in data_dir.glob("*"):
        if file_path.is_file():  # Make sure it's a file, not a subdirectory
            files_found = True
            print(f"\nResults for {file_path.name}:")
            file_results = process_file(str(file_path))
            print(f"Token count: {file_results['tokens']}")
            print(f"Character count: {file_results['characters']}")
    
    if not files_found:
        print(f"No files found in directory '{data_dir}'")

except PermissionError:
    print(f"Error: Permission denied accessing directory '{data_dir}'")
    exit(1)