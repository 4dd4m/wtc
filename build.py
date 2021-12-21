from bs4 import BeautifulSoup as bs
from Quest import Quest
import csv, json, getQuest

def generateQuestsFile():
    getQuest.getQuestsFile()

def parseQuests() -> list:
    #quest objects
    questList = []

    #uquest csv
    quests = []

    #Parse the Wuest File
    try:
        f = open('Quest', "r")
    except FileNotFoundError:
        getQuest.getQuestsFile()
        f = open('Quest', "r")
    f = open('Quest', "r")

    soup = bs(f, 'html.parser')
    tables = soup.find_all( class_='wikitable')
    id=0

    #iterate the tables
    for table in tables:
        try:
            dealer = table.tbody.tr.th.a.text.lower()
            
        except AttributeError:
            continue
        rows = table.find_all('tr')
        rowcounter = 0
        for row in rows[2:]:
            q = None
            objectivesstring = ''
            rewardstring = ''
            if rowcounter == 0:
                ths = row.find_all('th')
                questName = row.th.a.text
                questType = ths[1].text.strip()
            else:
                questName = row.th.a.text

            ths = row.find_all('td')
            objectives = ths[0]
            rewards = ths[1]
            q = Quest(questName)
            q.addTrader(dealer)

            for reward in rewards:
                try:
                    rewardstring += reward.strip()
                    q.addRewardStr(rewards.text)
                except TypeError:
                    pass


            for objective in objectives:
                try:
                    objectivesstring += objective.strip()
                except TypeError:
                    pass

            q.addObjectiveStr(objectives.text)

            if questName not in quests:
                str = 'Quest added'
                quests.append([id,questName])
                str += (': {}'.format(questName))

            if q is not None:
                questList.append(q)
                q = None
                
            rowcounter += 1
            id+=1
            #break


    with open('quests.js', 'w', encoding="utf-8") as f:
        str = "var csv = "
        str += json.dumps(quests)
        str += ";"

        f.write(str)

    return questList

def defaultOptions() -> str: #return with the default options
    return """let options = {
    'show_quests' : true,
    'show_collector' : true,
    'show_0_remaining' : true,
    };"""

def generateItems(quests) -> dict:
    pass

if __name__ == "__main__":
    quests = parseQuests()
    for q in quests:
        print(q.itemList)
