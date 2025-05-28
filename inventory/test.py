from product import Product

if __name__ == "__main__":
   products = [] 

   natraj_pencil = Product(1, "Natraj_pencil", 5, 100)
   print(f"The current quanity before sale is:", natraj_pencil.quantity)
   natraj_pencil.sale(10)
   print(f"The current quantity after sale is:", natraj_pencil.quantity)

   print(f"The current quantity before purchase is:", natraj_pencil.quantity)
   natraj_pencil.purchase(1000)
   print(f"The current quantity after purchase is:", natraj_pencil.quantity) 

   products.append(natraj_pencil)

   apsara_pencil = Product(2, "Apsara_pencil", 10, 1000)
   print(f"The current quantity before sale is:", apsara_pencil.quantity)
   apsara_pencil.sale(100)
   print(f"The current qauntity after sale is:", apsara_pencil.quantity)

   print(f"The current quantity before purchase is:", apsara_pencil.quantity)
   apsara_pencil.purchase(30)
   print(f"The current quantity after purchase is:" , apsara_pencil.quantity)

   products.append(apsara_pencil)

   for product in products:
      print(product.name)
      print(product.quantity)