import sys
from youtubesearchpython import SearchVideos

search_term = sys.argv[1]

search = SearchVideos("search_term", offset = 1, mode = "json", max_results = 20)

#json_str = search.result()
titles = search.titles
links = search.links
view = search.views
thumbnail_link = search.thumbnails

zipped = zip(titles, links, view, thumbnail_link)

for title,link,view,thumbnail in zipped:
    print(f'vc={view},  {title} ')