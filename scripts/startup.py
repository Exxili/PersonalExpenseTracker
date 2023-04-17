from scripts.checkFileExists import checkFileExists


def startup(filePath: str):
    """ Startup the Personal Expense Tracker"""

    # Log to the console
    print("Starting up Personal Expense Tracker...")

    # Check if file exists
    # If file does not exist, create it
    if not checkFileExists(filePath):
        with open(filePath, "w") as file:
            file.write("[]")