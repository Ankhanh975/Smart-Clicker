import winAPIOut
import minecraftAPI
from time import perf_counter, sleep
from random import shuffle

def __WhatToChat(numpad):
    global mode, Up_KIEM, Up_GIAP, IT_TRAP, LAY_KC

    if numpad == 0:
        return [-1]
    elif numpad == 1:
        return ["@hmm", "@v. ", "@c", "@cc?", "@?", "@v", "@:<", "@ghe vay", "@tu tu thoi"]
    elif numpad == 2:
        if LAY_KC==False:
            LAY_KC = True
            return ["ra KC di", "lay kc nha", "ra KC nhe"]
        elif Up_KIEM == False:
            return ["up KIEM pls", "up KIEM nha", "up KIEM nhe", "up KIEM pls", "up KIEM:"]
        else:
            if Up_GIAP == 3:
                return ["up GIAP IV nua"]
            elif Up_GIAP == 2:
                return ["up GIAP III nua pls", "ai lay kc up GIAP III ho"]
            else:
                return ["up GIAP pls", "up GIAP nha", "up GIAP nhe", "up GIAP di", "up GIAP pls", "up GIAP"]
    elif numpad == 3:
        if IT_TRAP == 0:
            return ["ai bed?", "ai bed?", "ai bed?", "ai bed day", "bed di nhe", "bed nha"]
        else:
            return ["v", "bed lai ", "Ai bed 1 lop nua ", "Ai bed nua di"]

    elif numpad == 4:
        return ["no qua!", "ve.", "ve", "no qua", "no", "e no qua", "no qua", "nhanh v"]
    elif numpad == 5:
        return ["@gg", "@gg", "@gg", "@GOOD GAME", "@GOOD GAME", "@good job", "@gg'", "@sorry", "@v", "@ths"]
    elif numpad == 6:
        return ["/leave"]
    elif numpad == 7:
        return ["/party invite"]
    elif numpad == 8:
        return ["/friend list"]


lastChat = ""


def WhatToChat(numpad):
    global lastChat
    all = __WhatToChat(numpad)
    shuffle(all)
    for x in all:
        any = x
        if lastChat != any:
            break
    lastChat = any
    return any


log = []
mode = "None"
Up_KIEM = False
Up_GIAP = 0
IT_TRAP = 0
LAY_KC = False

def onChatMessage(text):

    # print(text)
    global mode, Up_KIEM, Up_GIAP, IT_TRAP, LAY_KC
    log.append(text)
    if "? ??ng nh?p thành công!" in text:
        if not minecraftAPI.isFocused():
            return
        
        winAPIOut.fastclick("rbutton")
        sleep(1/60)

    elif "GoldAppleVn ?ã vào tr?n ??u" in text or "Green_Apple_Vn ?ã vào tr?n ??u" in text:
        mode = "None"

    elif "??i th?. Nâng c?p v? khí và trang b? b?ng" in text:
        if "B?o v? gi??ng c?a b?n và phá gi??ng c?a" in log[-2]:
            mode = "PLAY"
            Up_KIEM = False
            Up_GIAP = 0
            IT_TRAP = 0
            LAY_KC = False
    elif "Discord https://discord.gg/Zehw9wP" in text and len(log) > 5:
        if "Facebook" in log[-2]:
            if "MAKE 3F GREAT AGAIN" in log[-3]:
                if not minecraftAPI.isFocused():
                    return
                winAPIOut.fastclick("rbutton")
                sleep(1/60)

    elif "?ã mua Sharpened Swords" in text:
        Up_KIEM = True
    elif "?ã mua Reinforced Armor" in text:
        text = text.split("?ã mua Reinforced Armor ")
        if text == "I":
            Up_GIAP = 1
        elif text == "II":
            Up_GIAP = 2
        elif text == "III":
            Up_GIAP = 3
        elif text == "IV":
            Up_GIAP = 4

    elif "It's a trap! ?ã ???c kích ho?t!" in text:
        pass

    elif "?ã mua It's a trap!" in text:
        IT_TRAP = 1
