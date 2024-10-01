import os
import sys

def print_help():
    print("Usage: python script.py -d <directory> -e <extensions>")
    print("Options:")
    print("  -d <directory>     Directory to start searching from")
    print("  -e <extensions>    File extensions to include, comma-separated (e.g., txt,py,yml)")

def get_args():
    directory = None
    extensions = None
    
    # Basic argument parsing
    args = sys.argv[1:]
    if "-d" in args:
        try:
            directory = args[args.index("-d") + 1]
        except IndexError:
            print("Error: Missing argument for -d")
            sys.exit(1)
    
    if "-e" in args:
        try:
            extensions = args[args.index("-e") + 1].split(',')
        except IndexError:
            print("Error: Missing argument for -e")
            sys.exit(1)
    
    if not directory or not extensions:
        print_help()
        sys.exit(1)
    
    return directory, extensions

def scan_directory(directory, extensions):
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                results.append(relative_path)
    return results

def main():
    # Get the directory and extensions from command-line arguments
    directory, extensions = get_args()
    
    # Scan directory for files with the specified extensions
    files = scan_directory(directory, extensions)
    
    # Display the files and their content
    for file in files:
        print(f"----- {file} ----------------")
        try:
            with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
                print(f.read())
        except Exception as e:
            print(f"Could not read {file}: {e}")
        print("--------------------------------------------------")

if __name__ == "__main__":
    main()

