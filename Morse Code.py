def engtomorse(txt):
    for i in txt:
        if i in code:
            print(f'{code[i]} ',end="")

def morsetoeng(txt):
    morse_to_english = {v: k for k, v in code.items()}  # Reverse code dictionary for Morse to English lookup
    words = txt.split(" ")
    for word in words:
        if word == "/":
            print(" ", end="")
        elif word in morse_to_english:
            print(morse_to_english[word], end="")
        else:
            print("Invalid Morse code:", word) #invalid morse code

txt=input("Enter message: ")
txt=txt.lower()
code={"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.","0":"-----",
      "+":".-.-.", "-":"-....-", "/":"-..-.", "=":"-...-", " ":" / "}

if txt[0] in code.keys():
    engtomorse(txt)    
else:
    morsetoeng(txt)