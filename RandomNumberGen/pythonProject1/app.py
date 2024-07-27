import tkinter as tk
import random

# Function to generate a random number within the specified range
def generate_random_number():
    try:
        min_value = int(entry_min.get())
        max_value = int(entry_max.get())
        lucky_number = int(entry_lucky.get())
        if min_value > max_value:
            result_label.config(text="Min value must be less than or equal to Max value")
        else:
            random_number = random.randint(min_value, max_value)
            if random_number == lucky_number:
                result_label.config(text=f"Random Number: {random_number} - You won the lottery!")
            else:
                result_label.config(text=f"Random Number: {random_number}")
    except ValueError:
        result_label.config(text="Please enter valid integers")

# Create the main window
root = tk.Tk()
root.title("Random Number Generator")

# Create and place the labels, entries, and button
label_min = tk.Label(root, text="Min Value:")
label_min.grid(row=0, column=0, padx=10, pady=10)

entry_min = tk.Entry(root)
entry_min.grid(row=0, column=1, padx=10, pady=10)

label_max = tk.Label(root, text="Max Value:")
label_max.grid(row=1, column=0, padx=10, pady=10)

entry_max = tk.Entry(root)
entry_max.grid(row=1, column=1, padx=10, pady=10)

label_lucky = tk.Label(root, text="Lucky Number:")
label_lucky.grid(row=2, column=0, padx=10, pady=10)

entry_lucky = tk.Entry(root)
entry_lucky.grid(row=2, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate", command=generate_random_number)
generate_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()

