def read_file(file_path: str) -> str:
    """Read the content of a file and return it as a string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()
