import json

from constants import replacements

# Load the JSON file
with open('file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


# Function to fix specific misencoded sequences manually
def manual_fix_encoding(text):
    # Apply the replacements
    for wrong_char, correct_char in replacements.items():
        text = text.replace(wrong_char, correct_char)

    return text


# Iterate through each record and fix encoding issues
for record in data:
    # Correct the Title field if it exists
    if 'Title' in record:
        original_title = record['Title']
        record['Title'] = manual_fix_encoding(record['Title'])
        if original_title != record['Title']:
            print(f"Fixed Title from '{original_title}' to '{record['Title']}'")

    # Correct the Design field if it exists
    if 'Design' in record:
        original_design = record['Design']
        record['Design'] = manual_fix_encoding(record['Design'])
        if original_design != record['Design']:
            print(f"Fixed Design from '{original_design}' to '{record['Design']}'")

    if 'Design Company' in record:
        original_design = record['Design Company']
        record['Design Company'] = manual_fix_encoding(record['Design Company'])
        if original_design != record['Design Company']:
            print(f"Fixed Design from '{original_design}' to '{record['Design Company']}'")

# Save the corrected data back to a new JSON file
with open('file.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Data has been corrected and saved to 'corrected_data.json'")