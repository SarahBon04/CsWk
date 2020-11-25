import requests, json, random
def load_genre():
    #Loads data from deezer
    genre_data = requests.get("https://api.deezer.com/genre")

    genre_dict = {}
    #Puts deezer data in to a python dictionary
    genre_list = genre_data.json()["data"]
    for genre in genre_list:
        genre_name = genre["name"] 
        genre_id = genre["id"]

        #Add to the dictionary
        genre_dict[genre_name] = genre_id
    return genre_dict

def load_artist(genre_id):
    #Loads artist from particular genre
    artist_url = "https://api.deezer.com/genre/" + str(genre_id) + "/artists"
    artist_data = requests.get(artist_url)

    artist_dict = {}
    #Puts artist data in to a python dictionary
    artist_list = artist_data.json()["data"]
    for artist in artist_list:
        artist_name = artist["name"]
        artist_id = artist["id"]

        #Add to dictionary
        artist_dict[artist_name] = artist_id
    return artist_dict

#Selecting random artist and return id
def random_artist(artist_dict):
    random_artist_id = random.choice(list(artist_dict.values()))
    return random_artist_id

def load_song(artist_id):
    #Loads songs from a particular artist 
    song_url = "https://api.deezer.com/artist/" + str(artist_id) + "/top"
    song_data = requests.get(song_url)
    
    song_list = []
    #Puts song data into python list
    
    for song in song_data.json()["data"]:
        song_list.append(song)
    return song_list

def random_song(song_list):
    song = random.choice(song_list) 
    return song 






if __name__ == "__main__":
    mylist = load_artist(132)
    myartist = random_artist(mylist)
    mysonglist = load_song(myartist)
    mysong = random_song(mysonglist)
    print(mysong)


