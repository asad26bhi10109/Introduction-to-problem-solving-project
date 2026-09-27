# Introduction-to-problem-solving-project
# VIT Bhopal Canteen Billing System

A simple command-line billing program for the VIT Bhopal canteen. Students can choose items from the menu, enter quantities, and see the total bill for their order.

## Features

- Displays the canteen menu and item prices
- Adds multiple items to one order
- Calculates each item's cost and the order total
- Checks for invalid menu choices and quantities
- Prints the student's name and final bill

## Menu

| Option | Item | Price |
| --- | --- | ---: |
| 1 | Masala Dosa | Rs. 120 |
| 2 | Veg sandwich | Rs. 60 |
| 3 | Coffee | Rs. 30 |
| 4 | Finish order | — |

## Requirements

- Python 3
- No additional packages are required

## Run the program

1. Save the Python code as `projectcode.py`.
2. Open a terminal in the folder containing the file.
3. Run:

   ```bash
   projectcode.py
   ```

   On some systems, use `python3 projectcode.py` instead.

## Example

```text
Welcome to the VIT Bhopal Canteen
Enter your name: Asha

--- Canteen Menu ---
1. Masala Dosa - Rs. 120
2. Veg sandwich - Rs. 60
3. Coffee - Rs. 30
4. Finish order
Choose an option: 1
Enter quantity: 2
2 Masala Dosa added. Cost: Rs. 240

Choose an option: 4

--- Bill ---
Student name: Asha
Total amount: Rs. 240
Thank you for visiting the canteen!
```

## Project structure

```text
.
└── canteen_billing.py
```

The program handles one order at a time. Order details are kept only while the program is running.
