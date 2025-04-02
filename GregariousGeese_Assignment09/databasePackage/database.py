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
# database.py


import pyodbc
import random

class Database:
    """
    Stores database and executes SQL queries
    """
    def __init__(self):
        """
        Initializes parameters
        """
        self.conn = None
        self.connection_string = (
            'Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=GroceryStoreSimulator;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;'
        )

    def connect(self):
        if not self.conn:
            self.conn = pyodbc.connect(self.connection_string)

    def get_products(self):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct")
        return cursor.fetchall()

    def get_manufacturer_name(self, manufacturer_id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = ?", (manufacturer_id,))
        result = cursor.fetchone()
        return result[0] if result else "Unknown"

    def get_brand_name(self, brand_id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("SELECT Brand FROM tBrand WHERE BrandID = ?", (brand_id,))
        result = cursor.fetchone()
        return result[0] if result else "Unknown"

    def get_items_sold(self, product_id):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
            FROM dbo.tTransactionDetail 
            INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID 
            WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = ?)
        """, (product_id,))
        result = cursor.fetchone()
        return result[0] if result and result[0] else 0