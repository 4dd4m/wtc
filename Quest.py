import re

class Item:
    amount = 0

    def __init__(self, pName):
        self.name = pName

    def addAmount(self, pAmount):
        self.amount += pAmount

class Quest:
    _id = 0

    hiddenQuests = ['hidden quest']

    def __init__(self, pName):
        self.name = pName.lower()
        self.questItems = {}
        self.trader = ""
        self.hidden = False
        self.setHidden()
        self.itemList = {}
        self.objectiveStr = ""
        self.rewardStr = ""
        Quest._id += 1
        self.id = Quest._id

    def parseItems(self):
        exp = r'(Hand over|Handover|hand over) ([\d\,]*) (.*) to'
        result  = re.findall(exp,self.objectiveStr)
        if len(result) > 0:
            for i in result:
                amount = i[1]
                item = i[2]
                if i is not None:
                    if item not in self.itemList.keys():
                       amount = amount.replace("(","")
                       amount = amount.replace(")","")
                       amount = amount.replace(",","")
                       self.itemList[item] = amount

    def showItemList(self):
        if len(self.itemList.keys()) == 0:
            pass
        else:
            print(self.itemList)

    def setHidden(self):
        if self.name in self.hiddenQuests:
            self.hidden = True

    def isHidden(self):
        return self.hidden

    def addObjectiveStr(self, pObj):
        if pObj is not None:
            self.objectiveStr = pObj
            self.parseItems()
        else:
            raise Exception("Invalid Objectives")

    def addRewardStr(self, pRew):
        if pRew is not None:
            self.rewardStr = pRew
        else:
            raise Exception("Invalid Objectives")

    def printObjectiveString(self):
        print(self.objectiveStr)

    def addTrader(self, pTrader):
        traderList = ["prapor","therapist", "peacekeeper","skier",
                      "mechanic","ragman","jaeger","fence"]

        if pTrader in traderList:
            self.trader = pTrader
        else:
            raise Exception("This trader is not exists: " + pTrader)

    def getItemList(self):
        if len(self.itemList) >= 1:
            for k,v in self.itemList.items():
                if k is not None and v is not None:
                    print(k + v)

    def __str__(self):
        return "Quest: " + self.name.capitalize() + "\nTrader: " + self.trader.capitalize() + "\nObjectiveStr: " + self.objectiveStr
