# Version 0.2

# No to tak, jak to ma działać? Metoda gradientu jest spoko, ale tutaj mamy mocno ograniczoną liczbę elementów
# o konkretnych wartosciach.
# Zobaczmy czy zadziala taka funkcja dmg(character, weapon, feather, goblet, crown, time_piece, flower) = []
# Printuje zestaw ktory mial najwiesza wartosc
# 2 tryby pracy - optymalne_itemy, itemy_usera
# zacznijmy od bazy danych itemow usera - done
from EQtools import Artifacts

artifact_types = ['F', 'C', 'G', 'T', 'Fl']

def menu():
    print('Welcome to Genshin Impact Character Optimized 0.1')
    user_input = ''

    while user_input != 'Q':
        print('''
        Choose one of the following options:
        A - to add an Artifact
        L - to list all artifacts
        D - to delete an artifact
        Q - to quit the program''')
        user_input = input(': ')

        if user_input == 'A':
            prompt_add_artifact()
        elif user_input == 'L':
            list_artifacts()
        elif user_input == 'D':
            prompt_delete_artifact()
        elif user_input == 'Q':
            exit()
        else:
            print("Unknown command, please try again")


def exit():
    print('Thank you for using GenshinCalc 0.1')

def prompt_add_artifact():
    user_choice = input('''
What kind of artifact would you like to add?
[F]eather, [C]ap, [G]oblet, [T]imepieace or [Fl]ower?
: ''')
    if user_choice == 'F':
        Artifacts.add_feather()
    elif user_choice == 'C':
        Artifacts.add_crown()
    elif user_choice == 'G':
        Artifacts.add_goblet()
    elif user_choice == 'T':
        Artifacts.add_time_piece()
    elif user_choice == 'Fl':
        Artifacts.add_flower()

def artifact_list_formatting(result):
    atribute_list = []
    atribute_name_list = []
    for dictionary in result:
        for i in dictionary:
            if dictionary[i] != None:
                atribute_list.append(dictionary[i])
                atribute_name_list.append(i)
    l = len(atribute_name_list)

    if l % 8 == 0:
        composite_AN = [atribute_name_list[x:x + 8] for x in range(0, len(atribute_name_list), 8)]
        composite_A = [atribute_list[x:x + 8] for x in range(0, len(atribute_list), 8)]
        amount_of_items = int(l / 8)
        for x in range(0, amount_of_items, 1):
            atribute_name_list = composite_AN[x]
            atribute_list = composite_A[x]

            print(f'{atribute_name_list[0]}: {atribute_list[0]}, {atribute_name_list[1]}: {atribute_list[1]}, '
                  f'{atribute_name_list[2]}: {atribute_list[2]}, {atribute_name_list[3]}: {atribute_list[3]}, '
                  f'{atribute_name_list[4]}: {atribute_list[4]}, {atribute_name_list[5]}: {atribute_list[5]}, '
                  f'{atribute_name_list[6]}: {atribute_list[6]}, {atribute_name_list[7]}: {atribute_list[7]}.')

    elif l % 7 == 0:
        composite_AN = [atribute_name_list[x:x + 7] for x in range(0, len(atribute_name_list), 7)]
        composite_A = [atribute_list[x:x + 7] for x in range(0, len(atribute_list), 7)]
        amount_of_items = int(l / 7)
        for x in range(0, amount_of_items, 1):
            atribute_name_list = composite_AN[x]
            atribute_list = composite_A[x]

            print(f'{atribute_name_list[0]}: {atribute_list[0]}, {atribute_name_list[1]}: {atribute_list[1]}, '
                  f'{atribute_name_list[2]}: {atribute_list[2]}, {atribute_name_list[3]}: {atribute_list[3]}, '
                  f'{atribute_name_list[4]}: {atribute_list[4]}, {atribute_name_list[5]}: {atribute_list[5]}, '
                  f'{atribute_name_list[6]}: {atribute_list[6]}.')

    elif l % 6 == 0:
        composite_AN = [atribute_name_list[x:x + 6] for x in range(0, len(atribute_name_list), 6)]
        composite_A = [atribute_list[x:x + 6] for x in range(0, len(atribute_list), 6)]
        amount_of_items = int(l / 6)
        for x in range(0, amount_of_items, 1):
            atribute_name_list = composite_AN[x]
            atribute_list = composite_A[x]

            print(f'{atribute_name_list[0]}: {atribute_list[0]}, {atribute_name_list[1]}: {atribute_list[1]}, '
                  f'{atribute_name_list[2]}: {atribute_list[2]}, {atribute_name_list[3]}: {atribute_list[3]}, '
                  f'{atribute_name_list[4]}: {atribute_list[4]}, {atribute_name_list[5]}: {atribute_list[5]}.')

    elif l % 5 == 0:
        composite_AN = [atribute_name_list[x:x + 5] for x in range(0, len(atribute_name_list), 5)]
        composite_A = [atribute_list[x:x + 5] for x in range(0, len(atribute_list), 5)]
        amount_of_items = int(l / 5)
        for x in range(0, amount_of_items, 1):
            atribute_name_list = composite_AN[x]
            atribute_list = composite_A[x]

            print(f'{atribute_name_list[0]}: {atribute_list[0]}, {atribute_name_list[1]}: {atribute_list[1]}, '
                  f'{atribute_name_list[2]}: {atribute_list[2]}, {atribute_name_list[3]}: {atribute_list[3]}, '
                  f'{atribute_name_list[4]}: {atribute_list[4]}.')


def list_artifacts():
    user_choice = input('''
    What kind of artifact would you like listed?
    [F]eather, [C]ap, [G]oblet, [T]imepieace, [Fl]ower or [A]ll?
    : ''')
    if user_choice == 'F':
        result = Artifacts.list_all_artifacts('F')
        artifact_list_formatting(result)

    elif user_choice == 'C':
        result = Artifacts.list_all_artifacts('C')
        artifact_list_formatting(result)
    elif user_choice == 'G':
        result = Artifacts.list_all_artifacts('G')
        artifact_list_formatting(result)
    elif user_choice == 'T':
        result = Artifacts.list_all_artifacts('T')
        artifact_list_formatting(result)
    elif user_choice == 'Fl':
        result = Artifacts.list_all_artifacts('Fl')
        artifact_list_formatting(result)
    elif user_choice == 'A':
        for type in artifact_types:
            result = Artifacts.list_all_artifacts(type)
            artifact_list_formatting(result)
    else:
        print('Unknown command.')
        list_artifacts()



menu()
