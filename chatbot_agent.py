import re

class ChatBotAgent:
    def __init__(self, researcher):
        self.researcher = researcher

    def greet(self):
        print("👋 Welcome to SmartCafe Assistant!")
        print("Ask me anything about the café. Type 'exit' to quit.\n")

    def run(self):
        self.greet()
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("☕ Goodbye! Have a great day.")
                break
            self.handle_question(user_input)

    def handle_question(self, question):
        # Ingredients
        match = re.search(r"(?i)what(?:'s| is) in (?:a|an|the)? ?(?P<item>[\w\s]+)\??", question)
        if match:
            item = match.group("item").strip()
            ingredients = self.researcher.get_ingredients(item)
            if ingredients:
                print(f"🧾 The ingredients in {item.title()} are: {', '.join(ingredients)}.")
            else:
                print(f"❌ Sorry, I couldn't find information for {item}.")
            return

        # Calories
        match = re.search(r"(?i)how many calories in (?P<item>[\w\s]+)\??", question)
        if match:
            item = match.group("item").strip()
            calories = self.researcher.get_calories(item)
            if calories:
                print(f"🔥 {item.title()} has {calories} calories.")
            else:
                print(f"❌ Sorry, I don't have calorie info for {item}.")
            return

        # Hours
        match = re.search(r"(?i)when (?:are you|do you open) on (?P<day>\w+)\??", question)
        if match:
            day = match.group("day").capitalize()
            hours = self.researcher.get_opening_hours(day)
            if hours:
                print(f"🕒 We're open on {day}s from {hours}.")
            else:
                print(f"❌ Sorry, I don't have our hours for {day}.")
            return



        # Drinks
        match = re.search(r"(?i)what drinks (?:do you have|are available)\??", question)
        if match:
            drinks = self.researcher.get_drinks()
            print(f"🥤 We offer: {', '.join(drinks)}.")
            return

        # Sugar
        match = re.search(r"(?i)how much sugar (is in|in) (?P<item>[\w\s]+)\??", question)
        if match:
            item = match.group("item").strip()
            sugar = self.researcher.get_sugar(item)
            if sugar is not None:
                print(f"🍬 {item.title()} contains {sugar}g of sugar.")
            else:
                print(f"❌ Sorry, I don't have sugar info for {item}.")
            return

        # Price
        match = re.search(r"(?i)how much (is|does) (a|an|the)? ?(?P<item>[\w\s]+) (cost|price)\??", question)
        if match:
            item = match.group("item").strip()
            price = self.researcher.get_price(item)
            if price is not None:
                print(f"💵 {item.title()} costs ${price:.2f}.")
            else:
                print(f"❌ Sorry, I couldn't find a price for {item}.")
            return
        
        print("🤔 Sorry, I didn't understand that. Try asking about ingredients, hours, or drinks.")