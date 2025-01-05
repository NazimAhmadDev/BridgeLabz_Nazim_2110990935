input_file = 'demo.txt'  
output_file = 'example.txt'  

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    line_number = 0
    for line in infile:
        line_number += 1
        if line_number == 5:
            continue  # Skip the 5th line
        outfile.write(line)  # Write all other lines to the new file
