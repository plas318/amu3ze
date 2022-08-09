const yas = require('youtube-audio-server')

// Node js 
const api = process.env.Y_API_KEY

yas.setKey(api)
const port = 7331


function load_yas() {

    yas.listen(port, () => {
        console.log(`Listening on port http://localhost:${port}.`)
      })
      
}
load_yas()

function download_yas(){

    const id = 'https://www.youtube.com/watch?v=L-u3fkgZkO0' // 
      
      
      yas.get(id, (err, data) => {
          console.log(`GOT METADATA for ${id}:`, data || err)
      })
      
      console.log(`Downloading ${id}...`)
      yas.downloader
        .setFolder('./') // Optionally set a folder for downloaded content.
        .onSuccess(({id}) => {
          console.log(`Yay! Audio (${id}) downloaded successfully into ""!`)
        })
        .onError(({ id, error }) => {
          console.error(`Sorry, an error ocurred when trying to download ${id}`, error)
        })
        .download({ id, cache, metadata })
}