def read_and_modify_file():
    # input filename
    input_filename = input("Enter the filename to read: ")

    try:
        # open and read the input file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify 
        modified_content = content.upper()

        # modified content to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Success! Modified file written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run 
read_and_modify_file()
