from research_agent import ResearchAgent
from chatbot_agent import ChatBotAgent

def main():
    researcher = ResearchAgent("cafe_data.json")
    chatbot = ChatBotAgent(researcher)
    chatbot.run()

if __name__ == "__main__":
    main()
