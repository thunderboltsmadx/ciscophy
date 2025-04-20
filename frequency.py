def letter_frequency(filename):
    # Create an empty dictionary to store letter counts
    frequency = {}

    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the content and convert to lowercase
            text = file.read().lower()

            # Loop through each character in the text
            for char in text:
                if char.isalpha():  # Count only letters
                    if char in frequency:
                        frequency[char] += 1
                    else:
                        frequency[char] = 1

        # Print the frequencies
        for letter in sorted(frequency):
            print(f"{letter}: {frequency[letter]}")

    except FileNotFoundError:
        print("File not found. Please check the filename and path.")

# Example usage
filename = "sample.txt"  # Replace with your file name
letter_frequency(filename)
