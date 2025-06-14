project_num = input("Enter a project number: ")


if project_num == "1":
    def greet_user(name):
        
        print(f"\nWelcome {name.title()} at Codezilla python Course")
        print("Enjoy your Learning Journey")
    
    user_name= input("Enter your name: ")
    greet_user(user_name)


elif project_num == "2":
    def reverse(text):
        print(text[::-1])
    
    text = input("Enter your text: ")
    reverse(text)
    