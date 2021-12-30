
from typing import List, Union

MAGIC_NUMBER = 96

SECRET_KEY = "kryptos"
PUBLIC_KEY = "palimpsest"

def alphabetical_transposition(to_transform: Union[str,List[int]], number_to_letter:bool = False) -> List[int]:
    
    if number_to_letter:
        return [chr(letter +  MAGIC_NUMBER) for letter in to_transform]
    
    return [ord(letter) - MAGIC_NUMBER for letter in to_transform.lower()]

def alphabet_numbers() -> List[int]:
    
    magic_phrase_numbers = alphabetical_transposition(SECRET_KEY)
    alphabet_without_magic_phrase = []
    for i in range(1,27):
        if not i in magic_phrase_numbers:
            alphabet_without_magic_phrase.append(i)

    new_alphabet = magic_phrase_numbers + alphabet_without_magic_phrase
    return new_alphabet

def clean_str(dirty_str:str) -> str:
    return dirty_str.replace(" ","").lower()

# EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD
# EMUFPHZLRFAXYUS

def main(phrase:str, action:int):

    alphabet = alphabet_numbers()
    ret = []
    
    for index, phrase_letter in enumerate(phrase):
        
        phrase_letter_number = alphabetical_transposition(phrase_letter)[0]
        index = index % len(PUBLIC_KEY) if index > len(PUBLIC_KEY) - 1 else index
        public_list = list(PUBLIC_KEY)
        public_index_letter = public_list[index]
        public_index_transposition = alphabetical_transposition(public_index_letter)[0]
        
        alphabet_index = alphabet.index(public_index_transposition)
        index_numeric_alphabet = alphabet[alphabet_index:] + alphabet[:alphabet_index]
        index_alphabet = alphabetical_transposition(index_numeric_alphabet,True)

        if action == 1:
            encrypted_index = alphabet.index(phrase_letter_number)
            ret.append(index_alphabet[encrypted_index])
        else:
            encrypted_index = index_alphabet.index(phrase_letter)
            decripted_letter = alphabetical_transposition([alphabet[encrypted_index]], True)[0]
            ret.append(decripted_letter)
    
    return "".join(ret)

dirty_phrase = input("digite a frase que deseja encriptar: ")

action = input("1 para criptografar e 2 para decriptografar:  ")

while action != "1" and action != "2":
    action = input("1 para criptografar e 2 para decriptografar:  ")


phrase = clean_str(dirty_phrase)     

final_result = main(phrase,int(action))

print(final_result)