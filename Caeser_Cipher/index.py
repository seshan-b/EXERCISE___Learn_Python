# Imports
from logo import start_logo


# Display Logo
print(start_logo)


# The Letter to scramble
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_amount 
                end_text += alphabet[new_position]
            elif cipher_direction == "decode":
                 new_position = position - shift_amount
                 end_text += alphabet[new_position]
        else:
            end_text += char
        print(f"The {cipher_direction} is  {end_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift % 26
    
    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    
    should_continue = False