#Glossary of flashcards

from random import *
import csv

def file_to_dictionary(filename):
    '''
    Return a dictionary with the contents of a file
    '''
    file = open(filename, 'r')
    reader = csv.reader(file)
    dictionary = {}
    for row in reader:
        dictionary[row[0]] = row[1]
    return dictionary
    

glossary = file_to_dictionary('TM112_Glossary.txt')
gloss_list = list(glossary)

def show_flashcard():
    '''
    Show the user a random key and ask them for the answer
    '''

    random_key = choice(gloss_list)
    print('Define: ', random_key)
    input('Press return to see the other side')
    print(glossary[random_key])



def interactive_loop():
    '''
    Get the input from the user to continue the program or quit
    '''

    exit = False

    while not exit:
        user_input = input('Enter s to show the flashcard and enter q to quit: ')
        if user_input == 'q':
            exit = True
        elif user_input == 's':
            show_flashcard()
        else:
            print('You need to enter an s or a q')


interactive_loop()

