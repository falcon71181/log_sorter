import os

def remove_duplicates_from_file(file_path):
    lines_seen = set()
    updated_lines = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line not in lines_seen:
                lines_seen.add(stripped_line)
                updated_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

def process_files_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            remove_duplicates_from_file(file_path)
            print(f'Duplicates removed from {file_name}')

if __name__ == "__main__":
    logs_folder = input("Enter the path to the logs folder: ")
    process_files_in_folder(logs_folder)
