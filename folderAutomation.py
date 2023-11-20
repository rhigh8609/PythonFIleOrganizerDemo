import os
import shutil

# Function to create a new folder if it does not exist
def create_folder(path):
    # Check if the folder already exists
    if not os.path.exists(path):
        # Create the folder
        os.makedirs(path)

# Function to move a file to a specified folder
def move_file(file, folder):
    # Move the file to the new location
    shutil.move(file, folder)

# Function to organize files in a directory based on a given file extension
def organize_directory(directory, file_extension, folder_name):
    # Combine the directory path and new folder name into a full path
    folder_path = os.path.join(directory, folder_name)
    # Create the new folder if it doesn't exist
    create_folder(folder_path)

    # Loop through each item in the specified directory
    for item in os.listdir(directory):
        # Check if the item is a file with the desired file extension
        if item.endswith(f".{file_extension}"):
            # Move the file to the specified folder
            move_file(os.path.join(directory, item), folder_path)
            # Print a message indicating the file has been moved
            print(f"Moved: {item} to {folder_path}/")

# Main function where the script starts execution
def main():
    # Prompt the user to enter the directory path
    directory = input("Enter the path of the directory you want to organize: ")
    # Check if the entered directory exists
    if not os.path.exists(directory):
        # Print an error message if the directory does not exist
        print("The provided directory does not exist. Please check the path and try again.")
        # Exit the function
        return

    # Prompt for the file extension to be organized
    file_extension = input("Enter the file extension to organize (e.g., 'jpg', 'pdf'): ")
    # Prompt for the name of the new folder
    folder_name = input("Enter the name of the new folder for these files: ")

    # Call the function to organize the directory
    organize_directory(directory, file_extension, folder_name)
    # Print a message once the organization is complete
    print("Files have been organized.")

# Python boilerplate to ensure the main function is called
if __name__ == "__main__":
    main()
