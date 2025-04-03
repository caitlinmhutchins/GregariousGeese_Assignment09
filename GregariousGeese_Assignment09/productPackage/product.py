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
# product.py

class Product:
    """
    Represents a single product, its related manufacturer and brand, and the number of items sold.
    Builds a sentence summarizing the data.
    """
    def __init__(self, row):
        self.product_id = row[0]
        self.upc = row[1]
        self.description = row[2]
        self.manufacturer_id = row[3]
        self.brand_id = row[4]
        self.manufacturer = None
        self.brand = None
        self.items_sold = None

    def populate_details(self, db):
        """
        Fills in manufacturer, brand, and items sold using the provided Database object.
        """
        self.manufacturer = db.get_manufacturer_name(self.manufacturer_id)
        self.brand = db.get_brand_name(self.brand_id)
        self.items_sold = db.get_items_sold(self.product_id)

    def __str__(self):
        """
        Returns the final formatted output sentence.
        """
        return (f"The product '{self.description}' by manufacturer '{self.manufacturer}' "
                f"under the brand '{self.brand}' sold a total of {self.items_sold} units.")