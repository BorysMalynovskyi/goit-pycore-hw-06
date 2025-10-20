import sys
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama to automatically reset the style after each print() call
init(autoreset=True)

def display_directory_structure(directory_path: Path, prefix: str = ""):
    """
    Recursively traverses and visualizes the directory structure with colored output.
    
    Args:
        directory_path (Path): A Path object for the directory to visualize.
        prefix (str): A prefix for formatting the output, creating a tree-like effect.
    """
    paths_to_entries = sorted(list(directory_path.iterdir()), key=lambda path: (path.is_file(), path.name.lower()))

    entries_count = len(paths_to_entries)

    for index, path in enumerate(paths_to_entries):
        is_last = (index == entries_count - 1)
        
        if path.is_dir():
            print(f"{prefix}{Fore.BLUE}{Style.BRIGHT}{path.name}/")

            prefix_for_next = prefix + ("  " if is_last else " ")

            display_directory_structure(path, prefix_for_next)
        else:
            print(f"{prefix}{Fore.GREEN}{path.name}")

def main():
    """
    Main function to handle commandline arguments and start the visualization.
    """
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Error: Provide absolute path to the directory.")
        sys.exit(1)

    directory_path_string = sys.argv[1]
    directory_path = Path(directory_path_string)

    if not directory_path.exists():
        print(f"{Fore.RED}Error: The specified path '{directory_path_string}' does not exist.")
        sys.exit(1)

    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: The specified path '{directory_path_string}' is not a directory.")
        sys.exit(1)

    display_directory_structure(directory_path)

main()