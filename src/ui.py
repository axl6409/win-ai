import tkinter as tk
from customtkinter import CTk, CTkButton, CTkEntry
import src.api as api

def launch_main_ui(user_data, api_key, has_gpt4):
    root = CTk()
    root.geometry("400x300")
    root.title("My ChatGPT App")

    sidebar = tk.Frame(root, width=100, bg='#333')
    sidebar.pack(side="left", fill="y")

    chat_area = tk.Frame(root, bg='#fff')
    chat_area.pack(side="right", fill="both", expand=True)

    email_label = tk.Label(sidebar, text=user_data['email'], bg='#333', fg='#fff')
    email_label.pack(pady=10)

    gpt_list = api.get_gpt_list(api_key)
    for gpt in gpt_list:
        btn = CTkButton(sidebar, text=gpt["name"], command=lambda g=gpt: open_chat(g, api_key, has_gpt4))
        btn.pack(pady=5)

    root.mainloop()

def open_chat(gpt, api_key, has_gpt4):
    chat_window = CTk()
    chat_window.geometry("500x600")
    chat_window.title(f"Chat with {gpt['name']}")

    chat_frame = tk.Frame(chat_window, bg='#fff')
    chat_frame.pack(fill="both", expand=True)

    input_frame = tk.Frame(chat_window, bg='#eee')
    input_frame.pack(side="bottom", fill="x")

    input_field = CTkEntry(input_frame)
    input_field.pack(side="left", fill="x", expand=True, pady=10, padx=10)

    send_button = CTkButton(input_frame, text="Send", command=lambda: send_message(input_field.get(), chat_frame, api_key, has_gpt4))
    send_button.pack(side="right", pady=10, padx=10)

    chat_window.mainloop()

def send_message(message, chat_frame, api_key, has_gpt4):
    if message.strip() == "":
        return

    user_message = tk.Label(chat_frame, text=f"You: {message}", bg='#fff', anchor='w')
    user_message.pack(fill='x', padx=10, pady=5)

    response = api.send_message_to_gpt(message, api_key, has_gpt4)

    if response:
        gpt_message = tk.Label(chat_frame, text=f"GPT: {response}", bg='#eee', anchor='w')
        gpt_message.pack(fill='x', padx=10, pady=5)
        