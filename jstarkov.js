function init(){
    //if there is valid data in the local storage pull it in
    if(localStorage.getItem('collectibles') != undefined){;
        items = JSON.parse(localStorage.getItem('collectibles'));
        options = JSON.parse(localStorage.getItem('options'));
    }else{
        //otherwise set up
        localStorage.setItem('collectibles', JSON.stringify(items));
        localStorage.setItem('options', JSON.stringify(options));
        items = JSON.parse(localStorage.getItem('collectibles'));
        options = JSON.parse(localStorage.getItem('options'));
    }

    //checking the boxes 
    if(options.show_quests == true){
        $('#show_quests').attr('checked',true);
    }else{
        $('#show_quests').removeAttr('checked',false);
    }
    if(options.show_collector == true){
        $('#show_collector').attr('checked',true);
    }else{
        $('#show_collector').removeAttr('checked',false);
    }
    if(options.show_0_remaining == true){
        $('#show_0_remaining').attr('checked',true);
    }else{
        $('#show_0_remaining').removeAttr('checked',false);
    }
}
init(); //run the init


//build quests table
var HTML = '';
HTML += "<tr><th>id</th><th>Quest Name</th><th>Type</th><th>Objectives</th><th>Rewards</th></tr>";

for (let index = 0; index < csv.length; index++) {
    const element = csv[index];
    HTML += ('<tr><td>'+csv[index][0]+'</td><td>'+csv[index][1]+'</td><td>'+csv[index][2]+'</td><td>'+csv[index][3]+'</td><td>'+csv[index][4]+'</td></tr>');
}
$('.quests').html(HTML);

//build collectibles table
var HTML = '';
HTML += "<tr style='font-align: center;'><th style='width: 350px;'>Item name (<span class='glyphicon glyphicon-ok'></span> FIR | "
    + "<span class='glyphicon glyphicon-cog'></span> CanBeCrafted | <span class='glyphicon glyphicon-refresh'></span> Barter)</th>"
    + "<th style='width: 20px;'>Need</th><th style='width: 110px;'>Stashed</th><th style='width: 110px;'>Handed In</th><th  style='width: 180px;'>Remaining</th></tr>";
trid=1;
for (const key in items){ //items == localstorage.items
    const element = items[key];

    if(element.remaining >= 1 || options.show_0_remaining == true){ 
        //display the row if show0 = true or ramaning > 1


        if(element.remaining <= 0){//setup the background
            background = 'style="background: #333300;"';
        }else{
            background = 'style="background: transparent;"';
        }

        if(options.show_collector == false && 229 in element.quests){
            continue; //skip the collector quest
        }else{
            icon = "";
            if(element.inraid == true){
                icon += '<span class="glyphicon glyphicon-ok" style="margin-left:10px;"></span>';
            }
            if(element.barter == true){
                icon += '<span class="glyphicon glyphicon-refresh" style="margin-left:10px;"></span>';
            }
            if(element.crafted == true){
                icon += '<span class="glyphicon glyphicon-cog" style="margin-left:10px;"></span>';
            }

            //single table row
            HTML += "<tr " + background + "><td>"
                + "<a href='https://escapefromtarkov.gamepedia.com/" + key + "'>" +key + "</a>" + icon 
                + "</span></td><td><span id='tocollect_" + key.replace(/ /g, "_")+"'>"
                + element.amount + "</span></td>" 
                + "<td>" + haveinInvInput(key) + "</td>"
                + "<td>" + handedInInput(key) + "</td>"
                + "</td><td><span id='remaining_" + key.replace(/ /g, "_") + "'>"+ element.remaining +"</span></td></tr>";
            trid++;

            questId = element.quests; // quests : {}

            if(options.show_quests == true){ //display the quests
                for(var key2 in questId){
                    HTML += `<tr ` + background+
                        `><td><span style='margin-left:120px;'><a href='https://escapefromtarkov.gamepedia.com/`+ csv[key2][1] +  `'>` + csv[key2][1] + `</a></span><td>` + questId[key2]+ `</td></td>`
                        + `<td></td>`
                        + `<td></td>`;

                    if(element.remaining <= 0){
                        HTML += `<td></td>`;

                    }else{
                        HTML += `<td><button type='button' class='btn btn-primary btn-sm' id='completebutton_`+key2.replace(/ /g, "_")
                            + `' onClick='javascript:markAsCompleteQuest(`+key2+`);'>Marked quest as complete</button></td>` 

                    }
                        + `</tr>`;
                    trid++;
                }
            }

        }
    }
}
$('.itemstocollect').html(HTML);


//input field for inventory
function haveinInvInput(key){
    return `<div class='input-group' style='text-align: center;'>
  <div class='input-group-btn'>
    <!-- Buttons -->
  </div>
  <input type="number" style='width: 100px;' id="haveinInv_`
        + key.replace(/ /g, "_")
        +`" name="haveInInv" step="1" size="8" min="0" value="` 
        + items[key].ininventory
        +`" onChange="javascript:updateItemCount('`+ key.replace(/ /g, "_")+`');"></div>`;
}

//input field for handed in 
function handedInInput(key){
    return `<div class='input-group' style='text-align: center;'>
  <div class='input-group-btn'>
    <!-- Buttons -->
  </div>
  <input type="number" style='width: 100px;' size="8" id="handedIn_` + key.replace(/ /g, "_") 
        +`"  name="handedIn" step="1" min="0" value="` + items[key].handedin 
        + `" onChange="javascript:updateItemCount('`+ key.replace(/ /g, "_") +`');">
</div>`;
}

function updateItemCount(id){
    itemid = id.replace(/_/g, " ");
    console.log(id);
    console.log(items[itemid]);

    id_handedin  = "#handedIn_" + id;
    handedin = $(id_handedin).val();

    id_haveininv = "#haveinInv_" + id;
    haveininv = $(id_haveininv).val();

    console.log(handedin);
    console.log(haveininv);

    items[itemid].handedin = Number(handedin);
    items[itemid].ininventory = Number(haveininv);
    items[itemid].remaining = Number(items[itemid].amount - (items[itemid].handedin + items[itemid].ininventory));
    id_remaining = "#remaining_" + id;
    $(id_remaining).text(items[itemid].remaining);
    calculateRemaining(itemid);
}


//calculate remaining amount based in the tables data
function calculateRemaining(id){
    console.log(items[id]);
    amount = items[id].amount;
    inv    =  items[id].ininventory;
    handed =  items[id].handedin;
    remaining = items[id].remaining;


    saveLocalSotrage();
}


//search a collectible item based on their id's
function searchItemById(key){
    return items[key];
}

function checkQuestCanBeCompleted(id){
    console.log("will check quest as complete");
}

function markAsCompleteQuest(id){
    console.log("quest: " +id);

    activeItem = {};
    affectedItems = [];
    decreaselist = [];

    for(const item in items){
        if(id in items[item].quests){
            affectedItems.push(item);
        }
    }
    //console.log("If quest completed, affecting these items as well: " + affectedItems);

    for (let index = 0; index < affectedItems.length; index++) {
        const element = affectedItems[index];
        //console.log("Item: " + affectedItems[index] + ". Decrease with the following amount: " +items[element].quests[id]);
        decreaselist.push([affectedItems[index],items[element].quests[id]]);
        //console.log(decreaselist);

    }

    for (let index = 0; index < decreaselist.length; index++) {
        const item = decreaselist[index][0];
        const amount = decreaselist[index][1];

        sum = items[item].amount - amount;
        if(sum < 0){
            items[item].amount = 0;
        }else{
            items[item].amount -= amount;
            items[item].remaining -= amount;
        }








        delete items[item].quests[id];

    }

    //console.log("Corresponding quest id: " + items[questItem].quests[id]);



    //items[activeItem].remaining -= amountInQuest;
    //delete items[activeItem].quests[id];
    saveLocalSotrage();
    location.reload();



}



function saveLocalSotrage(){
    localStorage.clear();
    localStorage.setItem('collectibles', JSON.stringify(items));
    localStorage.setItem('options', JSON.stringify(options));
}

function toggle_show_quests(value){
    options.show_quests = value;
    saveLocalSotrage();
    location.reload();
}

function toggle_show_collector(value){
    options.show_collector = value;
    saveLocalSotrage();
    location.reload();
}

function toggle_show_0_remaining(value){
    options.show_0_remaining = value;
    saveLocalSotrage();
    location.reload();
}

function reset(){
    localStorage.clear();
    location.reload();
}

function exportItems(){
    navigator.clipboard.writeText(JSON.stringify(items));
    alert("Copied to clipboard");
}

function importItems(){
    let c = confirm("Importing from clipboard?");
    if(c){
        items = JSON.parse(localStorage.getItem('collectibles'));
        navigator.clipboard.readText().then( function(clipText){
            localStorage.setItem('collectibles',clipText );
        }
        );

        localStorage.setItem('options', JSON.stringify(options));
        items = JSON.parse(localStorage.getItem('collectibles'));
        options = JSON.parse(localStorage.getItem('options'));
        location.reload();
    }
}
