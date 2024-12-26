


# # Contact List Program

# # A dictionary to store contacts with name as key and phone number as value

# from tkinter import *

# imaginary_root = Tk()
# imaginary_root.title("Simple calculator")
# imaginary_root.geometry("570x600+100+200")
# imaginary_root.resizable(False,False)
# imaginary_root.configure(bg="black")

# equation=""

# def show (value):
#     global equation
#     equation+=value
#     Label_result.config(text=equation)
    
# def clear():
#     global equation
#     equation = ""
#     Label_result.config(text=equation)
    
# def calculate():
#     global equation
#     result = ""
#     if equation != "":
#         try:
#             result= eval(equation)
#         except:
#             result= "error"
#             equation = ""
#     Label_result.config(text=result)
        


# Label_result=Label(imaginary_root,width=25,height=2,text="",font=("arial",30))
# Label_result.pack()
# # for uppor buttons
# Button(imaginary_root,text="C",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)
# Button(imaginary_root,text="/",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=150,y=100)
# Button(imaginary_root,text="%",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=290,y=100)
# Button(imaginary_root,text="*",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=430,y=100)
# # Label_result.pack()

# # for middle buttons
# Button(imaginary_root,text="7",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("7")).place(x=10,y=200)
# Button(imaginary_root,text="8",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("8")).place(x=150,y=200)
# Button(imaginary_root,text="9",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("9")).place(x=290,y=200)
# Button(imaginary_root,text="-",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("-")).place(x=430,y=200)

# # for second middle button
# Button(imaginary_root,text="6",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("6")).place(x=10,y=300)
# Button(imaginary_root,text="5",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("5")).place(x=150,y=300)
# Button(imaginary_root,text="4",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("4")).place(x=290,y=300)
# Button(imaginary_root,text="+",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("+")).place(x=430,y=300)

# # second last button
# Button(imaginary_root,text="1",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("1")).place(x=10,y=400)
# Button(imaginary_root,text="2",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("2")).place(x=150,y=400)
# Button(imaginary_root,text="3",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("3")).place(x=290,y=400)
# Button(imaginary_root,text="0",width="11",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show("0")).place(x=10,y=500)

# # for last buttons
# Button(imaginary_root,text=".",width="5",height="1",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d20",command=lambda: show(".")).place(x=290,y=500)
# Button(imaginary_root,text="=",width="5",height="3",font=("arial",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda: calculate()).place(x=430,y=400)

contacts = {}

# Function to add a contact

def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter the phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added successfully!")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("Contact list is empty.")

# Function to search for a contact
def search_contact():
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        print(f"Contact found: {name} - {contacts[name]}")
    else:
        print(f"No contact found with the name {name}.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input(f"Enter new phone number for {name}: ")
        contacts[name] = phone
        print(f"Contact for {name} updated successfully!")
    else:
        print(f"No contact found with the name {name}.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"No contact found with the name {name}.")

# Function to display the menu
def display_menu():
    print("\n--- Contact List Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Main function to run the program
def contact_list():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the contact list. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run the contact list program
if __name__ == "__main__":
    contact_list()
    
# imaginary_root.mainloop()





# # from tkinter import *

# # imaginary_tech_root =Tk()
# # # for height and width
# # imaginary_tech_root.geometry("664x435")

# # kuna =Label(text="kunal is the good boy.")

# # kuna.pack() 

# # # for height and width
# imaginary_tech_root.minsize(300,200)

# imaginary_tech_root.mainloop()




