#Model M3



rotorI = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

rotorII = "AJDKSIRUXBLHWTMCQGZNPYFVOE"

rotorIII = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

rotorIV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"

rotorV = "VZBRGITYUPSDNHLXAWMJQOFECK"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plain_text = "HELLOTHERE"



rotorI_turn = 17

rotorII_turn = 5

rotorIII_turn = 22

rotorIV_turn = 10

rotorV_turn = 0



rotor1_turn = rotorI_turn

rotor2_turn = rotorII_turn

rotor3_stored = 0



reflector = "B"



rotor1_arr = list(rotorI)

rotor2_arr = list(rotorII)

rotor3_arr = list(rotorIII)

alphabet_arr = list(alphabet)

plain_text_arr = list(plain_text)

plain_text_len = len(plain_text)



rot_shift_1 = 0

rot_shift_2 = 0

rot_shift_3 = 0



rot_ring_1 = 1

rot_ring_2 = 0

rot_ring_3 = 0







def reflectorB(x):

    if x == "A":

        x = "Y"

    elif x == "Y":

        x = "A"

    elif x == "B":

        x = "R"

    elif x == "R":

        x = "B"

    elif x == "C":

        x = "U"

    elif x == "U":

        x = "C"

    elif x == "D":

        x = "H"

    elif x == "H":

        x = "D"

    elif x == "E":

        x = "Q"

    elif x == "Q":

        x = "E"

    elif x == "F":

        x = "S"

    elif x == "S":

        x = "F"

    elif x == "G":

        x = "L"

    elif x == "L":

        x = "G"

    elif x == "I":

        x = "P"

    elif x == "P":

        x = "I"

    elif x == "J":

        x = "X"

    elif x == "X":

        x = "J"

    elif x == "K":

        x = "N"

    elif x == "N":

        x = "K"

    elif x == "M":

        x = "O"

    elif x == "O":

        x = "M"

    elif x == "T":

        x = "Z"

    elif x == "Z":

        x = "T"

    elif x == "V":

        x = "W"

    elif x == "W":

        x = "V"

    

    return x



def reflectorC(x):

    if x == "A":

        x = "F"

    elif x == "F":

        x = "A"

    elif x == "B":

        x = "V"

    elif x == "V":

        x = "B"

    elif x == "C":

        x = "P"

    elif x == "P":

        x = "C"

    elif x == "D":

        x = "J"

    elif x == "J":

        x = "D"

    elif x == "E":

        x = "I"

    elif x == "I":

        x = "E"

    elif x == "G":

        x = "O"

    elif x == "O":

        x = "G"

    elif x == "H":

        x = "Y"

    elif x == "Y":

        x = "H"

    elif x == "K":

        x = "R"

    elif x == "K":

        x = "R"

    elif x == "L":

        x = "Z"

    elif x == "Z":

        x = "L"

    elif x == "M":

        x = "X"

    elif x == "X":

        x = "M"

    elif x == "N":

        x = "W"

    elif x == "W":

        x = "N"

    elif x == "T":

        x = "Q"

    elif x == "Q":

        x = "T"

    elif x == "S":

        x = "U"

    elif x == "S":

        x = "U"

    return x







#Initialize Shifts on Rotors

def ini_shift_1(x):

    if x >= 26:

        x -= 26

    global rot_shift_1

    rot_shift_1 += x



def ini_shift_2(x):

    if x >= 26:

        x -= 26

    global rot_shift_2

    rot_shift_2 += x



def ini_shift_3(x):

    if x >= 26:

        x -= 26

    global rot_shift_3

    rot_shift_3 += x





#Function for getting index number for letter

def num_value(x):

    count = 0

    letter_val = 0

    while x != alphabet_arr[count]:

        count += 1

        letter_val += 1

    return letter_val



def num_value_1(x):

    count = 0

    letter_val = 0

    while x != rotor1_arr[count]:

        count += 1

        letter_val += 1

    return letter_val



def num_value_2(x):

    count = 0

    letter_val = 0

    while x != rotor2_arr[count]:

        count += 1

        letter_val += 1

    return letter_val



def num_value_3(x):

    count = 0

    letter_val = 0

    while x != rotor3_arr[count]:

        count += 1

        letter_val += 1

    return letter_val



def shift_1():

    global rot_shift_1

    global rot_shift_2

    global rot_shift_3

    global rotor3_stored

    rot_shift_1 += 1

    if rot_shift_1 == 26:

        rot_shift_1 = 0

    if rotor3_stored == 1:

        shift_3()

        rot_shift_2 += 1

        rotor3_stored = 0

    elif rot_shift_1 == rotor1_turn:

        shift_2()

    



def shift_2():

    global rot_shift_2

    global rot_shift_3

    global rotor3_stored

    rot_shift_2 += 1


    if rot_shift_2 == 26:

        rot_shift_2 = 0

    if rot_shift_2 == rotor2_turn - 1:



        rotor3_stored += 1





def shift_3():

    global rot_shift_3

    rot_shift_3 += 1

    if rot_shift_3 == 26:

        rot_shift_3 = 0







#Getting index number for encrypted letter

def rotor1(x):

    if x >= 26:

        x -= 26

    x = rotor1_arr[x]

    x = num_value(x)

    return x





def rotor2(x):

    if x >= 26:

        x -= 26

    x = rotor2_arr[x]

    x = num_value(x)

    return x





def rotor3(x):

    if x >= 26:

        x -= 26

    x = rotor3_arr[x]

    x = num_value(x)

    return x



#Encryption for individual rotors

def rotor1_encrypt(x):

    global rot_shift_1

    rot_num_val = 0

    #print(rot_shift_1, "RotShift1")

    rot_num_val = num_value(x) + rot_shift_1

    char = rotor1(rot_num_val)

    encrypted_char = alphabet_arr[char - rot_shift_1]

    return encrypted_char



def rotor2_encrypt(x):

    global rot_shift_1

    global rot_shift_2

    global rot_shift_3

    rot_num_val = 0

    rot_num_val = num_value(x) + rot_shift_2

    char = rotor2(rot_num_val)

    encrypted_char = alphabet_arr[char - rot_shift_2]

    return encrypted_char



def rotor3_encrypt(x):

    global rot_shift_2

    global rot_shift_3

    rot_num_val = 0

    rot_num_val = num_value(x) + rot_shift_3

    char = rotor3(rot_num_val)

    encrypted_char = alphabet_arr[char - rot_shift_3]

    return encrypted_char



def rotor1_encrypt_ref(x):

    rot_num_val = 0

    rot_num_val = num_value(x) + rot_shift_1

    if rot_num_val >= 26:

        rot_num_val -= 26

    rot_num_val = alphabet_arr[rot_num_val]

    rot_num_val = num_value_1(rot_num_val) 

    encrypted_char = alphabet_arr[rot_num_val - rot_shift_1]

    #print(encrypted_char)

    return encrypted_char



def rotor2_encrypt_ref(x):

    rot_num_val = 0

    rot_num_val = num_value(x) + rot_shift_2

    if rot_num_val >= 26:

        rot_num_val -= 26

    rot_num_val = alphabet_arr[rot_num_val]

    rot_num_val = num_value_2(rot_num_val) 

    encrypted_char = alphabet_arr[rot_num_val - rot_shift_2]

    #print(encrypted_char)

    return encrypted_char



def rotor3_encrypt_ref(x):

    global rot_shift_2

    global rot_shift_3

    rot_num_val = 0

    rot_num_val = num_value(x) + rot_shift_3

    if rot_num_val >= 26:

        rot_num_val -= 26



    rot_num_val = alphabet_arr[rot_num_val]

    rot_num_val = num_value_3(rot_num_val) 

    encrypted_char = alphabet_arr[rot_num_val - rot_shift_3]


    return encrypted_char







#Final Encrypt

def encrypt(x):

    global reflector

    global rot_shift_1

    global rot_shift_2

    global rot_shift_3

    shift_1() 

    x = rotor1_encrypt(x)

    print(x, "1")

    x = rotor2_encrypt(x)

    print(x, "2")

    x = rotor3_encrypt(x)

    print(x, "3")

    if reflector == "B":

        x = reflectorB(x)

    elif reflector == "C":

        x = reflectorC(x)

    print(x, "4")

    x = rotor3_encrypt_ref(x)

    print(x, "5")

    x = rotor2_encrypt_ref(x)

    print(x, "6")

    x = rotor1_encrypt_ref(x)

    print(x, "7")

    return x

#ini_shift_3(1)







def main():

    final_encrypt=""

    for counter in range(0, plain_text_len):

        enc_char = encrypt(plain_text_arr[counter])

        final_encrypt += enc_char

    print("The final encrypt is", final_encrypt)









main()





print(rot_shift_1)

print(rot_shift_2)

print(rot_shift_3)
