def make_album(artist_name,album_title,number_of_songs=None):
    album = {"arist":artist_name,"title":album_title}
    if number_of_songs:
        album["number"]=number_of_songs
    return album
#album1 = make_album(album_title="Loi Choi",artist_name="wren evans",number_of_songs='11')
#print(album1)
#album2 = make_album(album_title="99%",artist_name="MCK")
#print(album2)

while True:
    print("Please give me the information for the album you want to make!")
    print("Enter 'q' to quit the function")
    artist_name = input("Enter the artist name: ")
    if(artist_name=="q"):
        break
    album_title = input("Enter the album title: ")
    if(album_title=='q'):
        break
    number_of_songs = input("Enter the number of songs: ")
    if(number_of_songs=='q'):
        break
    album = make_album(artist_name=artist_name,album_title=album_title,number_of_songs=number_of_songs)
    print(album)