import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field (display)
expression = ""

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Function to calculate result
def equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Function to clear
def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Function to delete last character
def backspace():
    global expression
    expression = expression[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

frame = tk.Frame(root)
frame.pack()

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        action = lambda x=btn: press(x) if x != '=' else equal()
        tk.Button(row_frame, text=btn, font=("Arial", 14),
                  command=action, height=2, width=5).pack(side="left", expand=True, fill="both")

# Bottom buttons (Clear & Backspace)
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill="both")

tk.Button(bottom_frame, text="C", font=("Arial", 14), command=clear).pack(side="left", expand=True, fill="both")
tk.Button(bottom_frame, text="⌫", font=("Arial", 14), command=backspace).pack(side="left", expand=True, fill="both")

# Run app
root.mainloop()

