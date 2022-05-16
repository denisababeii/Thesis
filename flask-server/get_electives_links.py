import pandas as pd

class Elective_Links:
    @staticmethod
    def get(database):
        df = database.get_courses()
        df = df[df["Type"] == "Optional"]
        return df[['Name', 'Link', 'Package']].values.tolist()