from bs4 import BeautifulSoup as bs
from Quest import Quest
import csv
import json


#get Quest File
from urllib.request import urlopen
url='https://escapefromtarkov.fandom.com/wiki/Quests'
page = urlopen(url)
page_content = page.read().decode()
f = open('Quest', 'w')
f.write(page_content)
f.close()

questList = []

traders = ['Fence','Jaeger','Mechanic','Pacekeeper','Prapor','Ragman','Skier','Therapist']
cols = ['id','questname','type','objective','reward']
quests = []

#Parse the Wuest File
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
                q.addObjectiveStr(objectives.text)
            except TypeError:
                pass

        if questName not in quests:
            str = 'Quest added'
            quests.append([id,questName,questType,objectivesstring,rewardstring])
            str += (': {}'.format(questName))
    

        if q is not None:
            questList.append(q)
            q = None
            
        rowcounter += 1
        id+=1
        #break
    
with open('quests.csv', 'w', encoding="utf-8") as f:
    f.write(json.dumps(quests))
