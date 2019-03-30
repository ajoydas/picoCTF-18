import base64

import pyperclip

val = base64.b64decode("dGg0dF93NHNfczFtcEwz")

print val
pyperclip.copy("picoCTF{"+str(val)+"}")