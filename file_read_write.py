# file_read_write.py

def modify_content(content):
    # Example modification: convert to uppercase
    return content.upper()

try:
    input_filename = input("Enter the name of the file to read: ")

    with open(input_filename, 'r') as infile:
        original_content = infile.read()

    modified_content = modify_content(original_content)

    output_filename = f"modified_{input_filename}"
    with open(output_filename, 'w') as outfile:
        outfile.write(modified_content)

    print(f"Modified content written to '{output_filename}' successfully!")

except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
except IOError:
    print("Error: Unable to read or write the file.")
