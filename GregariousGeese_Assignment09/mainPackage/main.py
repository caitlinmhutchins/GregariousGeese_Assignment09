# File Name : GreagriousGeese_Assignment09
# Student Name: Caitlin Hutchins, Sharvari Patil, and Chrystie Cadet
# email: hutchicu@mail.uc.edu, patilsg@mail.uc.edu, and cadetce@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:  4/3/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Uses a SQL statement to pull data and create a statement

# Brief Description of what this module does: We used Github to collaboratively create commits and create a statemtn through 3 packages/modules
# Citations: ChatGPT

# Anything else that's relevant:
# main.py

import random
from databasePackage.database import Database
from productPackage.product import Product


def main():
    db = Database()
    products = db.get_products()
    if not products:
        print("No products found.")
        return

    selected_row = random.choice(products)
    product = Product(selected_row)
    product.populate_details(db)
    print(product)

if __name__ == "__main__":
    main()

