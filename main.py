import string
import utils as u

exit = False
text = ""
while not exit:
    u.show_menu()
    option = u.get_option()

    if option == 1:
        text = input("Enter a string: ")
    elif option == 2:
        if len(text) != 0:
            lower, upper = u.upper_lower(text)
            u.print_option2_results(lower, upper)
        else:
            print("You need to enter a text through option 1")
    elif option == 3:
        if len(text) != 0:
            if u.is_it_a_date(text):
                print("The input is a date")
            else:
                print("The input is not a date")
        else:
            print("You need to enter a text through option 1")
    elif option == 4:
        # count the number of punctuation characters in our string
        if len(text) != 0:
            print("The number of punctuation characters in our string is: ",
                  u.count_punctuation_c(text, string.punctuation))
        else:
            print("You need to enter a text through option 1")
    elif option == 5:
        if len(text) != 0:
            punctuation_characters = u.get_punctuation_characters()
            print("The number of punctuation characters are: ", u.count_punctuation_c(text, punctuation_characters))
        else:
            print("You need to enter a text through option 1")
    elif option == 6:
        if len(text) != 0:
            print("We do things")
        else:
            print("You need to enter a text through option 1")
    elif option == 7:
        exit = True
        print("Program finished.")
    else:
        print("You have chosen an incorrect option. You need to choose a number between 1 and 7")