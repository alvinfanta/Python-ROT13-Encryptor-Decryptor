#List for all the alphabets
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#Placeholder for letters and strings
DecryptedLetter = ""
DecryptedString = ""
#Placeholder for order of letters
LetterOrder = 0

## isalpha() = check apa itu letter
## isupper() = check apa itu uppercase

##Function Section
def convert_per_letter(ltr, DecryptedString, UL) :
    i = 0
    while ltr != alphabet[i]:
        i += 1
    else:
        i += 13
        if i > 25:
            i -= 26
        DecryptedLetter = alphabet[i]
        if UL == "u":
            return (f"{DecryptedString}{DecryptedLetter.upper()}")
        else:
            return (f"{DecryptedString}{DecryptedLetter}")

EncryptedString = input("Masukkan stringmu: ")

StringLength = len(EncryptedString)

while LetterOrder < StringLength:
    currentLetter = EncryptedString[LetterOrder]
    if currentLetter.isalpha():
        if currentLetter.isupper():
            currentLetter = currentLetter.lower()
            DecryptedString = convert_per_letter(currentLetter, DecryptedString, "u")
        else:
            DecryptedString = convert_per_letter(currentLetter, DecryptedString, "l")
    else:
        DecryptedString = f'{DecryptedString}{currentLetter}'
    print(DecryptedString)
    LetterOrder += 1

else:
    print(f"The encrypted/decrypted string is: {DecryptedString}")