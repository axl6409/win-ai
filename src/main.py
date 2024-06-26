import tkinter as tk
from customtkinter import CTk, CTkButton, CTkEntry
import src.auth as auth
import src.ui as ui

def main():
    root = CTk()
    root.geometry("300x400")
    root.title("Login to OpenAI")

    email_label = tk.Label(root, text="Email:")
    email_label.pack(pady=5)
    email_entry = CTkEntry(root)
    email_entry.pack(pady=5)

    password_label = tk.Label(root, text="Password:")
    password_label.pack(pady=5)
    password_entry = CTkEntry(root, show='*')
    password_entry.pack(pady=5)

    api_key_label = tk.Label(root, text="API Key:")
    api_key_label.pack(pady=5)
    api_key_entry = CTkEntry(root)
    api_key_entry.pack(pady=5)

    error_label = tk.Label(root, text="", fg="red")
    error_label.pack(pady=5)

    def login():
        email = email_entry.get()
        password = password_entry.get()
        api_key = api_key_entry.get()
        user_data, has_gpt4 = auth.authenticate(email, password, api_key)
        if user_data:
            root.destroy()
            ui.launch_main_ui(user_data, api_key, has_gpt4)
        else:
            error_label.config(text="Login failed. Please check your credentials and API key.")

    login_button = CTkButton(root, text="Login", command=login)
    login_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
