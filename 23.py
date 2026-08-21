def find_and_replace(input_file, output_file, target, replacement, case_sensitive=True):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if case_sensitive:
        modified_text = text.replace(target, replacement)
    else:
        # Case-insensitive replacement
        import re
        # re.IGNORECASE ensures all matches regardless of case
        modified_text = re.sub(target, replacement, text, flags=re.IGNORECASE)
    
    # Write to new file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(modified_text)
    
    print(f"Replacement complete. Modified text saved to {output_file}")

find_and_replace("sample.txt", "output.txt", "Hello", "hiii", case_sensitive=False)
