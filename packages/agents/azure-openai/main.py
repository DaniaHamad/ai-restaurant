from azure_openai.restaurant_agent import RestaurantAgent
from dotenv import load_dotenv
import os

load_dotenv()
def main():
    agent = RestaurantAgent()

    print("CLI agent chat. Ctrl+C to exit.\n")

    while True:
        try:
            text = input("You: ")
            agent.run_agent(text)
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()
