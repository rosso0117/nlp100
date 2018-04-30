# coding: utf-8
import unicodedata

def cipher(input):
    ret = ''
    for c in input:
        c_name = unicodedata.name(c)
        if c_name.startswith('LATIN SMALL LETTER'):
            target_chord = 219 - ord(c)
            res = chr(target_chord)
        else:
            res = c
        ret += res

    return ret

str1 = "Atbash is a simple substitution cipher for the Hebrew alphabet."

str1 = cipher(str1)
print(str1)

str1 = cipher(str1)
print(str1)