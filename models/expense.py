class Expense:
    """A Class that represents a specific expense."""

    amount: int
    category: str
    description: str

    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description