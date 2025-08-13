import random
import string
from tkinter import *
from tkinter import ttk, messagebox

class PasswordGenerator:
    def __init__(self, root):  
        self.root = root
        self.root.title("Ultimate Password Generator")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f0f0')
        
        self.create_widgets()
        
    def create_widgets(self):
       
        main_frame = Frame(self.root, bg='#f0f0f0')
        main_frame.pack(pady=20)
        
       
        Label(main_frame, text="Secure Password Generator", font=('Helvetica', 18, 'bold'), bg='#f0f0f0').pack(pady=10)
        
        
        length_frame = Frame(main_frame, bg='#f0f0f0')
        length_frame.pack(pady=10)
        Label(length_frame, text="Password Length:", bg='#f0f0f0').pack(side=LEFT)
        self.length_var = IntVar(value=16)
        Spinbox(length_frame, from_=8, to=64, textvariable=self.length_var, width=5).pack(side=LEFT, padx=10)
        
        
        options_frame = Frame(main_frame, bg='#f0f0f0')
        options_frame.pack(pady=10)
        
        self.lower_var = BooleanVar(value=True)
        Checkbutton(options_frame, text="Lowercase (a-z)", variable=self.lower_var, bg='#f0f0f0').pack(anchor=W)
        
        self.upper_var = BooleanVar(value=True)
        Checkbutton(options_frame, text="Uppercase (A-Z)", variable=self.upper_var, bg='#f0f0f0').pack(anchor=W)
        
        self.digit_var = BooleanVar(value=True)
        Checkbutton(options_frame, text="Digits (0-9)", variable=self.digit_var, bg='#f0f0f0').pack(anchor=W)
        
        self.special_var = BooleanVar(value=True)
        Checkbutton(options_frame, text="Special Characters", variable=self.special_var, bg='#f0f0f0').pack(anchor=W)
        
        self.extended_special_var = BooleanVar()
        Checkbutton(options_frame, text="Include Rare Symbols", variable=self.extended_special_var, bg='#f0f0f0').pack(anchor=W)
        
        
        Button(main_frame, text="Generate Password", command=self.generate_password, bg='#4CAF50', fg='white').pack(pady=20)
        
        self.password_var = StringVar()
        password_entry = Entry(main_frame, textvariable=self.password_var, font=('Courier', 14), width=30, justify=CENTER, bd=2, relief="sunken")
        password_entry.pack(pady=10)
        
        Button(main_frame, text="Copy to Clipboard", command=self.copy_to_clipboard, bg='#2196F3', fg='white').pack(pady=5)
    
    def get_character_set(self):
        """Build character set based on user selections"""
        chars = ''
        
        if self.lower_var.get():
            chars += string.ascii_lowercase
        if self.upper_var.get():
            chars += string.ascii_uppercase
        if self.digit_var.get():
            chars += string.digits
        if self.special_var.get():
            chars += '!@#$%^&*()-_=+[]{}|;:,.<>?'
        if self.extended_special_var.get():
            chars += '€£¥©®™✓§¶•'

        return chars

    def generate_password(self):
        length = self.length_var.get()
        charset = self.get_character_set()

        if not charset:
            messagebox.showwarning("No Characters Selected", "Please select at least one character type.")
            return

        password = ''.join(random.choice(charset) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("No Password", "Generate a password first.")

if __name__ == "__main__":  
    root = Tk()
    app = PasswordGenerator(root)
    root.mainloop()