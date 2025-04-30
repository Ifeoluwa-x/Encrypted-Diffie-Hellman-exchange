#!/usr/bin/env python3
from datetime import datetime

def load_vigenere_table():
    """Load the Vigenère table from step3"""
    table = []
    with open("../pubrepiar64/3extvigniar64", "r") as f:
        for line in f:
            if line.startswith("Char"):  # Skip header lines
                continue
            # Extract the row of characters (after colon)
            row = line.strip().split(':')[1].strip()
            table.append(list(row))
    return table

def process_text(text, vigenere_table):
    """
    Process the text with Vigenère table verification:
    1. All punctuation → {decimal} using table positions
    2. First letter uppercase, rest lowercase
    3. Preserve newlines
    """
    processed_lines = []
    chars = [chr(i) for i in range(32, 127)]  # ASCII 32-126
    
    for line in text.split('\n'):
        if not line:
            processed_lines.append('')
            continue
        
        # Process first character
        first_char = line[0]
        if first_char in chars and first_char.isalpha():
            processed_line = [first_char.upper()]
        else:
            dec_val = chars.index(first_char) + 32 if first_char in chars else ord(first_char)
            processed_line = [f'{{{dec_val}}}']
        
        # Process remaining characters
        for char in line[1:]:
            if char in ['\n', '\r']:
                processed_line.append(char)
            elif char in chars:
                if char.isalpha():
                    processed_line.append(char.lower())
                else:
                    dec_val = chars.index(char) + 32
                    processed_line.append(f'{{{dec_val}}}')
            else:
                processed_line.append(f'{{{ord(char)}}}')
        
        processed_lines.append(''.join(processed_line))
    
    return '\n'.join(processed_lines)

# Main execution
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Processing started at: {timestamp}")

try:
    # Load resources
    vigenere_table = load_vigenere_table()
    with open("../step8/8dplaintextiar64", "r") as f:
        decrypted_text = f.read()
    
    # Process text with table verification
    final_text = process_text(decrypted_text, vigenere_table)
    
    # Save output
    with open("9absolutefinaliar64", "w") as f:
        f.write(final_text)
    
    # Print results
    print("\nProcessed text:")
    print(final_text)
    print("\nOutput saved to 9absolutefinaliar64")

except FileNotFoundError as e:
    print(f"Error: {str(e)}")
    print("Please ensure these files exist:")
    print("- ../pubrepiar64/3extvigniar64")
    print("- ../step8/8dplaintextiar64")
except Exception as e:
    print(f"Processing failed: {str(e)}")

print(f"\nCompleted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
