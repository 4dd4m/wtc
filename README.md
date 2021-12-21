#Tarkov What To Collect

This short javascript/python project help to keep track of all the quests and quest items in the game. The project is up to date for version: v0.12.12.2.16165, so you have nothing to do. You need to update your 'Quests.html' on any new quests released after the version mentioned above.

##How to Assemble the list (in case you want to do it yourself)
* run build.py with uncommented generateQuestsFile()
* run python Collectibles.py after you modified the two quest

##Quests needs to modify after downloading the Quest.html
* Crisis
* Acquaintance

Edit the downloaded Quest.html file and search for the two quests above. e.g. at Acquaintance quest, replace the:
* 'Find 3' to 'hand over 3'
* 'Find 2' to 'hand over 2'
* 'Find 2' to 'hand over 2'

On Crisis:
* 'Find 5' to 'hand over 5'
* 'Find 20' to 'hand over 20'

This thing is important, because the wiki is inconsistent on these quests.

##First boot
* open the index.html in your browser
* hit the reset list button to generate the initial localStorage items
* any other hit to reset list button will initialize the values, so be careful

##Import/Export
* Export button, then paste the data into a new .txt file
* Import button, copy the data from your .txt file and hit the Import button

##Todo
* further bugfixes
 
