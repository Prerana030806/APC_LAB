import re

def count_file_extensions(filenames):
    # Regex to match file extensions (dot + letters/numbers)
    pattern = re.compile(r'\.[a-zA-Z0-9]+$')
    
    extension_count = {}
    
    for filename in filenames:
        match = pattern.search(filename)
        if match:
            ext = match.group()
            extension_count[ext] = extension_count.get(ext, 0) + 1
    
    return extension_count