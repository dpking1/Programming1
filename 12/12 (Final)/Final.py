# Write a program that ensures a secure password has been created.
# The program should be written using a main() function that displays a menu
# that will use a while loop to call other functions.


# Prompts the user to enter a password then the user will be prompted again to
# re-enter their password to control for typos.

# The menu should be displayed as follows:

# Please select from the options below:
# 1. Check Password for Length.
# 2. Change Current Password.
# 3. Display History of Passwords.
# 4. Quit
# ------------------------------------------------------------------------------------------------------------------------------------------
# 1. Should use a function that takes in a password and displays the character length
# and a msg stating whether or not the entry has at least ten characters.
# 2. Should allow the user to change their password. They should be prevented from reusing any passwords
# that have been previously entered.
# 3. Should print out all of the passwords that have been entered (including passwords entered in #2).
# ------------------------------------------------------------------------------------------------------------------------------------------
# Users should receive an error message if they enter the wrong type of data into the menu.
#
# Special focus should be given to commenting throughout the program and formatting of messaging printed to the display.
#
# Extra Credit. Make sure that none of the passwords are on rockyou.txt (downloaded through github).


# Define a global variable to store the current password and the password history
password = None
password_history = []


def main():
    # Prompt the user to enter a password
    global check_password_length, change_password, display_password_history
    password = input("Enter your password: ")

    # Prompt the user to re-enter the password
    password_confirm = input("Re-enter your password to confirm: ")

    # If the passwords match, display the menu of options
    if password == password_confirm:
        print("Your passwords match. Password set.")
        while True:
            print("Please select from the options below:")
            print("1. Check Password for Length")
            print("2. Change Current Password")
            print("3. Display History of Passwords")
            print("4. Quit")

            # Functions for the numbered options
            try:
                option = int(input('Enter the number of the option you would like to select: '))
                if option == 1:
                    check_password_length()
                    # defines variable check_password_length()
                    def check_password_length():
                      if len(password) >= 10:
                        print('Password is sufficient length!')
                      else:
                        print('password is too short')

                elif option == 2:
                  change_password()

                    # defines variable change_password()
                  def change_password():
                        input('Enter New Password: ')
                        print('Password Changed!')



                elif option == 3:
                  display_password_history()

                    # defines variable display_password_history

                elif option == 4:
                    print('Goodbye!')
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid option number.")

    # If the passwords do not match, prints an error message
    else:
        print("Your passwords do not match. Please try again.")


main()
