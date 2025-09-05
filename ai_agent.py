import time
import random

LOG_FILE = "workflow.log"

def process_request(user_input):
    responses = [
        f"Analysed '{user_input}' and generated insights.",
        f"Summarised '{user_input}' into a concise report.",
        f"Processed '{user_input}' with advanced workflows."
    ]
    return random.choice(responses)

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.strftime('%H:%M:%S')} - {message}\n")

if __name__ == "__main__":
    print("AI Agent started. Type something to process...")
    while True:
        user_input = input("Enter data: ")
        result = process_request(user_input)
        log(f"INPUT: {user_input} | OUTPUT: {result}")
        print(f"Agent says: {result}")
