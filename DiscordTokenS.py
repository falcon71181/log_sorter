import os

def append_passwords(base_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as sequences_file:
        for root, _, files in os.walk(base_folder):
            for file in files:
                if file == 'Tokens.txt':
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as passwords_file:
                        passwords = passwords_file.read()
                        sequences_file.write(passwords)
                        sequences_file.write('\n')

if __name__ == "__main__":
    base_folder = input("Enter the base folder path: ")
    output_file = "DiscordTokens.txt"
    append_passwords(base_folder, output_file)
    print(f"All Passwords.txt files in folder '{base_folder}' have been appended to '{output_file}'.")
