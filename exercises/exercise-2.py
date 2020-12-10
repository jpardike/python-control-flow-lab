# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.




def character_length():
    user_input = input('Please enter a word or phrase: ')
    if user_input == 'quit':
        exit()
    user_input_length = len(user_input)
    print(f'What you entered is {user_input_length} characters long')
    return character_length()

character_length()