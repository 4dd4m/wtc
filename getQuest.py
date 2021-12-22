#get Quest File

def getQuestsFile():
    """Get the wiki page"""
    from urllib.request import urlopen
    url='https://escapefromtarkov.fandom.com/wiki/Quests'
    page = urlopen(url)
    page_content = page.read().decode()
    f = open('Quest.html', 'w')
    page_content = fixUp(page_content)
    f.write(page_content)
    f.close()

def fixUp(source):
    """Fix up the Acquaintance and The Crisis quest"""

    #Crisis quest
    source = source.replace('<ul><li>Find 5 <a href="/wiki/Portable_defibrillator" title="Portable defibrillator">Portable defibrillator</a>','<ul><li>Hand over 5 <a href="/wiki/Portable_defibrillator" title="Portable defibrillator">Portable defibrillator to</a>')
    source = source.replace('<li>Find 5 <a href="/wiki/Ophthalmoscope" title="Ophthalmoscope">Ophthalmoscope</a>','<li>Hand over 5 <a href="/wiki/Ophthalmoscope" title="Ophthalmoscope">Ophthalmoscope to</a>')
    source = source.replace('<li>Find 5 <a href="/wiki/LEDX_Skin_Transilluminator" title="LEDX Skin Transilluminator">LEDX Skin Transilluminator</a>','<li>Hand over 5 <a href="/wiki/LEDX_Skin_Transilluminator" title="LEDX Skin Transilluminator">LEDX Skin Transilluminator to</a>')
    source = source.replace('<li>Find 20 <a href="/wiki/Pile_of_meds" title="Pile of meds">Pile of meds</a>','<li>Hand over 20 <a href="/wiki/Pile_of_meds" title="Pile of meds">Pile of meds to</a>')

    #Acquaintance quest
    source = source.replace('<ul><li>Find 3 <a href="/wiki/Iskra_ration_pack" title="Iskra ration pack">Iskra ration pack</a>','<ul><li>Hand over 3 <a href="/wiki/Iskra_ration_pack" title="Iskra ration pack">Iskra ration pack to</a>')
    source = source.replace('<li>Find 2 <a href="/wiki/Emelya_rye_croutons" title="Emelya rye croutons">Emelya rye croutons</a>','<li>Hand over 2 <a href="/wiki/Emelya_rye_croutons" title="Emelya rye croutons">Emelya rye croutons to</a>')
    source = source.replace('<li>Find 2 <a href="/wiki/Large_can_of_beef_stew" title="Large can of beef stew">Large can of beef stew</a>','<li>Hand over 2 <a href="/wiki/Large_can_of_beef_stew" title="Large can of beef stew">Large can of beef stew to</a>')
    return source
