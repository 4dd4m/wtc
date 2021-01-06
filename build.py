from bs4 import BeautifulSoup as bs
import csv
import json

traders = ['Fence','Jaeger','Mechanic','Pacekeeper','Prapor','Ragman','Skier','Therapist']
cols = ['id','questname','type','objective','reward']
quests = []

f = open('Quest', "rb")
soup = bs(f, 'html.parser')
tables = soup.find_all( class_='wikitable')
id=0
for table in tables:
    dealer = table.tbody.tr.th.a.text

    rows = table.find_all('tr')
    rowcounter = 0
    for row in rows[2:]:
        objectivesstring = ''
        rewardstring = ''
        #print(row)
        if rowcounter == 0:
            ths = row.find_all('th')
            questName = row.th.a.text
            questType = ths[1].text.strip()
        else:
            questName = row.th.a.text


        ths = row.find_all('td')
        objectives = ths[0]
        rewards = ths[1]



        for reward in rewards:
            reward = str(reward)
            rewardstring += reward.strip()

        for objective in objectives:
            objective = str(objective)
            objectivesstring += objective.strip()
           
            
        
        
        
        




        if questName not in quests:
            quests.append([id,questName,questType,objectivesstring,rewardstring])
        #print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        rowcounter += 1
        id+=1
        #break
with open('quests.csv', 'w', encoding="utf-8") as f:
    f.write(json.dumps(quests))
