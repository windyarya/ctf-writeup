# Crypto - Caesar and Disaster

## Question
After making dumb jokes about cryptography to all his classmates, clam got a cease and desist filed against him! When questioned in court, his only comment was "clam's confounding Caesar cipher creates confusing cryptographic challenges." Needless to say, the judge wasn't very happy. Clam was sentenced to 5 years of making dumb Caesar cipher challenges. Here's one of them: **sulx{klgh_jayzl_lzwjw_ujqhlgyjshzwj_kume}**.

##
I made a script to decrypt caesar cipher ciphertext
```python
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
```
Then, I found that the shift/key is 18 and the flag/plaintext is **actf{stop_right_there_cryptographer_scum}**
![Alt text](/Angstrom-2022/Crypto-Caesar%20and%20Disaster/solution.png)