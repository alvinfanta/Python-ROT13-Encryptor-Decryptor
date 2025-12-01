
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encryptedLetter = ""

## isalpha() = check apa itu letter
## isupper() = check apa itu uppercase

def convert_per_letter(ltr) :
    i = 0
    while ltr != alphabet[i]:
        i += 1
    else:
        print(f'{ltr} adalah huruf ke {i+1}!')
        i += 13
        if i > 25:
            i -= 26
        encryptedLetter = alphabet[i]
        print(f'Encypted letter: {encryptedLetter}')

letter = input("Masukkan hurufmu: ")

convert_per_letter(letter)