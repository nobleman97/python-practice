


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")



def encrypt():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    crypt = ""

    for char in text:
        if char != " ":
            char_index = alphabet.index(char)

        if char == " ":
            crypt += " "
        elif char == alphabet[char_index]:
            final_pos = char_index + shift
            if final_pos > len(alphabet) - 1:
                final_pos -= (len(alphabet))
            
            result_letter = alphabet[final_pos]
            crypt += result_letter
    
    print(f"Encryption complete!\nResulting word is: {crypt}")

def decode():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    word = ""

    for char in text:
        if char != " ":
            char_index = alphabet.index(char)

        if char == " ":
            word += " "
        elif char == alphabet[char_index]:
            final_pos = char_index - shift
            if final_pos < 0:
                final_pos *= -1
                
            
            result_letter = alphabet[len(alphabet) - final_pos]
            word += result_letter
    
    print(f"Encryption complete!\nResulting word is: {word}")

if direction == 'encode':
    encrypt()
elif direction == 'decode':
    decode()