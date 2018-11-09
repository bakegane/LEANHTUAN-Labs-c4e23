from youtube_dl import YoutubeDL
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=HWK5p7JL7g4'])

#Dl multi ytb videos
dl = YoutubeDL()
#download songs
dl.download(['http://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

#download audio
options = {
    'format': 'bestaudio/audio' #Download best quality only
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=c3kH1YsmEe0'])

#search and then download first video
options = {
    'default_search': 'ytsearch', #tell downloader to search instead of directly downloading
    'max_downloads': 1 #tell downloader to download only the first entry(video)
}
dl = YoutubeDL(options)
dl.download(['nang am xa dan'])

#Search and then download first audio
options = {
    'default_search': 'ytsearch', #tell downloader to search instead of directly downloading
    'max_downloads': 1, #tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['nho mua sai gon lam truong'])