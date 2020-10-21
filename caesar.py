# substitute PLAIN the letter
PLAIN = "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT."

for i in range(26):
    KEY = i
    enc = ""

    for char in list(PLAIN):
        ASCII = ord(char)
        if (ASCII == 32):                   # if ASCII is SPC, make space.
            enc += " "
            continue
        if (122 >= ASCII and ASCII >= 97):  # if ASCII is lower
            num = ASCII - 97
            num = (num + KEY) % 26
            ASCII = num + 97
            enc += chr(ASCII)
        elif (90 >= ASCII and ASCII >= 65): # if ASCII is upper
            num = ASCII - 65
            num = (num + KEY) % 26
            ASCII = num + 65
            enc += chr(ASCII)
        else :                              # if ASCII is symbol
            enc += chr(ASCII)

    print(f"--------- Shifted {i} character ---------")
    print(enc)
    print("")