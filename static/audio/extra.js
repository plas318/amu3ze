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




