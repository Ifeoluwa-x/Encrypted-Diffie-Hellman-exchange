#!/usr/bin/env python3
from datetime import datetime
import html  # For safe HTML output

# Step 1: Generate characters in specified order
chars = (
    [chr(i) for i in range(48, 58)] +    # Numbers (0-9)
    [chr(i) for i in range(97, 123)] +   # Lowercase (a-z)
    [chr(i) for i in range(65, 91)] +    # Uppercase (A-Z)
    [chr(i) for i in range(32, 48)] +    # Specials before numbers
    [chr(i) for i in range(58, 65)] +    # Specials between numbers and uppercase
    [chr(i) for i in range(91, 97)] +    # Specials between uppercase and lowercase
    [chr(i) for i in range(123, 127)]    # Remaining specials
)

assert len(chars) == 95, "Character set must contain exactly 95 characters."

# Step 2: Generate the 95x95 Vigenère Table
vigniere_table = []
for i in range(len(chars)):
    row = chars[i:] + chars[:i]
    vigniere_table.append(row)

# Step 3: Save the matrix to a file in a readable format
with open("3extvigniar64", "w") as f:
    for row in vigniere_table:
        f.write(''.join(row) + '\n')  # Write row as a line of characters

# Step 4: Save the table as HTML (optional visualization)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("3extVigniereiar64.html", "w") as f:
    f.write(f"<html><head><title>Extended Vigenère Table</title></head><body>\n")
    f.write(f"<h2>Timestamp: {timestamp}</h2>\n")
    f.write("<table border='1' style='font-family: monospace; font-size: 12px;'>\n")
    for row in vigniere_table:
        f.write("<tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in row) + "</tr>\n")
    f.write("</table>\n</body></html>")

print(f"Matrix saved to '3extvigniar64'")
print(f"HTML visualization saved to '3extVigniereiar64.html'")
print(f"Timestamp: {timestamp}")

