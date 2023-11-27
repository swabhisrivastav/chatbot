import tkinter as tk
from tkinter import Text, Entry, Button

class ChatbotGUI:
    def __init__(self, handle_user_input, teach_bot):
        self.root = tk.Tk()
        self.root.title("Chatbot")

        # Chat history
        self.chat_history = Text(self.root, wrap="word", width=40, height=10)
        self.chat_history.pack(padx=10, pady=10)

        # Entry field
        self.entry = Entry(self.root, width=40)
        self.entry.pack(pady=10)

        # Buttons
        send_button = Button(self.root, text="Send", command=handle_user_input)
        send_button.pack(side=tk.LEFT, padx=5)
        teach_button = Button(self.root, text="Teach Bot", command=teach_bot)
        teach_button.pack(side=tk.LEFT, padx=5)

        # Bind Enter key to handle_user_input function
        self.root.bind('<Return>', lambda event: handle_user_input())

    def run(self):
        self.root.mainloop()
