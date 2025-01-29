from base64 import decode

from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def cipher(sentence, shift,direction):
    try:
                a  = ""
        # if direction == "encode" or direction == "decode":
                for i in sentence:

                    if i not in alphabet:
                        a += i
                    else:
                        position = alphabet.index(i)

                    if direction == "encode":
                        newPosition = position + int(shift)
                    elif direction==None:
                        newPosition = position + int(shift)
                    elif direction=="decode":
                        newPosition = position - int(shift)

                    a = a + alphabet[newPosition]
                return a
        # else:
        #     return "enter true word"
    except UnboundLocalError as error:
        return error
    except ValueError as error2:
        return error2
is_end = True
if __name__ == '__main__':
    print(logo)
    while is_end:
        chance = input("""Enter "encode" for encoding, "decode" for decoding: """)
        sentence = input("Enter a sentence: ").lower()
        shift = int(input("Enter a shift: "))

        print(cipher(sentence,shift,chance))
        end = input("Enter 'yes' for yes and 'no' for no: ")
        if end == "no":
            is_end = False

