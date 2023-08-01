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
        with open(os.path.join("logs", f"{domain}.txt"), "a") as file:
            for seq in seqs:
                file.write(seq + "\n")

if __name__ == "__main__":
    with open("sequences.txt", "r") as file:
        text = file.read()

    sequences = extract_seqs(text)
    organized_data = organize_seqs_by_domain(sequences)
    write_data_to_files(organized_data)
