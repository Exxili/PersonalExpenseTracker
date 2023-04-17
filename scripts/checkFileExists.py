from os.path import exists

def checkFileExists(filePAth: str) -> bool:
    """
    Checks if a file exists.
    """
    return exists(filePAth)