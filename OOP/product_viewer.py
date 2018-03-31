from products import Product

def list_products(my_products: tuple):
    '''display list of products'''
    print("PRODUCTS")
    for counter, product in enumerate(my_products):
        print("{:d}. {:s}\n".format(counter + 1, product.name))
        
def show_product_info(product_obj: Product):
    '''disply a product's info'''
    print("PRODUCT DATA")
    print("Name:                    {:s}".format(product_obj.name))
    print("Price:                   ${:,.2f}".format(product_obj.price))
    print("Discount Percent:        {:d}%".format(product_obj.discountPercent))
    print("Discount Amount:         {:.2f}".format(product_obj.getDiscountAmount()))
    print("Discount Price:          {:.2f}".format(product_obj.getDiscountPrice()))
    print()
    
def main():
    print("The Product Viewer Program")
    print()
    
    # a tuple of Product objects
    products = (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
                Product('National Hardware 3/4" Wire Nails', 5.06, 0),
                Product("Economy Duct Tape, 60 Yds, Silver", 7.24, 0))
                
    list_products(products)
    while True:
        number = int(input("Enter product number: "))
        print()
        
        selected_product = products[number-1]
        show_product_info(selected_product)
        
        choice = input("View another product? (y/n): ")
        print()
        if choice.lower() != "y":
            print("Bye!")
            break
        
        
if __name__ == '__main__':
    main()
        
    
    