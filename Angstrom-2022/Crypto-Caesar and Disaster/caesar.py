# def encrypt(text, s):
#     result = ""
 
#     for i in range(len(text)):
#         char = text[i]
#         if (char.isupper()):
#             result += chr((ord(char) + s - 65) % 26 + 65)
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97) 
#     return result

def decrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - 65 - s) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) - 97 - s) % 26 + 97)
        else:
            result += char
    return result

ciphertext = "sulx{klgh_jayzl_lzwjw_ujqhlgyjshzwj_kume}"
# Bruteforce to find shift

for i in range(26):
    res = decrypt(ciphertext, i)
    if res.startswith("actf"):
        print(res)
        print(i)
        exit()