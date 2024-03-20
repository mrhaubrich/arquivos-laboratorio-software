def read_file(file_path: str) -> str:
    return read_csv(file_path)
    
def read_csv(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return file.read().split('\n')