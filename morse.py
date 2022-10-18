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

    def encrypt(self, text: str):
        text_translated = []
        for char in text:
            text_translated.append(self.characters.get(char.upper(), 'X'))

        return ' '.join(text_translated)

    def decrypt(self, text: str):
        text_is_correct = True
        special_char = ' /.-'

        for i in text:
            if i in special_char:
                pass
            else:
                text_is_correct = False
                break

        if text_is_correct:
            text_translated = []
            separate_characters = text.split()
            for char in separate_characters:
                a = [i for i in self.characters if self.characters[i] == char]

                if a:
                    text_translated.append(str(a[0]))
                else:
                    text_translated.append('_')

            return ''.join(text_translated)

        else:
            return False
