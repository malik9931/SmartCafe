SmartCafe Assistant - Console-Based Café Chatbot

===============================
📌 Overview:
-------------------------------
SmartCafe Assistant is a console-based program that simulates a simple in-store assistant for a coffee shop. It answers customer questions like:
- “What’s in a Mocha?”
- “How many calories in Hot Chocolate?”
- “What drinks do you have?”
- “When are you open on Friday?”
- “How much is a Chai Latte price?”

The assistant uses a local JSON file as its knowledge base and is implemented using Object-Oriented Programming (OOP) in Python.

===============================
🧱 Program Structure:
-------------------------------

The system is divided into the following components:

1. `cafe_data.json` – the knowledge base that contains:
   - Menu items and their ingredients
   - Nutrition info (calories, sugar)
   - Prices
   - Opening hours
   - Available drinks list

2. `ResearchAgent` class:
   - Responsible for loading and querying data from the JSON file.

3. `ChatBotAgent` class:
   - Interacts with the user.
   - Uses regex to identify question intent.
   - Requests data from `ResearchAgent`.
   - Formats and displays the answer.

4. `main.py`:
   - Entry point that creates the agents and starts the chat loop.

===============================
📦 Class & Method Responsibilities:
-------------------------------

### Class: ResearchAgent
- `__init__(data_file)`: Loads the JSON file into memory.
- `get_ingredients(item)`: Returns a list of ingredients for a menu item.
- `get_calories(item)`: Returns calorie count for a menu item.
- `get_sugar(item)`: Returns sugar content (in grams).
- `get_price(item)`: Returns the price of a menu item in USD.
- `get_opening_hours(day)`: Returns opening hours for a given day.
- `get_drinks()`: Returns the list of all available drinks.

### Class: ChatBotAgent
- `__init__(researcher)`: Accepts a ResearchAgent instance.
- `greet()`: Displays the welcome message.
- `run()`: Main loop to handle user input.
- `handle_question(question)`: Uses regex to detect intent and call the corresponding method from ResearchAgent.

===============================
🔍 How Regex is Used:
-------------------------------

The assistant uses Python’s `re` module to identify user intent from natural-language-style questions. Each supported question type has a specific pattern.

Example patterns:

1. **Ingredients**:
   Pattern: `(?i)what(?:'s| is) in (?:a|an|the)? ?(?P<item>[\w\s]+)\??`  
   Detects questions like “What’s in a Mocha?”

2. **Calories**:
   Pattern: `(?i)how many calories in (?P<item>[\w\s]+)\??`  
   Detects “How many calories in Hot Chocolate?”

3. **Sugar**:
   Pattern: `(?i)how much sugar (is in|in) (?P<item>[\w\s]+)\??`  
   Detects “How much sugar in Latte?”

4. **Price**:
   Pattern: `(?i)how much (is|does) (a|an|the)? ?(?P<item>[\w\s]+) (cost|price)\??`  
   Detects “How much does a Mocha cost?”

5. **Opening hours**:
   Pattern: `(?i)when (?:are you|do you open) on (?P<day>\w+)\??`  
   Detects “When do you open on Friday?”

6. **Available drinks**:
   Pattern: `(?i)what drinks (do you have|are available)\??`  
   Detects “What drinks do you have?”

===============================
✅ How to Run:
-------------------------------
1. Make sure all the files are in the same folder:
   - `main.py`
   - `research_agent.py`
   - `chatbot_agent.py`
   - `cafe_data.json`
   - `README.txt`

2. Run the assistant using:
   ```bash
   python main.py

3. Ask your question. Type exit or quit to end the chat.