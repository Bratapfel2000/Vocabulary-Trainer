from random import *
import csv

#################################
#                               #
#     vokabeltrainer2000        #
#     written in python 3.7     #
#                               #
#################################
version = "0.112"

vocabulary_file = 'vokabeln.csv'

#vocabularies are stored in dict() entry which will be called 'field', consisting
#of word in language1, word in language2, correct answer, wrong answer
#example field[3] = ['paste', 'kleister', 0, 0]

#csv file reader
def readMyFile(filename):
    lang1 = []
    lang2 = []
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            lang1.append(row[0])
            lang2.append(row[1])
    return lang1, lang2
lang1,lang2 = readMyFile(vocabulary_file)

#'headline' - name of languages in first line, will be capitalized also
lang_1 = str(lang1[0]).capitalize()
lang_2 = str(lang2[0]).capitalize()

#takes csv and returns fields, with words and slots for statistics
field = {}
##field[0] = ["en","de","stats1"]
## field[i-1][0] assigns words to list, words are from lang1[i]
##and first line in lang1/2 is telling the name of the languages 
def fields():
    global field
    for i in range(1, len(lang1)):
        #[lang1,lang2,correct,wrong]
        field[i-1] = [0,0,0,0]
        field[i-1][0] = lang1[i]
        field[i-1][1] = lang2[i]
fields()

#for later use when word lists are updated
def make_new_list():
    global new_word_list
    new_word_list = list()
    for i in field:
        new_word_list.append(field[i])

#to update fields from dict->list->dict
def global_field_updater():
    global field_update
    make_new_list()
    field = dict()
    field_update = dict()
    for i in range(len(new_word_list)):
        field_update[i] = new_word_list[i]

#assigns fields to updated fields (ie. with less words)
def changer_of_field():
    global field
    field = dict()
    for i in range(len(field_update)):
        field[i] = field_update[i]

#wrong input error
def wrong_input():
    print(" ")
    print(22* "-")
    print("Wrong input. Try again")
    print(22* "-")
    print(" ")

def back_main():
    print(" ")
    enter_menu = input("Press [Enter] to go back ")
    print(" ")
    if enter_menu == "":
        print(" ")
        return commando()
    else:
        wrong_input()
        back_main()
       
#menu 
def menu():
    print(" ")
    print(" ")
    print("Command                   key")
    print("=============================")
    print("Info                        i")
    print("-----------------------------")
    print("Show dictionary             p")
    print("-----------------------------")
    print("Update words                u")
    print("-----------------------------")
    print("Update words II             v")
    print("-----------------------------")
    print("Add words                   a")
    print("-----------------------------")    
    print("Delete words                d")
    print("-----------------------------")    
    print("Show statistics             s")
    print("-----------------------------")    
    print("Export csv file             x")
    print("-----------------------------")    
    print("Back to main menu           m")
    print(" ")
    enter_menu = input("Enter  key: ")
    print(" ")
    return enter_menu

#menu commands
def commando():
    enter_cmd = menu()
    if enter_cmd == "i":
        return info()
    if enter_cmd=="p":
        show_me_all_words(35)
        print(" ")
        return back_main()
    if enter_cmd=="u": 
        update_words_by_index()
        print(" ")
        return commando()
    if enter_cmd == "v":
        update_words_by_words()
        print(" ")
        return commando() 
    if enter_cmd=="a":
        word_adder()
        return commando()
    if enter_cmd == "d":
        delete_words()
        print(" ")
        return commando()
    if enter_cmd=="s":
        find_tested_words()
        print(" ")
        return back_main()
    if enter_cmd=="x":
        csv_exporter()
        print(" ")
        return commando()
    if enter_cmd == "m":
        return start_screen()
    else:
        wrong_input()
        commando()

#menu item: 'Info'
def info():
    print("With this vocabulary trainer you can train ")
    print("your choice of specific words as often as you")
    print("like. You can also choose which direction you ")
    print("want to be tested and how many words randomly")
    print("should show up.")
    print(" ")
    back_main()

#menu item: 'Show dictionary'
##new (modified) dict() with 'dir /p' function
def show_me_all_words(number_words=35):
    length = len(field)
    parts = length // number_words
    rest = length % number_words
    for i in range(parts):
        show_me_some_words(i*number_words,i*number_words+number_words)
        dir_p = input("Press Enter . . . ")
        print(" ")
    for i in range(length-len(field)%number_words, length):
        print('%-6i%-22s%-22s' %
              (i+1,
               field[i][0],
               field[i][1]))
         
##displays words in range from j to k
        #belongs toshow_me_all_words(number_words)
def show_me_some_words(j,k):
    for i in range(j,k):
        print('%-6i%-22s%-22s' %
              (i+1,
               field[i][0],
               field[i][1]))

#shows original csv data, not in use
def print_original_csv():
    print("#original 2-columns file")
    for i in range(len(lang1)):
        print(lang1[i], lang2[i])

#menu item: update words I
#update word by chosing entry number in list
def update_words_by_index():
    z = len(field)
    print("[ Enter number of word to change at the end ]")
    print(" ")
    show_me_all_words()
    print(" ")
    input_howmany = how_many_words('Enter number of word to change [1-'+str(z)+'] or [0] to go back: ')
    if input_howmany in range(1, z+1):
        print(" ")
        print(field[int(input_howmany)-1][0], field[int(input_howmany)-1][1])
        print(" ")
        input_lang = input("Change "+lang_1+" [1] or "+lang_2+" [2] word, [0] to go back : ")
        if input_lang == "1":
            print(" ")
            print("Old word is", field[int(input_howmany)-1][0])
            print(" ")
            input_word_new = input("Enter new word: ")
            field[int(input_howmany)-1][0] = input_word_new
            print(" ")
            print("Word updated")
            print(" ")
            input("Press [Enter] to go back")
            return
        if input_lang == "2":
            print(" ")
            print("Old word is", field[int(input_howmany)-1][1])
            print(" ")
            input_word_new = input("Enter new word: ")
            field[int(input_howmany)-1][1] = input_word_new
            print(" ")
            print("Word updated")
            print(" ")
            input("Press [Enter] to go back")
            return
        if input_lang == "0":
            return
        else:
            wrong_input()
            updater(input_howmany)
    if input_howmany == 0:
        return 
    else:
        wrong_input()
        update_words_by_index()
   
#menu item: update words II 
#update word by entering word
def update_words_by_words():
    z = len(field)
    show_me_all_words(35)
    print(" ")
    input_change_word = input("Enter word you want to change or [Enter] to go back: ")
    for i in range(len(field)):
        if input_change_word in field[i]:
            print(" ")
            print("'"+field[i][0]+"' - '"+field[i][1]+"'")
            print(" ")
            input_lang = input("[1] to change "+lang_1+" word - [2] for "+lang_2+" - [0] to go back: ")
            if int(input_lang) == 1:
                print(" ")
                print("Old word is", field[i][0])
                print(" ")
                input_word_new = input("Enter new word: ")
                print(" ")
                save_updated = input("Updated word is: '"+input_word_new+"' - '"+field[i][1]+"'. Save? [Y/N]")
                if save_updated == "y" or "Y":
                    field[i][0] = input_word_new
                    print(" ")
                    print("Word updated")
                    print(" ")
                    input("Press enter to go back")
                    return 
                else:
                    print(" ")
                    print("Word not updated")
                    print(" ")
                    input("Press enter to go back")
                    return
            if int(input_lang) == 2:
                print(" ")
                print("Old word is", field[i][1])
                print(" ")
                input_word_new = input("Enter new word: ")
                print(" ")
                save_updated = input("Updated word is: '"+field[i][0]+"' - '"+input_word_new+"'. Save? [Y/N]")
                if save_updated == "y" or "Y":
                    field[i][1] = input_word_new
                    print(" ")
                    print("Word updated")
                    print(" ")
                    input("Press enter to go back")
                    return 
                else:
                    print(" ")
                    print("Word not updated")
                    print(" ")
                    input("Press enter to go back")
                    return
            if int(input_lang) == 0:
                return
            else:
                print("Input not valid. Try again.")
        elif input_change_word == "":
            return
    else:
        print(" ")
        print("Input not valid. Try again.")
        print(" ")
        return update_words_by_words()

#menu item: 'add words'
def word_adder():
    input_lang1 = input("enter new word ("+lang_1+") - [0] to cancel: ")
    if input_lang1 == "0":
        return 
    input_lang2 = input("enter new word ("+lang_2+") - [0] to cancel: ")
    if input_lang2 == "0":
        return 
    input_check = input(("Add " +input_lang1 +" " + input_lang2+ " to dictionary? [Y/N]"))
    if input_check == "y" or "Y":
        z = len(field)
        field[z] = [0,0,0,0]
        field[z][0] = input_lang1
        field[z][1] = input_lang2
        print("---------------")
        print("New words added")
        print("---------------")
        return 
    if input_check == "n" or "N":
        print("-------------------")
        print("New words not added")
        print("-------------------")
        return 
    else:
        wrong_input()
        return word_adder()

#to add additional words in 'add words'
def word_adder_new():
    input_lang3 = input("Add new word? [Y/N]")
    if input_lang3 == "n" or "N":
        return 
    if input_lang3 == "y" or "Y":
        return word_adder()
    else:
       wrong_input()
       word_adder_new()
       
#menu item: 'delete words'
def delete_words():
    z = len(field)
    print("[ Enter number of word to delete at the end ]")
    print(" ")
    show_me_all_words(35)
    print(" ")
    input_howmany = how_many_words('Enter number of word to delete (1-'+str(z)+') or [0] to go back: ')
    if input_howmany in range(1,len(field)+1):
        print(" ")
        del_for_real = input("Delete '"+field[int(input_howmany)-1][0]+"'"+" - "+"'"+field[int(input_howmany)-1][1]+"' ? [Y/N]")
        if del_for_real == "y" or "Y":
            print(" ")
            print("'"+field[int(input_howmany)-1][0]+"'"+" - "+"'"+field[int(input_howmany)-1][1],"'", "deleted")
            del field[int(input_howmany)-1]
            print(" ")
            global_field_updater()
            input("Press Enter to go back")
            return changer_of_field()
        elif del_for_real == "n" or "N":
            return 
        else:
            wrong_input()
            return delete_words()
    if input_howmany == 0:
        return
    else:
        wrong_input()
        delete_words()

#not in use
def show_stats():
    print('%-3s%-12s%-12s%-8s%-8s%-8s' %("#", lang_2, lang_1, "Right", "Wrong", "Total"))
    print(51*"-")
    for i in range(len(field)):
        print('%-3i%-12s%-12s%-8i%-8i%-8i' %
              (i+1,
               field[i][0],
               field[i][1],
               field[i][2],
               field[i][3],
               field[i][2]+field[i][3]))

#menu item: 'show statistics'
#displays at the end  the words which were tested + stats
def find_tested_words():
    print('%-6s%-22s%-22s%-8s%-8s%-8s' %("#", str(lang1[0]).capitalize(), str(lang2[0]).capitalize(), "Right", "Wrong", "Total"))
    print(71*"-")
    for i in range(len(field)):
        if field[i][2]+field[i][3] != 0:
            print('%-6i%-22s%-22s%-8i%-8i%-8i' %
              (i+1,
               field[i][0],
               field[i][1],
               field[i][2],
               field[i][3],
               field[i][2]+field[i][3]))
        
#menu item: 'Export csv file'
def csv_exporter():
    file_namer = input("enter name for csv-file or [Enter] to go back: ")
    if file_namer == "":
        return 
    else:
       with open(file_namer+'.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in field.items():
           writer.writerow([key, value[0], value[1], value[2], value[3]])
        print(" ")
        print('"'+file_namer+'.csv'+'"'+" exported")
        print(" ")
        input("Press [Enter] to go back")
        return

#start screen options
def start_screen():
    print(" ")
    print(" ------------------------------------------------")
    print(" Vocabulary Trainer 2000 - Version "+version)
    print(" ------------------------------------------------")
    print(" ")
    input_menu = input("Press [Enter] to start / 'M' for Menu / 'Q' for quit: ")
    if input_menu == "":
        print(" ")
        return trainer()
    if input_menu == "m":
        return commando()
    if input_menu == "q":
        return print("Ciao!")
##        exit()
    else:
        wrong_input()
        start_screen()

#takes a random number from range of length of vocabulary_file
def lang1_lang2_rand_picker():
    #length_dict =len(lang1)  # raus wg delete words aktion
    length_dict =len(field)
    rand_no = randint(0, length_dict-1)
    return rand_no

#how many vocabularies to check
def how_many_words(display_input):
    while True:
        try:
            enter_val  = int(input(display_input))
        except ValueError:
            wrong_input()
            continue
        else:
            return enter_val 

#chose language direction and do questionaire + show results
def direction_language(x,y):
    j = 0
    k = 0
    for i in range(how_many_words("How many words to check?: ")):
        print(" ")
        rand_no = lang1_lang2_rand_picker()
        input_lang = input(field[rand_no][x]+" : ")
        if input_lang.capitalize() == field[rand_no][y].capitalize():
            j += 1
            field[rand_no][2] += 1
            print("Correct!")
            print(" ")
        else:
            k += 1
            field[rand_no][3] += 1
            print("Wrong. The Correct answer is: ", field[rand_no][y])
            print(" ")
    print(" ")
    print(6*"-","Results", 6*"-")
    print("Correct:",j, "Wrong:", k)
    print(21*"-")

#play again
def do_again():
    print(" ")
    do_again_input = input("Play again? [y/n]")
    if do_again_input == "y" or "Y":
        return trainer()
    if do_again_input == "n" or "N":
        return start_screen()
    else:
        print(do_again_input)
        wrong_input()
        do_again()
    
#train words, count right or wrong
def trainer():
    input_lang_direction = input("[1] "+str(lang1[0]).capitalize()
                             +"-"+str(lang2[0]).capitalize()
                             +" - [2] "+str(lang2[0]).capitalize()
                             +"-"+str(lang1[0]).capitalize()+" - [0] Start Screen: ")
    if input_lang_direction == "1":
        direction_language(0,1)
        find_tested_words()
        return do_again()
    if input_lang_direction == "2":
        direction_language(1,0)
        find_tested_words()
        return do_again()
    if input_lang_direction == "0":
        return start_screen()
    else:
        wrong_input()
        return trainer()

start_screen()
