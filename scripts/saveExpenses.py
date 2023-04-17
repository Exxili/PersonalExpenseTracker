import json
from typing import List
from models.expense import Expense


def saveExpenses(expenses: List[Expense]) -> None:
    """
    Saves expenses to a JSON file.
    """
    with open("expenses.json", "w") as file:
        file.write(json.dumps(expenses))