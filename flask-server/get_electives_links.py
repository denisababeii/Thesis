import configparser
import pandas as pd

class Elective_Links:
    @staticmethod
    def get():
        parser = configparser.ConfigParser()
        parser.read("config.txt")
        file = parser.get("config", "courses")
        df = pd.read_excel(file)
        df = df[df["Type"] == "Optional"]
        return df[['Name', 'Link', 'Package']].values.tolist()