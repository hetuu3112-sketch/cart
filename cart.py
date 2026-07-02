def main():
    cart = []
    x = print(" Press 1 To Add Items,\n Press 2 To Print Items In Cart,\n Press 3 To Exit,\npress 4 To Remove.\n ")
    
    while True :
        user_input = cart_items()
        if user_input == 1:
            items(cart)
        elif user_input == 2 :
            if item == []:
                print("Cart is emptry,add items.")
            else:
                print(cart)
        elif user_input == 4:
            item_pop(cart)
            print(cart)
        elif user_input != 1 or 2 or 3 or 4:
            print("Invlid Choice,") 
        else:
            print("Program Ends Here.")
            break


def items(cart):
        
    value = str(input("Enter Here:"))
    item.append(value)
    return cart


def cart_items():
    x = int(input("press(1,2,3,4):"))
    return x
    if x != 1 or 2 or 3 or 4:
        print("Invlid Choice,")


def item_pop(cart):
    pop = str(input("Enter Item To Remove:"))
        if pop in cart:
            cart.remove(pop)
            print("Removed !:",pop)
        else:
            print("No Such Item.")
    
    
main()