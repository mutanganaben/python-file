# file_handling_assignment.py

def create_file():
    try:
        # File Creation: Creates a new file named "my_file.txt" in write mode
        with open("my_file.txt", "w") as file:
            file.write("This is the first line.\n")
            file.write("The number is 12345.\n")
            file.write("Python file handling is easy.\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred during file creation: {e}")
    finally:
        print("File creation task completed.")

def read_file():
    try:
        # File Reading and Display: Reading the contents of "my_file.txt"
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nReading File Content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("File reading task completed.")

def append_to_file():
    try:
        # File Appending: Appending more lines to "my_file.txt"
        with open("my_file.txt", "a") as file:
            file.write("This is an appended line.\n")
            file.write("Numbers can be appended too: 67890.\n")
            file.write("File handling in Python is fun.\n")
        print("Text appended successfully.")
    except Exception as e:
        print(f"An error occurred during file appending: {e}")
    finally:
        print("File appending task completed.")

if __name__ == "__main__":
    create_file()    # Task 1: Create and write to the file
    read_file()      # Task 2: Read and display the file content
    append_to_file() # Task 3: Append to the file
    read_file()      # Task 4: Read the file again after appending
