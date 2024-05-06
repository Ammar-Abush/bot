import sys
print(sys.path)
#sys.path.append('../')


from ..manager.chat_manager import ChatManager
from dotenv import load_dotenv, find_dotenv

def initialize():
    chat_manager = ChatManager()
    return chat_manager

def Prompt(prompt, chat_manager):
    
    user_input = prompt
    answer = chat_manager.chain({"question": user_input.lower()})['answer']
    return answer

'''if __name__ == "__main__":
    if not load_dotenv(find_dotenv()):
        print("Failed to load .env file.")
        sys.exit(1)
    print(Prompt("hi"))'''
