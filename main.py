import pandas as pd
import csv
from datetime import datetime

class CSV:
    CS_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CS_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CS_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CS_FILE, "a", newline="") as csfile:
            writer = csv.DictWriter(csfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

CSV.initialize_csv()
CSV.add_entry("20-07-2024", 125.65, "Income", "Salary")