import pyperclip

val = chr(int("41",16))

print val
pyperclip.copy("picoCTF{"+str(val)+"}")