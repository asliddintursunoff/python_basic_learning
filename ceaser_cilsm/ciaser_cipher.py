from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def cipher(sentence, shift,direction):
    a  = ""
    for i in sentence:
        if i not in alphabet:
            a += i
        else:
            position = alphabet.index(i)

        if direction == "encode":
            newPosition = position + shift
        else:
            newPosition = position - shift
        a = a + alphabet[newPosition]
    print(a)
is_end = True
while is_end:
    chance = input("""Enter "encode" for encoding, "decode" for decoding: """)
    sentence = input("Enter a sentence: ").lower()
    shift = int(input("Enter a shift: "))

    cipher(sentence,shift,chance)
    end = input("Enter 'yes' for yes and 'no' for no: ")
    if end == "no":
        is_end = False

