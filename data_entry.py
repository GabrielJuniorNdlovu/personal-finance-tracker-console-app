import pandas as pd
import csv
from datetime import datetime

class CSV:
    CS_FILE = "finance_data.csv"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CS_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount","category", "Description"])