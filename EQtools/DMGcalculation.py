import numpy as np
import matplotlib.pyplot as plt


def NonCriticalAttack(data_for_DMG_calculation):
    input_vector = data_for_DMG_calculation
    #vector format: [Base_ATK, ATKp, ATK, Elemental_DMG_percent, Skill_Multiplier, Character_level, Enemy_level,
    # Defence_drop, Corresponding_Enemy_Res]

    ATKp = input_vector[1] / 100
    Corresponding_DMG_Bonus = input_vector[3] / 100

    DMG = (input_vector[0] * (1 + ATKp) + input_vector[2]) * (1 + Corresponding_DMG_Bonus) * (input_vector[4]) *\
          ((100 + input_vector[5]) / ((100 + input_vector[5]) + (100 + input_vector[6]) * input_vector[7])) * \
          (1 - input_vector[8])

    # DMG = (Base_ATK * (1 + ATKp) + ATK)) * (1 + Corresponding_DMG_Bonus) * (Skill_Multiplier) *\
    #       ((100 + Character_level) / ((100 + Character_level)+ (100 + Enemy_level) * Defence_drop)) * \
    #       (1 - Corresponding_Enemy_Res)
    # A B C D E F  k
    # DMG = m_nfr (k + kA + B) * (1 + C)


    return DMG

def Av_DMG_inc_Critical_Attack(data_for_DMG_calculation, crit_info):
    # Non - CriticalDmg * (1 + (Crit Rate % * Crit DMG %))
    # Average DMG increase due to critical attack
    inDMG = NonCriticalAttack(data_for_DMG_calculation) * (1 + (crit_info[0]/100 * crit_info[1]/100))
    return inDMG


# Code for making permutations and selection of best item set.

    #vector format: [Base_ATK, ATKp, ATK, Elemental_DMG_percent, Skill_Multiplier, Character_level, Enemy_level,
    # Defence_drop, Corresponding_Enemy_Res]

# wszystko jest utaj stale poza ATKp, ATK, Elemental/Physical_DMG_percent

# Próba obliczeń analitycznych
vector_for_atk = [500, 0, 0, 0, 1, 80, 80, 0.5, 0.5]
vector_for_crit = [500, 0, 0, 0, 1, 80, 80, 0.5, 0.5]

x_axis = []
y_axis = []
y_axisr = []
y_axisd = []
y_axiscorr = []
y_axisboth = []
for a in range(0, 100, 1):
    x_axis.append(a)


    y_atk0 = Av_DMG_inc_Critical_Attack([500, a, 0, 0, 1, 80, 80, 0.5, 0.5], (0, 0))
    y_atk1 = Av_DMG_inc_Critical_Attack([500, a+1, 0, 0, 1, 80, 80, 0.5, 0.5], (0, 0))
    y_atk = ((y_atk1*100)/y_atk0)-100
    y_axis.append(y_atk)

    y_critrate0 = Av_DMG_inc_Critical_Attack([700, 0, 0, 0, 1, 80, 80, 0.5, 0.5], (a, 10))
    y_critrate1 = Av_DMG_inc_Critical_Attack([700, 0, 0, 0, 1, 80, 80, 0.5, 0.5], (a+1, 10))
    y_critrate = ((y_critrate1*100)/y_critrate0)-100
    y_axisr.append(y_critrate)

    y_critdmg0 = Av_DMG_inc_Critical_Attack([700, 0, 0, 0, 1, 80, 80, 0.5, 0.5], (10, a))
    y_critdmg1 = Av_DMG_inc_Critical_Attack([700, 0, 0, 0, 1, 80, 80, 0.5, 0.5], (10, a+1))
    y_critdmg = ((y_critdmg1*100)/y_critdmg0)-100
    y_axisd.append(y_critdmg)

    y_critboth0 = Av_DMG_inc_Critical_Attack([700, 0, 0, 0, 1, 80, 80, 0.5, 0.5], (a, a))
    y_critboth1 = Av_DMG_inc_Critical_Attack([700, 0, 0, 0, 1, 80, 80, 0.5, 0.5], (a+1, a+1))
    y_critboth = ((y_critboth1*100)/y_critboth0)-100
    y_axisboth.append(y_critboth)

    y_corrdmg0 = Av_DMG_inc_Critical_Attack([700, 0, 0, a, 1, 80, 80, 0.5, 0.5], (0, 0))
    y_corrdmg1 = Av_DMG_inc_Critical_Attack([700, 0, 0, a+1, 1, 80, 80, 0.5, 0.5], (0, 0))
    y_corrdmg = ((y_corrdmg1 * 100) / y_corrdmg0) - 100
    y_axiscorr.append(y_corrdmg)


y_sum = [x+y+z for x, y, z in zip(y_axis, y_axisr, y_axisboth)]

plt.plot(x_axis, y_axis, label="Increase per ATK% point", linestyle="-.", color="blue")
# plt.plot(x_axis, y_axisr, label="Increase per Crit Rate point (10% CritDMG)", linestyle="--")
# plt.plot(x_axis, y_axisd, label="Increase per Crit DMG point (10% CritRate)", linestyle="-.")
plt.plot(x_axis, y_axisboth, label="Increase per Crit DMG and Crit Rate point", linestyle="--")
# plt.plot(x_axis, y_axiscorr, label="Increase per Phys/Elemental DMG point", linestyle="--")
plt.plot(x_axis, y_sum, label="Suma")
dy = np.diff(y_sum)
ddy = np.diff(dy)

plt.plot(x_axis[:-1], dy, label="pierwsza pochodna")
plt.plot(x_axis[:-2], ddy, label="druga pochodna")

i = 0
possible_inflection_points = []

for _ in range(0, len(ddy)-1):
    a, b = ddy[_], ddy[_+1]
    if a*b<0:
        possible_inflection_points.append(i)
        i += 1
    else:
        i += 1

print(possible_inflection_points)
# plt.title('Procentowe zwiększanie DPS za każdy punkt w danej statystyce')
# plt.xlabel('Wartość procentowa statystyki')
# plt.ylabel('Ilość DPS uzyskiwana za 1 punkt procentowy')
# plt.xlim(-5, 100)
# plt.ylim(-0.25, 3)
plt.legend(loc='upper right')
plt.show()

def evaluation(num1, num2, num3):
  return num1 + num2 + num3

num1 = [1, 2, 3]
num2 = [3, 2, 1]
num3 = [4, 4, 4]



def selection():
    evaluated_numbers = []
    for x in num1:
      for y in num2:
        for z in num3:
            temp_data = (x, y, z)
            result = evaluation(*temp_data)
            evaluated_numbers.append({temp_data: result})
    return evaluated_numbers

#print(selection())

best_sets = []

comparison_value = 0
for dictionary in selection():
  for key in dictionary:
    value = dictionary[key]
    if value > comparison_value:
      comparison_value = value
      best_sets.clear()
      best_sets.append(dictionary)
    elif value == comparison_value:
      best_sets.append(dictionary)
    else:
      break

#print(best_sets)

"""
Logika tego kodu idzie tak:

Dodane_bonusy = Bonusy z artefaktów (feather+goblet+crown+timepiece+flower) + bonusy z broni + bonusy z setów

Bonusy z artefaktów - słownik którego kluczem jest nazwa artefaktow i które statystyki z niego pochodzą, a wartością 
tuple z ich sumą.


vector format: [Base_ATK, ATKp, ATK, Elemental_DMG_percent, Skill_Multiplier, Character_level, Enemy_level,
    # Defence_drop, Corresponding_Enemy_Res]
"""