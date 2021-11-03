CHAT = ["ra KC di", "lay kc nhe", "ra KC nhe"]


def WhatToChat(numpad):
    if numpad == 0:
        return [-1]
    elif numpad == 1:
        return ["@hmm", "@v. ", "@c", "@cc?", "@?", "@v", "@:<", "@ghe vay", "@tu tu thoi"]
    elif numpad == 2:
        return ["up KIEM pls", "up KIEM nha", "up KIEM nhe", "up KIEM di", "up KIEM pls", "up KIEM"]
        # if LogReader.Up_KIEM == False:
        #     return ["up KIEM pls", "up KIEM nha", "up KIEM nhe", "up KIEM di", "up KIEM pls", "up KIEM"]

        # else:
        #     if LogReader.Up_GIAP == 3:
        #         return ["up GIAP IV nua"]
        #     elif LogReader.Up_GIAP == 2:
        #         return ["up GIAP III nua pls", "ai lay kc up GIAP III ho"]
        #     else:
        #         return ["up GIAP pls", "up GIAP nha", "up GIAP nhe", "up GIAP di", "up GIAP pls", "up GIAP"]
    elif numpad == 3:
        # if LogReader.ACTIVE_IT_TRAP == None:
        return ["ai bed?", "ai bed?", "ai bed?", "ai bed day", "bed di nhe", "bed nha"]
        # else:
        # return ["bed lai di", "bed 1 lop nua vcl", "bed 1 lop nua di"]

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
