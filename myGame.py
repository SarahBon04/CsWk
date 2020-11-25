from lib import music

mylist = music.load_artist(132)
myartist = music.random_artist(mylist)
mysonglist = music.load_song(myartist)
mysong = music.random_song(mysonglist)
print(mysong)