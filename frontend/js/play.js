var gameStatus = {game:{status:-1}, user:null, players:[]}

function gameloop(){
    var gameId = getGameId();
    fetch(`/game_status/${gameId}`).then(function(response) { 
        return response.json();
    }).then(function(j) {
        play(j);
        setTimeout(gameloop, 5000);
    });
} 

function play(newStatus){
    if (statusChanged(newStatus)){
        updateStatus(newStatus.game.status)
    }
    gameStatus = newStatus;
}


function statusChanged(newStatus){
    if (newStatus.game.status != gameStatus.game.status){
        updateStatus(newStatus.game.status);
    }
}

function updateStatus(status){
    s = document.getElementById("game");
    s.setAttribute("data-status", status);
}

function getGameId(){
    return location.href.split("/")[4]
}

function join(){
    var playerName = document.getElementById("name").value;
    fetch(`/games/${getGameId()}/players`, {  
        method: 'POST',
        body: JSON.stringify({player_name:playerName})
    }).then(function (data) {  
      console.log('Request success: ', data);  
    })  
    .catch(function (error) {  
      console.log('Request failure: ', error);  
    });
}


setTimeout(gameloop, 5000);