#!/usr/bin/env python3

# Created by: Angelo Garcia
# Created on: November 6th, 2025
# Program asks the user for the length and width of a rectangle
# and tells the user whether or not it is a square


def main():
    # This line asks the user to enter the length (keeps it as text)
    length_as_string = input("Enter the length of the rectangle: ")
    print("")

    # This line asks the user to enter the width (keeps it as text)
    width_as_string = input("Enter the width of the rectangle: ")
    print("")

    try:
        # Convert the inputs to numbers
        length = float(length_as_string)
        width = float(width_as_string)

        # Check if the rectangle is a square
        if length == width:
            print("This is a square.")
        else:
            print("This is not a square.")

    except Exception:
        # Updated message for invalid (non-numeric) input
        print("One or both inputs were not valid numbers!")
        
    finally:
        # Closing message
        print("Thank you for using the program.")


if __name__ == "__main__":
    main()
