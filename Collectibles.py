import Quest, build, json

def generateCollectibles():
    """Generate The collectibles String"""
    questList = build.parseQuests()
    collectibleDict = {}
    header = "let items = "
    tail = ";"

    c = 0 #questid
    for q in questList:
        ##build questlist "Killa's helmet", {'amount': 1, 'ininventory': 0, 
        #'handedin': 0, 'remaining': 1, 'quest': {54: 1}}
        if len(q.itemList) > 0:
            for i,a in q.itemList.items():
                if i not in collectibleDict:
                    collectibleDict[i] = {}
                    collectibleDict[i]["amount"] = int(a)
                    collectibleDict[i]["ininventory"] = 0
                    collectibleDict[i]["handedin"] = 0
                    collectibleDict[i]["barter"] = "false"
                    collectibleDict[i]["crafted"] = "false"
                    collectibleDict[i]["remaining"] = int(a)
                    collectibleDict[i]["quest"] = {}
                    collectibleDict[i]["quest"][int(c)] = int(a)
                else:
                    collectibleDict[i]["amount"] += int(a)
                    collectibleDict[i]["ininventory"] = 0
                    collectibleDict[i]["handedin"] = 0
                    collectibleDict[i]["remaining"] += int(a)
                    collectibleDict[i]["quest"][int(c)] = int(a)
            print(q.id)
        c += 1


    return json.dumps(collectibleDict)

def addHeader(str):
    """Add a let items = { to the string"""
    options = defaultOptions()
    return "let items = " + str + ";\n" + options

def defaultOptions() -> str: #return with the default options
    return """let options = {
    'show_quests' : true,
    'show_collector' : true,
    'show_0_remaining' : true,
    };"""

if __name__ == "__main__":
    str = generateCollectibles()
    f = addHeader(str)
    print(f)
