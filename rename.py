import os

def rename_folders(base_folder):
    if not os.path.exists(base_folder):
        print(f"Error: The folder '{base_folder}' does not exist.")
        return
    
    folder_list = [name for name in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, name))]
    
    for index, folder_name in enumerate(sorted(folder_list, key=lambda x: int(''.join(filter(str.isdigit, x))))):
        old_path = os.path.join(base_folder, folder_name)
        new_name = str(index + 1)
        new_path = os.path.join(base_folder, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renaming '{folder_name}' to '{new_name}'")

if __name__ == "__main__":
    base_folder = input("Enter the base folder path: ")
    rename_folders(base_folder)
