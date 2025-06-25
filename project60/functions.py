# متجر العوجان الإلكتروني

cart = {}  # القاموس الذي يحتوي على العناصر التي يضيفها المستخدم إلى سلة الشراء

# الدالة الرئيسية التي تبدأ تشغيل المتجر وتعرض الخيارات للمستخدم
def main(items):
    print("Welcome to Alawjan Store!\n")
    
    # قائمة الخيارات التي يمكن للمستخدم تنفيذها
    options = """1. View Available Items
2. View Cart
3. Total Cart Price
4. Clear Cart
5. Quit"""

    while True:
        print(f"Avaliable Options:\n{options}")
        user_input = input("Enter the number of your choice: ")  # قراءة اختيار المستخدم
        
        # تنفيذ الخيار المناسب بناءً على مدخل المستخدم
        if user_input == "1":
            view_available_items(items)
        elif user_input == "2": 
            view_cart()
        elif user_input == "3":
            total_cart_price()
        elif user_input == "4": 
            clear_cart()
        elif user_input == "5":
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")
            
    # طباعة رسالة ختامية عند الخروج
    if not cart:
        print("No items have been bought")
        return
    
    print("Thanks for choosing Alawjan Store!")
    
    view_cart()
    total_cart_price()    
    


# عرض العناصر المتاحة للشراء والتعامل مع طلب المستخدم لإضافة عنصر
def view_available_items(items):
    display_items(items)  # طباعة جميع العناصر المتاحة
    
    item_index = get_user_selected_item(items)  # الحصول على رقم العنصر الذي اختاره المستخدم
    if item_index is None:
        return

    item_key = list(items.keys())[item_index]  # تحويل رقم العنصر إلى اسمه
    if items[item_key]["quantity"] == 0:
        print("Sorry, this item is out of stock.")
        return

    quantity = get_valid_quantity(items[item_key]["quantity"])  # التأكد من صلاحية الكمية المدخلة
    if quantity is None:
        return

    add_to_cart(item_key, items, quantity)  # إضافة العنصر للسلة
    print("Item has been added to the cart successfully.")


# دالة لطباعة قائمة العناصر مع الأسعار وتحديد حالة التوفر
def display_items(items):
    for i, (name, info) in enumerate(items.items(), 1):
        status = "(Out of stock)" if info["quantity"] == 0 else ""
        print(f"{i}. {name}: ${info['price']} {status}")


# دالة تطلب من المستخدم اختيار عنصر من القائمة
def get_user_selected_item(items):
    try:
        num = int(input("Please, Enter the number of the item you want (0 to return the previous menu): "))
    except:
        print("Invalid input, please enter a number.")
        return

    if num == 0:
        print("Returning to the previous menu...")
        return

    if 1 <= num <= len(items):
        return num - 1  # تحويل رقم العرض إلى فهرس في القاموس

    print("Invalid number. Please select from the list.")
    return


# دالة تطلب من المستخدم إدخال كمية العنصر وتتحقق من صحتها
def get_valid_quantity(available_quantity):
    print(f"Available quantity: {available_quantity}")
    try:
        qty = int(input("Please, Enter the quantity: "))
    except:
        print("Invalid input, please enter a number.")
        return

    if qty <= 0:
        print("Invalid quantity, must be greater than 0.")
        return
    if qty > available_quantity:
        print(f"Sorry, we only have {available_quantity} of this item.")
        return 

    return qty


# دالة لإضافة عنصر وكمية معينة إلى السلة وتحديث المخزون
def add_to_cart(item_name, items, quantity):
    price = items[item_name]["price"]
    current_quantity = cart.get(item_name, {}).get("quantity", 0)
    
    cart[item_name] = {
        "price": price,
        "quantity": current_quantity + quantity
    }

    items[item_name]["quantity"] -= quantity  # إنقاص الكمية من المخزون


# دالة لعرض محتويات السلة للمستخدم
def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    
    print("Cart:")
    print("-" * 30)
    for i, item in enumerate(cart, 1):
        item_price = cart.get(item).get("price")
        item_quantity = cart.get(item).get("quantity")
        total_of_item = item_price * item_quantity
        print(f"{i}. {item}: ${item_price:,.2f} x {item_quantity} = ${total_of_item:,.2f}")
    print("-" * 30)


# دالة لحساب وإظهار السعر الإجمالي للسلة
def total_cart_price():
    if not cart:
        print("Your cart is empty.")
        return
    
    total = 0
    for item in cart:
        item_price = cart.get(item).get("price")
        item_quantity = cart.get(item).get("quantity")
        total += item_price * item_quantity
    
    print(f"Total price of cart: ${total:,.2f}")


# دالة لمسح محتويات السلة بعد التأكيد من المستخدم
def clear_cart():
    if not cart:
        print("Your cart is empty.")
        return
    
    sure = input("Are you sure you want to clear the cart? (y/n): ").lower()
    
    if sure == "y":
        cart.clear()
        print("Cart has been cleared")
    elif sure == "n":
        print("Cart has not been cleared")
    else:
        print("Invalid input, please enter 'y' or 'n'.")
