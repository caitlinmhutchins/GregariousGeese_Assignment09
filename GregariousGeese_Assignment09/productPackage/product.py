# File Name : GreagriousGeese_Assignment09
# Student Name: Caitlin Hutchins,
# email: hutchicu@mail.uc.edu,
# Assignment Number: Assignment 09
# Due Date:  4/3/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Uses a SQL statement to pull data and create a statement

# Brief Description of what this module does: We used Github to collaboratively create commits and create a statemtn through 3 packages/modules
# Citations: ChatGPT

# Anything else that's relevant:
# product.py


class Product:
    def __init__(self, row):
        self.product_id = row.ProductID
        self.description = row.Description
        self.manufacturer_id = row.ManufacturerID
        self.brand_id = row.BrandID
        self.manufacturer_name = ""
        self.brand_name = ""
        self.total_items_sold = 0

    def populate_details(self, db):
        self.manufacturer_name = db.get_manufacturer_name(self.manufacturer_id)
        self.brand_name = db.get_brand_name(self.brand_id)
        self.total_items_sold = db.get_items_sold(self.product_id)

    def __str__(self):
        return f"The product '{self.description}' is manufactured by {self.manufacturer_name}, branded as {self.brand_name}, and has sold {self.total_items_sold} items."

