import json
from typing import List

from models.expense import Expense


def loadExpenses(filepath: str) -> List[Expense]:
    """
    Loads expenses from a JSON file.
    """

    with open(filepath, "r") as file:
        data = file.read()
        return json.loads(data)