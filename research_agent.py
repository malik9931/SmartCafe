import json

class ResearchAgent:
    def __init__(self, data_file):
        self.data = self.load_data(data_file)

    def load_data(self, filepath):
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")
            return {}

    def get_ingredients(self, item_name):
        item = self.data.get("menu", {}).get(item_name)
        return item.get("ingredients") if item else None

    def get_calories(self, item_name):
        item = self.data.get("menu", {}).get(item_name)
        return item.get("nutrition", {}).get("calories") if item else None

    def get_sugar(self, item_name):
        item = self.data.get("menu", {}).get(item_name)
        return item.get("nutrition", {}).get("sugar_g") if item else None

    def get_price(self, item_name):
        item = self.data.get("menu", {}).get(item_name)
        return item.get("price_usd") if item else None

    def get_opening_hours(self, day):
        return self.data.get("opening_hours", {}).get(day)


    def get_drinks(self):
        return self.data.get("drinks", [])
