import cowsay
import csv
import fpdf
import os
import re
import sys
import validators
from datetime import date


def main():

    # Show the usage instructions when running the program
    print("usage: first_name last_name email YYYY/MM/DD")
    print("Press Ctrl + D when done")

    # Infinite loop to prompt the user for participants until he presses Ctrl + d
    while True:

        try:
            participant = input("Participant: ")
        except EOFError:
            print()
            break

        # Unpack the space separated values with split into a dictionary. Catches ValueError if user doesn't enter exactly four space separated values, then prompts again
        participant_dict = {}
        try:
            participant_dict["first_name"], participant_dict["last_name"], participant_dict["email"], participant_dict["a_date"] = participant.split()
        except ValueError:
            print("usage: first_name last_name email YYYY/MM/DD")
            print("Press Ctrl + D when done")
            continue

        # Validate the four participant values with pattern matching
        if(validate(**participant_dict)):

            # After validating the participant values, the program registers them in the participants.csv file
            register(**participant_dict)

            # Then the fox mascot greets them
            cowsay.fox(f"Welcome {participant_dict["first_name"]} {participant_dict["last_name"]}!")

        # Invalid participant values are rejected and the user is prompted again
        else:
            print("usage: first_name last_name email YYYY/MM/DD")
            print("Press Ctrl + D when done")
            continue

    # Generate certificates for all the registered participants
    generate_certificates("participants.csv")


# validate function examines the four inputted participant values with pattern matching
def validate(first_name, last_name, email, a_date):

    # Validate the participant's first name. Should only contain word characters and spaces. Can have spaces if the first name is inputted with quotation marks
    if not re.search(r"^(\w|\s)+$", first_name):
        return False

    # Validate the participant's last name. Should only contain word characters and spaces. Can have spaces if the last name is inputted with quotation marks.
    if not re.search(r"^(\w|\s)+$", last_name):
        return False

    # Validate the participant's email
    if not validators.email(email):
        return False

    # Validate the participant's date of attendance in YYYY/MM/DD format. Must be a valid date
    if not re.search(r"^(\d{4})/(\d{2})/(\d{2})$", a_date):
        return False
    a_date = [int(_) for _ in a_date.split("/")]
    try:
        date(*a_date)
    except ValueError:
        return False

    # All pattern matching tests passed means that the function can return True
    return True


# register function takes four valid participant inputted values and writes them in the participants.csv file
def register(first_name, last_name, email, a_date):

    # https://www.geeksforgeeks.org/check-if-a-text-file-empty-in-python/
    # Write a header only when the participants.csv file is empty or doesn't exist
    write_header = False
    try:
        file_size = os.path.getsize("participants.csv")
        if file_size == 0:
            write_header = True
    except FileNotFoundError:
        write_header = True

    # Write the parcipant's data in the participants.csv file
    with open("participants.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["first name", "last name", "email", "date"])
        if write_header:
            writer.writeheader()
        writer.writerow({"first name": first_name, "last name": last_name, "email": email, "date": a_date})

    # return True when the function is successful. This value is used on test_project file
    return True


# generate_certificates function reads all the participants in the participants.csv file and generates a certificate for each of them
def generate_certificates(file_name):

    # Open the participants.csv file
    try:
        file = open(file_name)

    # Exit the program if it doesn't exist. This would mean that no participants have been registered
    except FileNotFoundError:
        sys.exit("No participants registered")

    # Read the participants.csv file and generate certificates for all registered participants
    else:
        with file:
            reader = csv.DictReader(file)
            for row in reader:

                # Data of each participant that will be added to each certificate
                first_name = row["first name"]
                last_name = row["last name"]
                a_date = row["date"]

                # Create fpdf object. Add a page. Set margins to zero.
                pdf = fpdf.FPDF(orientation="landscape", unit="mm", format="A4")
                pdf.add_page()
                pdf.set_margins(0, 0)

                # Add the image with (w,h) dimensions at the (x,y) position
                pdf.image("certificate.png", w=250, h=175, x=23.5, y=17.5)

                # Set the pointer around the middle of the certificate and write the participant's name in red
                pdf.set_y(85)
                pdf.set_font("helvetica", "I", 40)
                pdf.set_text_color(r=163, g=14, b=38)
                pdf.cell(297, 40, f"{first_name} {last_name}", border=0, align="C")

                # Set the pointer lower. Convert the month to word. Write the date in black
                pdf.set_y(134)
                pdf.set_font("Times", "", 16)
                pdf.set_text_color(r=0, g=0, b=0)
                a_date = [int(_) for _ in a_date.split("/")]
                a_date = date(*a_date)
                a_date = a_date.strftime("%B %d, %Y")
                pdf.cell(297, 10, f"{a_date}", border=0, align="C")

                # Generate the certificate for the participant
                pdf.output(f"{last_name}, {first_name} certificate.pdf")


if __name__ == "__main__":
    main()
