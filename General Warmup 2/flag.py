import pyperclip

val = bin(27)[2:]

print val
pyperclip.copy("picoCTF{"+str(val)+"}")