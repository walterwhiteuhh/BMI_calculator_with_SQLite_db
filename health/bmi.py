# Import modules

import sqlite3
import os.path

# Define class for users

class User:
    def __init__(self,name,height):
        self.name = name
        self.height = height

# Define class for BMI calculator & connection to SQLite database

class Bmirechner:
    def __init__(self):
        self.datastorage={}