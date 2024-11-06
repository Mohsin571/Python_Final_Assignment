# Product class for handling product details
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: ${self.price:.2f}, Stock: {self.stock_quantity}"

    def restock(self, amount):
        self.stock_quantity += amount

    def reduce_stock(self, amount):
        if self.stock_quantity >= amount:
            self.stock_quantity -= amount
        else:
            print(f"Not enough stock for {self.name}. Only {self.stock_quantity} left.")

class InventoryManagementSystem:
    def __init__(self):
        self.products = {}
        self.users = {"admin": {"password": "admin123", "role": "admin"}, "user": {"password": "user123", "role": "user"}}
        self.logged_in_user = None

    # Authentication System
    def login(self):
        print("===== Login =====")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in self.users and self.users[username]['password'] == password:
            self.logged_in_user = username
            print(f"Logged in as {username} with role {self.users[username]['role']}")
        else:
            print("Invalid credentials. Please try again.")

    def logout(self):
        self.logged_in_user = None
        print("Logged out successfully.")

    # Role Check
    def is_admin(self):
        if self.logged_in_user:
            return self.users[self.logged_in_user]["role"] == "admin"
        return False

    # Product Management Methods
    def add_product(self):
        if not self.is_admin():
            print("Only admins can add products.")
            return
        
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        price = float(input("Enter product price: "))
        stock_quantity = int(input("Enter stock quantity: "))
        
        product = Product(product_id, name, category, price, stock_quantity)
        self.products[product_id] = product
        print(f"Product {name} added successfully.")

    def edit_product(self):
        if not self.is_admin():
            print("Only admins can edit products.")
            return
        
        product_id = input("Enter product ID to edit: ")
        if product_id in self.products:
            name = input("Enter new name: ")
            category = input("Enter new category: ")
            price = float(input("Enter new price: "))
            stock_quantity = int(input("Enter new stock quantity: "))

            product = self.products[product_id]
            product.name = name
            product.category = category
            product.price = price
            product.stock_quantity = stock_quantity
            print(f"Product {name} updated successfully.")
        else:
            print("Product not found.")

    def delete_product(self):
        if not self.is_admin():
            print("Only admins can delete products.")
            return
        
        product_id = input("Enter product ID to delete: ")
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    # Inventory Operations
    def view_products(self):
        if not self.products:
            print("No products available.")
            return
        
        for product in self.products.values():
            print(product)

    def search_product(self):
        search_name = input("Enter product name to search: ").lower()
        found = False
        for product in self.products.values():
            if search_name in product.name.lower():
                print(product)
                found = True
        if not found:
            print("No products found with that name.")

    def check_stock_levels(self):
        low_stock_threshold = 10  # You can modify this threshold
        for product in self.products.values():
            if product.stock_quantity < low_stock_threshold:
                print(f"Warning: Low stock for {product.name}. Only {product.stock_quantity} left.")

    def adjust_stock(self):
        product_id = input("Enter product ID to adjust stock: ")
        if product_id in self.products:
            action = input("Do you want to restock or reduce stock? (restock/reduce): ").lower()
            amount = int(input("Enter the quantity: "))

            if action == "restock":
                self.products[product_id].restock(amount)
            elif action == "reduce":
                self.products[product_id].reduce_stock(amount)
            else:
                print("Invalid action.")
        else:
            print("Product not found.")

    # Main Menu
    def menu(self):
        while True:
            if not self.logged_in_user:
                self.login()
            else:
                print("\n===== Main Menu =====")
                print("1. View Products")
                if self.is_admin():
                    print("2. Add Product")
                    print("3. Edit Product")
                    print("4. Delete Product")
                    print("5. Adjust Stock")
                    print("6. Check Stock Levels")
                print("7. Search Product")
                print("8. Logout")
                print("9. Exit")
                
                choice = input("Enter your choice: ")
                
                if choice == "1":
                    self.view_products()
                elif choice == "2" and self.is_admin():
                    self.add_product()
                elif choice == "3" and self.is_admin():
                    self.edit_product()
                elif choice == "4" and self.is_admin():
                    self.delete_product()
                elif choice == "5" and self.is_admin():
                    self.adjust_stock()
                elif choice == "6" and self.is_admin():
                    self.check_stock_levels()
                elif choice == "7":
                    self.search_product()
                elif choice == "8":
                    self.logout()
                elif choice == "9":
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid choice. Try again.")

# Initialize and run the system
ims = InventoryManagementSystem()
ims.menu()
