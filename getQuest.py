#get Quest File

def getQuestsFile():
    from urllib.request import urlopen
    url='https://escapefromtarkov.fandom.com/wiki/Quests'
    page = urlopen(url)
    page_content = page.read().decode()
    f = open('Quest.html', 'w')
    f.write(page_content)
    f.close()
