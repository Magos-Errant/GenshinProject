import copy
import collections

from EQtools.database_connection import Database_Connect

def _questions_for_user(type):
    print('''
    Answer following questions refering to stats as:
    ATK, ATKp, DEF, DEFp, HP, HPp, Elemental_Mastery,
    Energy_Recharge_p, CRIT_rate_p, CRIT_DMG_p)
    ''')

    answers = []
    user_item_set = input("What is the name of this item set? (Gladiator, Witch, ect): ")
    answers.append({"Set_name": user_item_set})
    user_item_rarity = input("What is rarity of your item? (1-5): ")
    answers.append({"Rarity": user_item_rarity})

    limit_of_level = {1:"4", 2:"8", 3:"12", 4:"16", 5:"20"}

    user_item_level = input(f"What is the level of your item? (1-{limit_of_level[int(user_item_rarity)]}): ")
    answers.append({"Item_level": user_item_level})

    if type == 'F':
        user_primary_stat = "ATK"
    elif type == 'Fl':
        user_primary_stat = "HP"
    else:
        user_primary_stat = input("What is primary stat of your item?: ")

    answers.append({"Primary_stat": user_primary_stat})

    secondary_stat_amount = int(input("How many secondary stats does your item has? (1-4): "))

    for x in range(1, secondary_stat_amount+1):
        if x == 1:
            A = 'first'
        elif x == 2:
            A = 'second'
        elif x == 3:
            A = 'third'
        elif x == 4:
            A = 'fourth'

        answer = input(f'Your {A} secondary stat is?: ')

        if answer == 'ATK' and type == 'F':
            print('Feathers cannot have flat ATK as secondary stat!')
            _questions_for_user('F')
        elif answer == 'HP' and type == 'Fl':
            print('Flowers cannot have flat HP as secondary stat!')
            _questions_for_user('Fl')
        else:
            answer_val = input(f'Your {A} secondary stat value is?: ')

            answer = {answer: answer_val}
            answers.append(answer)

    return answers

def _formatting_for_SQLite(answers):
    collumn_names = []
    collumn_data = []
    for dictionary in answers:
        for i in dictionary:
            collumn_names.append(i)
            collumn_data.append(dictionary[i])

    formatted_collumn_names = ' '.join(collumn_names)
    formatted_collumn_names = ', '.join("'{}'".format(word) for word in formatted_collumn_names.split(' '))
    formatted_collumn_data = ' '.join(collumn_data)
    formatted_collumn_data = ', '.join("'{}'".format(word) for word in formatted_collumn_data.split(' '))

    return formatted_collumn_names, formatted_collumn_data


def add_feather():
    with Database_Connect('artifact.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS feather(Set_name text,'
                       ' Primary_Stat text,'
                       ' Rarity integer,'
                       ' Item_level integer,'
                       ' ATK real,'
                       ' ATKp real,'
                       ' DEF integer,'
                       ' DEFp real,'
                       ' HP integer,'
                       ' HPp real,'
                       ' ElementalMastery integer,'
                       ' EnergyRecharge real,'
                       ' CritRate real,'
                       ' CritDMG real)')

    answers = _questions_for_user('F')
    with Database_Connect('artifact.db') as connection:
        cursor = connection.cursor()
        formatted_output = _formatting_for_SQLite(answers)
        cursor.execute(f'INSERT INTO feather ({formatted_output[0]}) VALUES ({formatted_output[1]})')
#Mam stabelaryzowane main_statsy wiec bedzie zawsze mozna zrobic override user inputu

def add_goblet():
    with Database_Connect('artifact.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS goblet(Set_name text,'
                       ' Primary_Stat text,'
                       ' Rarity integer,'
                       ' Item_level integer,'
                       ' ATK real,'
                       ' ATKp real,'
                       ' DEF integer,'
                       ' DEFp real,'
                       ' HP integer,'
                       ' HPp real,'
                       ' ElementalMastery integer,'
                       ' EnergyRecharge real,'
                       ' CritRate real,'
                       ' CritDMG real)')
    answers = _questions_for_user('G')
    with Database_Connect('artifact.db') as connection:
        cursor = connection.cursor()
        formatted_output = _formatting_for_SQLite(answers)
        cursor.execute(f'INSERT INTO goblet ({formatted_output[0]}) VALUES ({formatted_output[1]})')

def add_crown():
    with Database_Connect('artifact.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS crown(Set_name text,'
                       ' Primary_Stat text,'
                       ' Rarity integer,'
                       ' Item_level integer,'
                       ' ATK real,'
                       ' ATKp real,'
                       ' DEF integer,'
                       ' DEFp real,'
                       ' HP integer,'
                       ' HPp real,'
                       ' ElementalMastery integer,'
                       ' EnergyRecharge real,'
                       ' CritRate real,'
                       ' CritDMG real)')
    answers = _questions_for_user('C')
    with Database_Connect('artifact.db') as connection:
        cursor = connection.cursor()
        formatted_output = _formatting_for_SQLite(answers)
        cursor.execute(f'INSERT INTO crown ({formatted_output[0]}) VALUES ({formatted_output[1]})')

def add_time_piece():
    with Database_Connect('artifact.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS time_piece(Set_name text,'
                       ' Primary_Stat text,'
                       ' Rarity integer,'
                       ' Item_level integer,'
                       ' ATK real,'
                       ' ATKp real,'
                       ' DEF integer,'
                       ' DEFp real,'
                       ' HP integer,'
                       ' HPp real,'
                       ' ElementalMastery integer,'
                       ' EnergyRecharge real,'
                       ' CritRate real,'
                       ' CritDMG real)')
    answers = _questions_for_user('T')
    with Database_Connect('artifact.db') as connection:
        cursor = connection.cursor()
        formatted_output = _formatting_for_SQLite(answers)
        cursor.execute(f'INSERT INTO time_piece ({formatted_output[0]}) VALUES ({formatted_output[1]})')

def add_flower():
    with Database_Connect('artifact.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS flower(Set_name text,'
                       ' Primary_Stat text,'
                       ' Rarity integer,'
                       ' Item_level integer,'
                       ' ATK real,'
                       ' ATKp real,'
                       ' DEF integer,'
                       ' DEFp real,'
                       ' HP integer,'
                       ' HPp real,'
                       ' ElementalMastery integer,'
                       ' EnergyRecharge real,'
                       ' CritRate real,'
                       ' CritDMG real)')
    answers = _questions_for_user('Fl')
    with Database_Connect('artifact.db') as connection:
        cursor = connection.cursor()
        formatted_output = _formatting_for_SQLite(answers)
        cursor.execute(f'INSERT INTO flower ({formatted_output[0]}) VALUES ({formatted_output[1]})')

def list_all_artifacts(choice):
    with Database_Connect('artifact.db') as connection:
        cursor = connection.cursor()
        if choice == 'F':
            print('Feathers: ')
            cursor.execute('SELECT * from feather')
            artifact_dictionary = [{'Set_name': row[0], 'Primary_Stat': row[1], 'Rarity': row[2], 'Item_level': row[3],
                            'ATK': row[4], 'ATKp': row[5], 'DEF': row[6], 'DEFp': row[7], 'HP': row[8], 'HPp': row[9],
                            'ElementalMastery': row[10], 'EnergyRecharge': row[11], 'CritRate': row[12],
                            'CritDMG': row[13]} for row in cursor.fetchall()]
            return artifact_dictionary
        elif choice == 'G':
            print('Goblets: ')
            cursor.execute('SELECT * from goblet')
            artifact_dictionary = [{'Set_name': row[0], 'Primary_Stat': row[1], 'Rarity': row[2], 'Item_level': row[3],
                            'ATK': row[4], 'ATKp': row[5], 'DEF': row[6], 'DEFp': row[7], 'HP': row[8], 'HPp': row[9],
                            'ElementalMastery': row[10], 'EnergyRecharge': row[11], 'CritRate': row[12],
                            'CritDMG': row[13]} for row in cursor.fetchall()]
            return artifact_dictionary
        elif choice == 'C':
            print('Crowns: ')
            cursor.execute('SELECT * from crown')
            artifact_dictionary = [{'Set_name': row[0], 'Primary_Stat': row[1], 'Rarity': row[2], 'Item_level': row[3],
                            'ATK': row[4], 'ATKp': row[5], 'DEF': row[6], 'DEFp': row[7], 'HP': row[8], 'HPp': row[9],
                            'ElementalMastery': row[10], 'EnergyRecharge': row[11], 'CritRate': row[12],
                            'CritDMG': row[13]} for row in cursor.fetchall()]
            return artifact_dictionary
        elif choice == 'T':
            print('Time pieces: ')
            cursor.execute('SELECT * from time_piece')
            artifact_dictionary = [{'Set_name': row[0], 'Primary_Stat': row[1], 'Rarity': row[2], 'Item_level': row[3],
                            'ATK': row[4], 'ATKp': row[5], 'DEF': row[6], 'DEFp': row[7], 'HP': row[8], 'HPp': row[9],
                            'ElementalMastery': row[10], 'EnergyRecharge': row[11], 'CritRate': row[12],
                            'CritDMG': row[13]} for row in cursor.fetchall()]
            return artifact_dictionary
        elif choice == 'Fl':
            print('Flowers: ')
            cursor.execute('SELECT * from flower')
            artifact_dictionary = [{'Set_name': row[0], 'Primary_Stat': row[1], 'Rarity': row[2], 'Item_level': row[3],
                            'ATK': row[4], 'ATKp': row[5], 'DEF': row[6], 'DEFp': row[7], 'HP': row[8], 'HPp': row[9],
                            'ElementalMastery': row[10], 'EnergyRecharge': row[11], 'CritRate': row[12],
                            'CritDMG': row[13]} for row in cursor.fetchall()]
            return artifact_dictionary


        print('Goblets: ')
        print('Crowns: ')
        print('Time pieces: ')
        print('Flowers: ')



DPS_related_stats = ['ATK', 'ATKp', 'ElementalMastery', 'CritRate', 'CritDMG', 'EnergyRecharge']
Base_Artifact = {
    'MainStat': ['ATK'],
    'Substat1': DPS_related_stats,
    'Substat2': DPS_related_stats[:-1],
    'Substat3': DPS_related_stats[:-2],
    'Substat4': DPS_related_stats[:-3]
}

possible_substats_feather = copy.deepcopy(Base_Artifact)
possible_substats_crown = copy.deepcopy(Base_Artifact)
possible_substats_goblet = copy.deepcopy(Base_Artifact)
possible_substats_timepiece = copy.deepcopy(Base_Artifact)
possible_substats_flower = copy.deepcopy(Base_Artifact)

possible_substats_crown['MainStat'] = ['ATKp', 'ElementalMastery', 'CritRate', 'CritDMG']
possible_substats_goblet['MainStat'] = ['ATKp', 'ElementalMastery', 'PhysDMGBonus', 'EleDMGBonus']
possible_substats_timepiece['MainStat'] = ['ATKp', 'ElementalMastery'] #Also Energy Reg but not for now
possible_substats_flower['MainStat'] = ['HP']

space_of_all_builds = [
    possible_substats_feather,
    possible_substats_crown,
    possible_substats_goblet,
    possible_substats_timepiece,
    possible_substats_flower
]
#Example build permutator

def all_of_a_kind(possibility_dictionary):
    all_item_permutatons = []
    mainlist = possibility_dictionary['MainStat']
    Sub1 = possibility_dictionary['Substat1']
    Sub2 = possibility_dictionary['Substat2']
    Sub3 = possibility_dictionary['Substat3']
    Sub4 = possibility_dictionary['Substat4']
    for a in mainlist:
        for b in Sub1:
            for c in Sub2:
                for d in Sub3:
                    for e in Sub4:
                        _temporary_artifact = (a, b, c, d, e)
                        if a == b or a==c or a==d or a==e or b==c or b==d or b==e or c==d or c==e or d==e:
                            pass
                        else:
                            all_item_permutatons.append(_temporary_artifact)

    return all_item_permutatons


def Artifact_Build_Generator():
    f = all_of_a_kind(possible_substats_feather)
    g = all_of_a_kind(possible_substats_goblet)
    c = all_of_a_kind(possible_substats_crown)
    t = all_of_a_kind(possible_substats_timepiece)
    fl = all_of_a_kind(possible_substats_flower)

    for a in f:
        for b in g:
            for C in c:
                for d in t:
                    for e in fl:
                        Combinations = {}
                        Combinations[f'feather {a}, goblet {b}, crown {C}, timepiece {d}, flower {e}']=a+b+C+d+e
                        yield Combinations


def Repeated_values():
    # Znajduje powtarzane wartosci w liscie tupli
    a = all_of_a_kind(possible_substats_feather)

    att = []
    for element in a:
        for pos in element:
           att.append(pos)

    values = collections.Counter(att)
    return values


artifact_set_bonuses4 = [
    {'name': 'Archaic Petra', 'bonus': {'Corresponding_DMG_Bonus': 50}},
    {'name': 'Berserker', 'bonus': {'CritRate': 36}}
]

possible_set_bonuses2 = []
artifact_set_bonuses2 = [('a', 'b')]