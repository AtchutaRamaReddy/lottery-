  Features
1.Input fields to specify the minimum and maximum range for the random number.
2.Input field to specify a lucky number.
3.Button to generate a random number within the specified range.
4.Display the generated random number.
5.Display a special message if the generated number matches the lucky number.
  Requirements
Python 3.x
Tkinter (usually included with Python installations)
  Installation
Clone the repository:


git clone https://github.com/your-username/random-number-generator.git
Navigate to the project directory:


cd random-number-generator
  Usage
Run the application:


python random_number_generator.py
.Enter the minimum and maximum values in the respective fields.

.Enter your lucky number in the designated field.

.Click the "Generate" button to generate a random number.

If the generated random number matches your lucky number, a message saying "You won the lottery!" will be displayed.

Code Overview
Functionality
generate_random_number():
Retrieves values from the input fields.
Generates a random number within the specified range.
Compares the generated number with the lucky number.
Updates the result label with the generated number and, if applicable, the lottery message.
GUI Layout
Uses Tkinter to create a simple GUI.
Grid layout is used to arrange labels, entry widgets, and buttons.
Example Code
Here is the main code for the application:

python

import tkinter as tk
import random

 Function to generate a random number within the specified range
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

 Create the main window
root = tk.Tk()
root.title("Random Number Generator")

 Create and place the labels, entries, and button
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

 Run the application
root.mainloop()
  License
This project is licensed under the MIT License - see the LICENSE file for details.

  Contributing
If you wish to contribute to this project, please fork the repository and submit a pull request.
