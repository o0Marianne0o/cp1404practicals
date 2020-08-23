name = input("Enter name: ")
print("""(H)ello
(G)oodbye
(Q)uit""")
selected_menu = input(">>> ").upper()

while selected_menu != "Q":
    if selected_menu == "H":
        print("Hello", name)
    elif selected_menu == "G":
        print("Goodbye", name)
    else:
        print("Invalid input. Try again.")
    print("""(H)ello
(G)oodbye
(Q)uit""")
    selected_menu = input(">>> ").upper()
print("Finished.")
