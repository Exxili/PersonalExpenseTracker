import json
from typing import List
from models.expense import Expense
from scripts.checkFileExists import checkFileExists


def shutdown (filePath: str, expenses: List[Expense]):
    """ shutdown the Personal Expense Tracker"""
    """ before shutdown, save the expense list """

    # Log to the console
    print("Saving expenses to file...")

    with open(filePath, "r") as file:
        file.write(json.dumps(expenses))

