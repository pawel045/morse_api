from random import choice

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', '!':'-.-.--',
                    ' ':'/', }


class Alphabet:
    def __init__(self):
        self.characters = MORSE_CODE_DICT

    def get_rand_char(self):
        eng_char, morse_char = choice(list(self.characters.items()))
        return eng_char, morse_char

    def translate(self, text: str):
        text_translated = []
        for char in text:
            text_translated.append(self.characters.get(char.upper(), 'X'))

        return ' '.join(text_translated)