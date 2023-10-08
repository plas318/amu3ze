//This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {

player = new YT.Player('iframe_p', {
videoId: "V2paBoVofDk",
playerVars: 
      {
        
        autoplay: 1
      },
events: {
    'onReady': onPlayerReady,
    'onError': onPlayerError,
    'onStateChange': onStateChange
}
});
}

const shuffleSwitch = document.querySelector('#shuffle')
shuffleSwitch.addEventListener('change', e=>{
    let current_player = YT.get('iframe_p');
    if (e.target.checked){
        current_player.setShuffle(1)
        console.log('Shuffle option set: on')
        player.playVideoAt(0)
    }
    else {
        current_player.setShuffle(0)
        console.log('Shuffle option set: off')
    }
});


// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
    //player.cuePlaylist(['PKs7v6Ti2e0', 'MwN-jQ6fIHY', 'nmHzvQr3kYE']);
} 

function onStateChange(event){
    if (event.data===5){
        let shuffleSwitch = document.querySelector('#shuffle')
        if (shuffleSwitch.checked){
            event.target.setShuffle(1);
            event.target.playVideoAt(0);               
        }
        else{
            event.target.playVideoAt(0);
        }

    }
}


function stopVideo() {
player.stopVideo();
}

function onPlayerError(error){
    console.log(error);
    player.nextVideo()
}

let btns = document.querySelectorAll('.list-group-item-playlist');
btns.forEach( btn => {
    btn.addEventListener('click', e=> {
        //Toggle Selected lists
        
        //Change youtube playlist event
        let pl = YT.get('iframe_p');
        let url = e.target.dataset['url'];
        console.log(url)

        pl.cuePlaylist({list: url, listType:'playlist'});
        
        setTimeout( function(){
            pl.cuePlaylist({list: url, listType:'playlist'})
        },500)


        activelist = document.querySelector('.list-group-item.activated');
        if (activelist){
            activelist.classList.toggle('activated');
        }
        e.target.classList.toggle('activated');

    });
});


const mytoolTip = document.querySelector('[data-bs-toggle="tooltip"]')

//Initializing Tooltips for bootstrap 5
const tooltipList = Array(initTooltip(mytoolTip))
function initTooltip(mytoolTip){
    return new bootstrap.Tooltip(mytoolTip)
}


function shuffle(){
    let current_player = YT.get('iframe_p');
        if (e.target.checked){
            current_player.setShuffle(1)
            console.log('Shuffle option set: on')
            player.playVideoAt(0)
        }
        else {
            current_player.setShuffle(0)
            console.log('Shuffle option set: off')
        }
}


const prev = document.querySelector('#prev-btn');
const play = document.querySelector('#play-btn');
const next = document.querySelector('#next-btn');

prev.addEventListener('click', e=>{
    let current_player = YT.get('iframe_p');
    current_player.previousVideo()
    current_player.previousVideo()
});
next.addEventListener('click', e=>{
    let current_player = YT.get('iframe_p');
    current_player.nextVideo()
});
play.addEventListener('click', e=>{
    let current_player = YT.get('iframe_p');
    const state = player.getPlayerState()
    if (state===1){
        current_player.pauseVideo()
    }
    else {
        current_player.playVideo()
    }
});

const cp = document.querySelector('#c-p');
cp.addEventListener('click', e=>{
    const cPlayer = document.querySelector('.c-player')
    const cText = document.querySelector('.c-text')
    cPlayer.classList.toggle('active');
    cText.classList.toggle('active');

});



function createPlaylist(list) {

    let source = []
    list.forEach((song)=>{
        v = {'source': '../../'+song};
        source.push(v);
    });


    let player = new Calamansi(document.querySelector('#calamansi-player-1'), {
        skin: '../../static/audio/skins/calamansi',
        volume: 20,
        playlists: {
            'Classics': source,
        },
        defaultAlbumCover: '../../static/audio/skins/default-album-cover.png',
    });

    return player
}

if (typeof source !== 'undefined'){
    let player = createPlaylist(source)
}
else{

}




