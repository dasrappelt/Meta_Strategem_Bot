
import random
import time
from functools import wraps

# Persona
# 0 superior
# 1 confrontation
# 2 attack
# 3 confusing
# 4 gaining
# 5 desperate


def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())

    return k[v.index(max(v))]


def decide(strang):

    fit = {}

    fit[1] = calcStrategem1(strang)
    fit[12] = calcStrategem12(strang)
    fit[131] = calcStrategem131(strang)
    fit[132] = calcStrategem132(strang)
    fit[14] = calcStrategem14(strang)
    fit[15] = calcStrategem15(strang)
    fit[16] = calcStrategem16(strang)
    fit[171] = calcStrategem171(strang)
    fit[172] = calcStrategem172(strang)
    fit[173] = calcStrategem173(strang)
    fit[19] = calcStrategem19(strang)
    fit[20] = calcStrategem20(strang)
    fit[21] = calcStrategem21(strang)
    fit[22] = calcStrategem22(strang)
    fit[23] = calcStrategem23(strang)
    fit[25] = calcStrategem25(strang)
    fit[26] = calcStrategem26(strang)
    fit[27] = calcStrategem27(strang)
    fit[28] = calcStrategem28(strang)
    fit[29] = calcStrategem29(strang)
    fit[30] = calcStrategem30(strang)
    fit[31] = calcStrategem31(strang)
    fit[32] = calcStrategem32(strang)
    fit[33] = calcStrategem33(strang)
    fit[34] = calcStrategem34(strang)
    fit[36] = calcStrategem36(strang)

    KeyMaxFitness = keywithmaxval(fit)
    print("\nDie Berechnung ergab folgende Werte für die Strategeme:")
    for key, values in fit.items():
        print(key, values)

    if(fit[KeyMaxFitness] >= 0.5):
        return KeyMaxFitness

    # ERROR: Kein Strategem hat eine geeignete Fitness. Eventuell sollte etwas gewartet werden (4 Minuten Regeln in den calcStrategem Funktionen steigern Fitness)
    return -1


def isQuestion(text):
    for c in text:
        if c == "?":
            return True
    return False


def includesPersona(personaList, selfp):
    for x in personaList:
        if x == selfp:
            return True
    return False


def calcStrategem1(strang):
    if(strang.usedStrategems.count("1") == 1):
        return 0

    fitness = 0

    if(len(strang.usedStrategems) == "0"):
        fitness += .4
    try:
        if(strang.usedStrategems[-1] == "12"):
            fitness += .8
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)

    return fitness



def calcStrategem5(strang):
    if(strang.usedStrategems.count("5") == 1):
        return 0

    fitness = 0

    try:
        if(strang.usedStrategems[-1] == "7"):
            fitness += 1.5
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)

    return fitness

def calcStrategem7(strang):
    if(strang.usedStrategems.count("7") == 1):
        return 0

    fitness = 0

    if(len(strang.usedStrategems) >= "2"):
        fitness += .6

    try:
        if(strang.usedStrategems[-1] == "131" or strang.usedStrategems[-1] == "132"):
            fitness += .8
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)

    return fitness


def calcStrategem8(strang):
    if(strang.usedStrategems.count("8") == 1):
        return 0

    fitness = 0
    fitness += random.uniform(-0.2, 1.8)

    return fitness


def calcStrategem10(strang):
    if(strang.usedStrategems.count("10") == 1):
        return 0

    fitness = 0

    try:
        if(strang.usedStrategems[-1] == "14"):
            fitness += 1.4
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)

    return fitness


def calcStrategem11(strang):
    if(strang.usedStrategems.count("11") == 1):
        return 0

    fitness = 0

    try:
        if(strang.usedStrategems[-1] == "26"):
            fitness += 1.4
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)

    return fitness




def calcStrategem12(strang):
    if(strang.usedStrategems.count("12") == 1):
        return 0

    fitness = 0

    elapsed_time_s = time.time() - strang.tweets[-1].date  # time in seconds

    if(elapsed_time_s > 60 * 4):
        fitness = 1

    fitness += random.uniform(-0.2, 0.2)

    return fitness


def calcStrategem131(strang):
    if(strang.usedStrategems.count("131") == 1):
        return 0

    fitness = 0

    elapsed_time_s = time.time() - strang.tweets[-1].date  # time in seconds

    if(elapsed_time_s > 60 * 4):
        fitness = 1

    try:
        if(strang.usedStrategems[-1] == "31"):
            fitness = 1
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)

    return fitness


def calcStrategem132(strang):
    if(strang.usedStrategems.count("132") == 1):
        return 0

    fitness = 0

    elapsed_time_s = time.time() - strang.tweets[-1].date  # time in seconds

    try:
        if(strang.usedStrategems[-1] == "12" and elapsed_time_s > 60 * 4):
            fitness = 1.4

        if(strang.usedStrategems[-1] == "20"):
            fitness = 1.2

    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.5)

    return fitness


def calcStrategem14(strang):
    if(strang.usedStrategems.count("14") == 1):
        return 0

    fitness = 0

    # if(strang.tweets[-1].sentiment_pos>=2)
    # find and RT tweet mit sentiment_neg

    return fitness


def calcStrategem15(strang):
    if(strang.usedStrategems.count("15") == 1):
        return 0

    fitness = 0

    # if(SPELLCHECK == false):
    # fitness+=1.5

    fitness += random.uniform(-0.2, 0.4)  # 0.4 als hoher random weil tendentiell immer anwendbar

    return fitness


def calcStrategem16(strang):
    if(strang.usedStrategems.count("16") == 1):
        return 0

    fitness = 0

    try:
        if(strang.usedStrategems[-1] == "9" and strang.usedStrategems[-2] == "171"):
            fitness = 1.5
    except (IndexError, ValueError):
        pass

    return fitness


def calcStrategem171(strang):
    if(strang.usedStrategems.count("171") == 1):
        return 0

    fitness = 0

    if(len(strang.tweets) == 1):  # als antwort auf ersten tweet sehr gut
        fitness += 1.3

    try:
        if(strang.usedStrategems[-1] == "27"):
            fitness += 1.3
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)

    return fitness


def calcStrategem172(strang):
    if(strang.usedStrategems.count("172") == 1):
        return 0

    fitness = 0
    try:

        if(strang.usedStrategems[-1] == "21"):
            fitness += 1.3

    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)

    return fitness


def calcStrategem173(strang):
    if(strang.usedStrategems.count("173") == 1):
        return 0

    fitness = 0

    try:
        if(strang.usedStrategems[-1] == "9" and strang.usedStrategems[-2] == "171"):
            fitness += 1.5
    except (IndexError, ValueError):
        pass

    if(len(strang.tweets) == 1):
        fitness += 1.5

    if(strang.tweets[-1].sentiment_neg > 2):
        fitness += 1.5

    fitness += random.uniform(-0.2, 0.2)

    return fitness


def calcStrategem19(strang):
    if(strang.usedStrategems.count("19") == 1):
        return 0

    fitness = 0

    if(strang.tweets[-1].sentiment_neg > 2):
        fitness += 1.5

    if(len(strang.tweets) > 5):
        fitness += 1.5

    fitness += random.uniform(-0.2, 0.5)  # immer!

    return fitness


def calcStrategem20(strang):
    if(strang.usedStrategems.count("20") == 1):
        return 0

    fitness = 0

    if(len(strang.tweets) == 1):
        fitness += 1.5
        fitness += random.uniform(-0.4, 0.4)  # immer!

    return fitness


def calcStrategem21(strang):
    if(strang.usedStrategems.count("21") == 1):
        return 0

    fitness = 0

    try:
        if(strang.usedStrategems[-1] == "26"):
            fitness += 1
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.4)  # immer!

    return fitness


def calcStrategem22(strang):
    if(strang.usedStrategems.count("22") == 1):
        return 0

    fitness = 0

    if(len(strang.tweets) == 1):
        fitness += 1
        fitness += random.uniform(-0.2, 0.4)  # immer!

    return fitness


def calcStrategem23(strang):
    if(strang.usedStrategems.count("23") == 1):
        return 0

    fitness = 0

    try:
        if(strang.usedStrategems[-1] == "27"):
            fitness += 1.5
            fitness += random.uniform(-0.2, 0.4)

        if(strang.usedStrategems[-1] == "29"):
            fitness += 1.5
            fitness += random.uniform(-0.2, 0.4)
    except (IndexError, ValueError):
        pass

    return fitness


def calcStrategem25(strang):
    if(strang.usedStrategems.count("25") == 1):
        return 0

    fitness = 0

    try:
        if(strang.usedStrategems[-1] == "13"):
            fitness += 1.5
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.4)  # immer!

    return fitness


def calcStrategem26(strang):
    if(strang.usedStrategems.count("26") == 1):
        return 0

    fitness = 0

    if(len(strang.tweets) == 1):
        fitness += 1.5

    fitness += random.uniform(-0.2, 0.4)  # immer!

    return fitness


def calcStrategem27(strang):
    if(strang.usedStrategems.count("27") == 1):
        return 0

    fitness = 0

    try:
        if(includesPersona(strang.involvedCharacters, "timlandich") is False):  # wenn dieser bot noch nicht im strang aktiv ist
            if(strang.tweets[-1].sentiment_neg > 2):
                fitness = 1.5
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)  # immer!

    return fitness


def calcStrategem28(strang):

    # Doppelpost: Frage stellen, auf Antwort warten, haha das stellst du dir zu einfach vor
    # Aufteilen in 281("Kannst du das noch einmal erkl�ren?") und 282("Haha")

    return 0


def calcStrategem29(strang):
    if(strang.usedStrategems.count("29") == 1):
        return 0

    fitness = 0

    if len(strang.tweets) == 1:
        fitness += 1.2

    try:
        if strang.usedStrategems[-1] == "10" or strang.usedStrategems[-1] == "16":
            if time.date() - strang.tweets[-1].date > 4 * 60:
                fitness += 1.5
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)

    return fitness


def calcStrategem30(strang):
    if strang.usedStrategems.count("30") == 1:
        return 0

    fitness = 0

    try:
        if isQuestion(strang.tweets[-1].text):
            fitness += 1.5
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)

    return fitness


def calcStrategem31(strang):
    if strang.usedStrategems.count("31") == 1:
        return 0

    fitness = 0

    try:
        if strang.usedStrategems[-1] == "26":
            fitness += 1.5
    except (IndexError, ValueError):
        pass

    fitness += len(strang.tweets) / 10  # wahrscheinlicher, je länger die Diskussion

    fitness += random.uniform(-0.2, 0.5)  # immer!

    return fitness


def calcStrategem32(strang):
    if strang.usedStrategems.count("32") == 1:
        return 0

    fitness = 0

    try:
        if strang.usedStrategems[-1] == "26":
            fitness += 1.2
    except (IndexError, ValueError):
        pass

    fitness += len(strang.tweets) / 10  # wahrscheinlicher, je länger die Diskussion
    fitness += random.uniform(-0.2, 0.5)  # immer!

    return fitness


def calcStrategem33(strang):
    if strang.usedStrategems.count("33") == 1:
        return 0

    fitness = 0

    try:
        if strang.usedStrategems[-1] == "7":
            fitness += 1.2
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)

    return fitness


def calcStrategem34(strang):
    if strang.usedStrategems.count("34") == 1:
        return 0

    fitness = 0

    try:
        if strang.usedStrategems[-1] == "19":
            fitness += 1.5

        if strang.usedStrategems[-1] == "131" and strang.usedStrategems[-2] == "31":
            fitness += 2
    except (IndexError, ValueError):
        pass

    fitness += random.uniform(-0.2, 0.2)

    return fitness


def calcStrategem36(strang):
    if strang.usedStrategems.count("36") == 1:
        return 0

    fitness = 0

    fitness += len(strang.tweets) / 10  # wahrscheinlicher, je länger die Diskussion
    fitness += random.uniform(-0.2, 0.5)  # immer!

    return fitness
