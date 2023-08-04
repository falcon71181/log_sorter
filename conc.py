import os

def append_txt_files(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as combined_file:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as txt_file:
                    combined_file.write(txt_file.read())
                combined_file.write('\n')  # Add a new line between files

if __name__ == "__main__":
    folder_path = "pass"
    output_file = "combined.txt"
    append_txt_files(folder_path, output_file)
    print("All .txt files in the folder have been combined into combined.txt.")
