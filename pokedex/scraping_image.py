from BeautifulSoup import BeautifulSoup
import argparse
import requests

ap = argparse.ArgumentParser()
#ap.add_argument("-p", "--pokemon-list", required=True, help="Path to where raw html was store")
ap.add_argument("-s", "--sprites", required=True, help="Path where we will store our sprites image")
args = vars(ap.parse_args())

url = "https://pokemondb.net/pokedex/national"
print "Fetching html file...."
r = requests.get(url)

if r.status_code == 200:
    soup = BeautifulSoup(r.content)
    names = []
    for link in soup.findAll('a', {'class': 'ent-name'}):
        names.append(link.text)

    for name in names:
        parseName = name.lower()
        parseName = parseName.replace("'", "")
        parseName = parseName.replace(". ", "-")
        if name.find(u'\u2640') != -1:
            parseName = 'nidoran-f'
        elif name.find(u'\u2642') != -1:
            parseName = "nidoran-m"

        print "Downloading image %s" % name
        image_url = "http://img.pokemondb.net/sprites/red-blue/normal/%s.png" % (parseName)
        image = requests.get(image_url)
        if image.status_code != 200:
            print "Fail to download image.."
            continue
        f = open("%s%s.png" % (args["sprites"], name.lower()), "wb")
        f.write(image.content)
        f.close()
