# encrypting a message. 

code = {
"9": "0",
"3": "1",
"8": "2",
"2": "3",
"7": "4",
"6": "5",
"1": "6",
"a": "7",
"b": "8",
"c": "9",
"k": "a",
"l": "b",
"m": "c",
"n": "d",
"o": "e",
"p": "f",
"q": "g",
"r": "h",
"s": "i",
"t": "j",
"u": "k",
"v": "l",
"w": "m",
"x": "n",
"y": "o",
"z": "p",
"!": "q",
"=": "r",
"#": "s",
".": "t",
",": "u",
")": "v",
"*": "w",
"(": "x",
" ": "y",
"5": "z",
"0": "!",
"4": "=",
"d": "#",
"e": ".",
"f": ",",
"g": ")",
"h": "*",
"i": "(",
"j": " "
} 
 
s2 = ""
s1 = str(input("Enter a message to be encrypted: ").lower())

for i in range(0,len([code[str(s1[i])] for i in range(0, len(s1))])):
    s2 += [code[str(s1[i])] for i in range(0, len(s1))][i]
 
print("The encrypted message is:  " + s2 + "  .")



print("\n")
  
# decrypting a message.   
# Suppose you received a message you want to decrypt.  

t1= str(input("Enter the message to be decrypted: ").lower())
 
dual_code = dict(zip(code.values(), code.keys()))

t3 = ""

for i in range(0, len([dual_code[t1[i]] for i in range(0,len(t1))])): 
    t3 = t3 + [dual_code[t1[i]] for i in range(0,len(t1))][i]

print("The decrypted messsage is:  " + t3 + "  .")


