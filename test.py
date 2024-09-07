# Read the contents of the file
with open('filtered--subdomains.txt', 'r') as file:
    lines = file.readlines()

# Initialize a flag to start saving lines after the match
save_lines = False
filtered_lines = []

# Iterate over each line
for line in lines:
    # If we find the target URL, start saving lines
    if 'hwb-d1-trn-teller-temenos.fisglobal.com' in line:
        save_lines = True
    if save_lines:
        filtered_lines.append(line)

# Write the filtered lines back to the file
with open('filtered--subdomains.txt', 'w') as file:
    file.writelines(filtered_lines)
