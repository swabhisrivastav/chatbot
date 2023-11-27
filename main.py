import json
import tkinter as tk
from difflib import get_close_matches
from chatbot_gui import ChatbotGUI

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:

    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.4)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def handle_user_input():
    global current_user_input  # Add this line
    user_input = gui.entry.get()
    gui.entry.delete(0, 'end')  # Clear the entry field

    if user_input.lower() == 'quit':
        gui.root.destroy()
    else:
        current_user_input = user_input  # Add this line
        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            gui.chat_history.insert(tk.END, f'You: {user_input}\nBot: {answer}\n\n')
        else:
            gui.chat_history.insert(tk.END, f'You: {user_input}\nBot: I don\'t know the answer. Can you teach me?\n\n')

def teach_bot():
    global current_user_input  # Add this line
    new_answer = gui.entry.get()
    gui.entry.delete(0, 'end')  # Clear the entry field

    if new_answer.lower() != 'skip':
        knowledge_base["questions"].append({"question": current_user_input, "answer": new_answer})
        save_knowledge_base('knowledge_base.json', knowledge_base)
        gui.chat_history.insert(tk.END, f'Bot: Thank you! I learned a new response!\n\n')

# Load knowledge base
knowledge_base = load_knowledge_base('knowledge_base.json')

# Create and run the GUI
gui = ChatbotGUI(handle_user_input, teach_bot)
gui.run()
