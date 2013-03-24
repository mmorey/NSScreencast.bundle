
VIDEO_PREFIX   = "/video/nsscreencast"
BASE_URL       = "http://feeds.feedburner.com/Nsscreencast?format=xml"
CACHE_INTERVAL = 1800
ICON           = "icon-default.png"

####################################################################################################
def Start():
  Plugin.AddPrefixHandler(VIDEO_PREFIX, VideoMenu, "NSScreencast", ICON, "art-default.png")
  Plugin.AddViewGroup("Details", viewMode="InfoList", mediaType="items")
  MediaContainer.art    = R('art-default.png')
  MediaContainer.title1 = 'NSScreencast'
  HTTP.SetCacheTime(CACHE_INTERVAL)
  
def VideoMenu():
    dir = MediaContainer(mediaType="video", viewGroup="Details")    
    for item in XML.ElementFromURL(BASE_URL, False, errors='ignore').xpath('//item'):
      title       = item.find('title').text.strip()
      date        = item.find('pubDate').text.strip()
      description = item.find('description').text.strip()
      url         = item.find('enclosure').get("url").strip()
      dir.Append(VideoItem(url, title=title, summary=description, subtitle=date[0:-15]))
    dir.Reverse()
    return dir
