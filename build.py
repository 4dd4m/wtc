from bs4 import BeautifulSoup as bs
from Quest import Quest
import csv, json, getQuest, Collectibles

def generateQuestsFile():
    """This function downloads the .html from the wiki"""
    getQuest.getQuestsFile()

def parseTable(file):
    """Parse the tables from the provided file"""

    #Parse the Wuest File
    try:
        f = open(file, "r")
    except FileNotFoundError:
        getQuest.getQuestsFile()
        f = open(file, "r")
    f = open(file, "r")

    soup = bs(f, 'html.parser')
    tables = soup.find_all( class_='wikitable')
    return tables

def parseQuests(tables):
    """Parse the Quests from the provided tables"""
    #iterate the tables
    #quest objects
    questList = []
    id=0

    #uquest csv
    quests = []
    for table in tables:
        try:
            dealer = table.tbody.tr.th.a.text.lower()
        except AttributeError:
            continue

        rows = table.find_all('tr')
        rowcounter = 0
        for row in rows[2:]: #skip the table header
            q = None
            objectivesstring = ''
            rewardstring = ''
            if rowcounter == 0:
                ths = row.find_all('th')
                questName = row.th.a.text
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

    #writing the quests.js file - used to get the names from the ids
    with open('quests.js', 'w', encoding="utf-8") as f:
        str = "var csv = "
        str += json.dumps(quests)
        str += ";"
        f.write(str)

    return questList

def generateHideout(file):
    """Generating the hideout file"""
    pass

def parseHideout(tables):
    """Parsing the hideout file"""
    pass

if __name__ == "__main__":
    generateQuestsFile()
    quests = parseTable('Quest.html')
    quest = parseQuests(quests)

    str = Collectibles.generateCollectibles(quest)
    a = Collectibles.addHeader(str)
    with open('collectibles.js', 'w', encoding="utf-8") as f:
        f.write(a)
        f.close()
    print("Done")
