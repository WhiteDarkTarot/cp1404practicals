"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""


def main():
    name = input("Enter name: ")

    display_menu = True
    while display_menu:
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")
        choice = input(">>> ").upper()

        if choice == "Q":
            print("Finished.")
            display_menu = False
        elif choice == "H":
            print("Hello", name)
        elif choice == "G":
            print("Goodbye", name)
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
