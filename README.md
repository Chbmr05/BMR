🧾 Python Receipt Generator

A simple, interactive Command Line Interface (CLI) tool built in Python to generate, calculate, and save transaction receipts.

🌟 Features

1. Interactive Input: Add multiple items with custom names, prices, and quantities.

2. Automatic Calculations: * Calculates Subtotal based on quantity.

    i.Applies a 9% Tax Rate by default.

    ii. Applies a 10% Discount automatically.

3.Formatted Output: Generates a clean, readable receipt string.

4.File Export: Option to save the final receipt as a .txt file for record-keeping.

📊 How it Works

The project uses a Receipt class to manage items and logic:

1. add_item(): Stores items in a list of dictionaries.

2. calculate_totals(): Uses the following logic for the final price:
   
        $$Total = Subtotal + Tax - Discount$$

3.save_receipt(): Uses Python's os and file handling to write the output to your local drive.

### 🛒 Itemized Breakdown
| Item Name | Quantity | Unit Price | Total |
| :--- | :---: | :---: | :--- |
| Apple | 3 | $1.00 | $3.00 |
| Bread | 1 | $2.50 | $2.50 |

### 💰 Final Totals
| Description | Amount |
| :--- | :--- |
| **Subtotal** | $5.50 |
| Tax (9%) | +$0.50 |
| Discount (10%) | -$0.55 |
| **Grand Total** | **$5.45** |
