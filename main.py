import json
from logging import shutdown
from scripts.loadExpenses import loadExpenses
from scripts.startup import startup

# Define variables
filePath = "expenses.json"
expenseList = []



# read file and load data into expense list
expenses = loadExpenses() 

# define startup function
def main():
    try:
        startup()
    finally:
        shutdown()

if __name__ == "__main__":
    main()
