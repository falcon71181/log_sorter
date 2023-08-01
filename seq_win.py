import os
import re

def extract_seqs(text):
    regex = r'URL: (?P<url>https?://(?:www\.)?([a-zA-Z0-9.-]+)\.\w+)/?\nUsername: (?P<username>.+)\nPassword: (?P<password>.+)\nApplication: (?P<app>.+)'
    matches = re.findall(regex, text)
    return matches

def organize_seqs_by_domain(seqs):
    domain_data = {}
    for seq in seqs:
        domain = seq[1]
        username = seq[2]
        password = seq[3]
        if domain not in domain_data:
            domain_data[domain] = []
        domain_data[domain].append(f"{username}:{password}")

    return domain_data

def write_data_to_files(data):
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    for domain, seqs in data.items():
        file_path = os.path.join("logs", f"{domain}.txt")
        with open(file_path, "a", encoding="utf-8") as file:
            for seq in seqs:
                file.write(seq + "\n")

if __name__ == "__main__":
    try:
        with open("sequences.txt", "r", encoding="utf-8") as file:
            text = file.read()

        sequences = extract_seqs(text)
        organized_data = organize_seqs_by_domain(sequences)
        write_data_to_files(organized_data)

        print("Data has been organized and written to separate files.")
    except FileNotFoundError:
        print("Error: 'sequences.txt' file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
