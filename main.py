import counter
import file_operations
import calculator

def main():
    while True:
        print("\nSimple Python App")
        print("1. Increment Counter")
        print("2. Reset Counter")
        print("3. Show Counter")
        print("4. File and Directory Operations")
        print("5. Division Calculator")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            counter.increment_counter()
        elif choice == '2':
            counter.reset_counter()
        elif choice == '3':
            counter.show_counter()
        elif choice == '4':
            file_operations_menu()
        elif choice == '5':
            division_calculator()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

def file_operations_menu():
    while True:
        print("\nFile and Directory Operations")
        print("1. Show Current Directory")
        print("2. Create Directory 'test_dir'")
        print("3. Change to 'test_dir' Directory")
        print("4. Create File 'test_file.txt'")
        print("5. Delete File 'test_file.txt'")
        print("6. Delete Directory 'test_dir'")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            file_operations.show_directory()
        elif choice == '2':
            file_operations.create_directory()
        elif choice == '3':
            file_operations.change_directory()
        elif choice == '4':
            file_operations.create_file()
        elif choice == '5':
            file_operations.delete_file()
        elif choice == '6':
            file_operations.delete_directory()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def division_calculator():
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        result = calculator.divide_num(a, b)
        if result is not None:
            print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
