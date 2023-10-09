import ast

L1 = {}
L2 = {}
L3 = {}
L4 = {}
L5 = {}
L6 = {}
L7 = {}
with open("../text/vocabulary.txt", "r") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    line = line.strip()
    dictionary = ast.literal_eval(line)
    if i == 0:
        L1 = dictionary
    elif i == 1:
        L2 = dictionary
    elif i == 2:
        L3 = dictionary
    elif i == 3:
        L4 = dictionary
    elif i == 4:
        L5 = dictionary
    elif i == 5:
        L6 = dictionary
    elif i == 6:
        L7 = dictionary


def indonesian(L1, L2, L3, L4, L5, L6, L7):
    L1_, L2_, L3_, L4_, L5_, L6_, L7_ = L1.copy(), L2.copy(), L3.copy(), L4.copy(), L5.copy(), L6.copy(), L7.copy()
    day = int(input("Which day is it ? "))

    with open("../text/day.txt", 'w') as file:      # Remember the day
        file.write(str(day))

    if not day % 39:
        for fr in L7_.keys():
            indo = input(f'What is the translation of {fr} ? ').lower().strip()
            if indo == L7[fr].lower().strip():
                print("Bagus !")
            else:
                L1[fr] = L7[fr]
                print("Nope")
                print(L1[fr])
            del L7[fr]

    if not day % 24:
        for fr in L6_.keys():
            indo = input(f'What is the translation of {fr} ? ').lower().strip()
            if indo == L6_[fr].lower().strip():
                print("Bagus !")
                L7[fr] = indo
            else:
                L1[fr] = L6[fr]
                print("Nope")
                print(L1[fr])
            del L6[fr]

    if not day % 15:
        for fr in L5_.keys():
            indo = input(f'What is the translation of {fr} ? ').lower().strip()
            if indo == L5[fr].lower().strip():
                print("Bagus !")
                L6[fr] = indo
            else:
                L1[fr] = L5[fr]
                print("Nope")
                print(L1[fr])
            del L5[fr]

    if not day % 7:
        for fr in L4_.keys():
            indo = input(f'What is the translation of {fr} ? ').lower().strip()
            if indo == L4[fr].lower().strip():
                print("Bagus !")
                L5[fr] = indo
            else:
                L1[fr] = L4[fr]
                print("Nope")
                print(L1[fr])
            del L4[fr]

    if not day % 4:
        for fr in L3_.keys():
            indo = input(f'What is the translation of {fr} ? ').lower().strip()
            if indo == L3[fr].lower().strip():
                print("Bagus !")
                L4[fr] = indo
            else:
                L1[fr] = L3[fr]
                print("Nope")
                print(L1[fr])
            del L3[fr]

    if not day % 2:
        for fr in L2_.keys():
            indo = input(f'What is the translation of {fr} ? ').lower().strip()
            if indo == L2[fr].lower().strip():
                print("Bagus !")
                L3[fr] = indo
            else:
                L1[fr] = L2[fr]
                print("Nope")
                print(L1[fr])
            del L2[fr]

    for fr in L1_.keys():
        indo = input(f'What is the translation of {fr} ? ').lower().strip()
        if indo == L1[fr].lower().strip():
            print("Bagus !")
            del L1[fr]
            L2[fr] = indo
        else:
            print("Nope")
            print(L1[fr])
    return L1, L2, L3, L4, L5, L6, L7


if __name__ == "__main__":
    D1, D2, D3, D4, D5, D6, D7 = indonesian(L1, L2, L3, L4, L5, L6, L7)
    with open("../text/vocabulary.txt", "w") as f:
        f.write(str(L1) + "\n" + str(L2) + "\n" + str(L3) + "\n" + str(L4) + "\n" + str(L5) +
                "\n" + str(L6) + "\n" + str(L7))
