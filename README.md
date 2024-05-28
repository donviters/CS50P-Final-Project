# CS50P Final Project - CS50 Conference
#### Video Demo: <https://youtu.be/eVDddnjf7wg>
#### Description:

#### My final project is a Python program that's intended to be used at a conference. Its purpose in life is to register the conference participants in a file called participants.csv and later take all the participants' data in the file to generate conference certificates for each participant.

## project.py
#### File that contains all the program's code. There's the main function and three additional functions that take care of the program's tasks.

### main
#### The main function starts by printing how the program is intended to be used. The user should insert in the command line a participant's data in the form 'first_name' 'last_name' 'email' 'date', where date is the date of participation in the conferece in YYYY/MM/DD format. In the next line the main function also prints how to exit the program: the user should press Ctrl + d when he's done entering participants.
#### The way it works is by entering an infinite loop that's broken with an EOFError. Inside the loop, the program prompts the user repeatedly for participants' data. This data is verified by calling the validate function. If the data is inputted incorrectly, the program shows the correct usage and prompts the user again. When the data is correct, it is stored in a dictionary for easier access. The program then calls the register function to add the data to the participants.csv file. Afterwards, the program welcomes the new participant with the conference mascot, a fox, by calling cowsay.fox.
#### Finally, when the user is done entering participants by pressing Ctrl + d, the generate_certificates function is called and creates certificates for all the participants registered in participants.csv.

### validate
#### The validate function takes four parameters: first_name, last_name, email, and a_date. It subsequently verifies each one with pattern matching. first_name and last_name should only contain word characters and spaces (if inputted with quotation marks). email is verified by using the validators module with the validators.email function. a_date should be in the format YYYY/MM/DD, having only digits and slashes. a_date is then tried to be passed to the date function from the datetime module to make sure that the date entered is valid. If any of the pattern matching tests fail, the validate function returns False, and the participant's data is not registered. However when all the tests pass, the function returns True, and the program can proceed to the data registration by calling the register function.

### register
#### The register function is only called when the validate function returns True. It takes the same four paramenters as the latter: first_name, last_name, email, and date.
#### It first checks if it will be necessary to write a header on the file. This is done by checking if the file is blank with the os.path.getsize or by checking if the file doesn't exist by trying to open it and catching a FileNotFoundError.
#### Then the function writes in append mode the four parameters to the file, separated with commas by using csv.DictWriter and specifying fieldnames for better design.
#### The function ends by returning True. This boolean value is used only for testing purposes in the test_project.py file.

### generate_certificates
#### The generate_certificates function is called after the user presses Ctrl + d during the program runtime. It takes only one parameter, which is the name of a file.
#### It first tries to open this file in read mode. In the case that it doesn't exist, the function is ready to handle a FileNotFoundError by exiting the program with sys.exit. But if, as expected, the file exists, the function uses the csv.DictReader to read each participant's data. It stores a participant's first name, last name, and participation date in variables (email could in theory be used in a later implementation to automatically send the certificates to the participants). Then it proceeds to create a certificate for each participant by instantiting an fpdf object as a landscape A4. It adds a page with add.page, inserts a certificate image template with pdf.image. The participant's first name and last name are written in the certificate in helvetica red italics. Then the participation date is written below in times black regular. Finally, the certificate pdf is created with pdf.output. The name of the pdf file is in the form 'last_name, first_name certificate'.

## test_project.py
#### File used to test with pytest the validate, register, and generate_certificates functions from the project.py file.

### test_validate
#### Function that tests the validate function from project.py. Uses some sample data to catch incorrect patterns in its parameters.

### test_register
#### Function that tests the register function from project.py. It tests that a sample of correct parameters returns True.

### test_generate_certificates
#### Function that tests the generate_certificates function from project.py. It tests that an inexistent file as parameter raises a system exit.

## requirements.txt
#### Lists all pip -installable libraries that the project requires, one per line.

## certificate.png
#### Template for all the certificates that the program generates with the generate_certificates function.
