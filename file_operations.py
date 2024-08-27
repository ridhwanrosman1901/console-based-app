import os

def show_directory():
    """Display the current working directory and its contents."""
    print("Directory: ", os.getcwd())
    print("List of files and directories: ", os.listdir())

def create_directory():
    """Create a new directory called 'test_dir'."""
    os.mkdir("test_dir")
    print("New directory created.")

def change_directory():
    """Change the working directory to 'test_dir'."""
    os.chdir("test_dir")
    print("New working directory: ", os.getcwd())

def create_file():
    """Create a file named 'test_file.txt'."""
    with open("test_file.txt", "w") as file:
        file.write("This is a test file.")
    print("A file created.")

def delete_file():
    """Delete the file 'test_file.txt'."""
    os.remove("test_file.txt")
    print("File deleted.")

def delete_directory():
    """Change back to the parent directory and delete 'test_dir'."""
    os.chdir("..")
    os.rmdir("test_dir")
    print("Directory deleted.")
