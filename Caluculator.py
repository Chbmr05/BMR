import os
class Receipt:
    def __init__(self):
        """Initializes the receipt with empty items."""
        self.items = []

    def add_item(self, name, price, quantity):
        """
        Adds an item to the receipt.
        :param name: Name of the item
        :param price: Price of the item
        :param quantity: Quantity of the item
        """
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def calculate_totals(self, tax_rate=0.09, discount_rate=0.1):
        """
        Calculates the subtotal, tax, discount, and final total.
        :param tax_rate: The tax rate (default is 7%)
        :param discount_rate: The discount rate (default is 10%)
        :return: A dictionary with subtotal, tax, discount, and final total
        """
        subtotal = sum(item['price'] * item['quantity'] for item in self.items)
        tax = subtotal * tax_rate
        discount = subtotal * discount_rate
        total = subtotal + tax - discount
        return {
            "subtotal": subtotal,
            "tax": tax,
            "discount": discount,
            "total": total
        }

    def generate_receipt(self):
        """Generates a receipt string."""
        receipt_lines = ["--- Receipt ---"]
        for item in self.items:
            receipt_lines.append(f"{item['name']} (x{item['quantity']}): ${item['price']:.2f} each")
        
        totals = self.calculate_totals()
        receipt_lines.append(f"\nSubtotal: ${totals['subtotal']:.2f}")
        receipt_lines.append(f"Tax: ${totals['tax']:.2f}")
        receipt_lines.append(f"Discount: -${totals['discount']:.2f}")
        receipt_lines.append(f"Total: ${totals['total']:.2f}")
        receipt_lines.append("--- Thank you! ---")

        return "\n".join(receipt_lines)

    def save_receipt(self, filename='receipt.txt'):
        """Saves the receipt to a text file."""
        receipt_content = self.generate_receipt()
        with open(filename, 'w') as file:
            file.write(receipt_content)
        print(f"Receipt saved as {filename}")
def main():
    receipt = Receipt()
    
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        receipt.add_item(name, price, quantity)

    # Calculate totals and generate receipt
    print("\nGenerating receipt...")
    print(receipt.generate_receipt())

    # Save receipt to a file
    save_option = input("Do you want to save the receipt? (yes/no): ")
    if save_option.lower() == 'yes':
        receipt.save_receipt()

if __name__ == "__main__":
    main()