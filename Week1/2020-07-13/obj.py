class Product:
  # Define the __init__ method
  # Initialize the object 
    total_products_created = 0 
    def __init__(self, name, price, color, size):
        self.name = name
        self.price = price
        self.color = color
        self.size = size
        print(self.name + " created successfully! At a price of " + str(self.price) + " and color " + self.color + ", size " + self.size + ".")
        Product.total_products_created += 1
        print("We have a total of " + str(Product.total_products_created) + " avaliable")

# Initialize the first products
product1 = Product("Pillow Pal", 24.99, "Pink", "n/a")
print(product1.name)
# product2 = Product("Colored Pencils", 5.99)
# product2 = Product("Muji Pens", 6.99)
# product2 = Product("Markers", 6.99)
# product2 = Product("Rubber Ducky", 1.99)


