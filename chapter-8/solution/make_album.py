def make_album(artist, album, number_songs=0):
    """BUild dictionary with album details"""
    artist_album = {
        'artist':artist.title() ,
        'album':album.title()
        }
    
    if number_songs:
        artist_album['songs'] = number_songs
    return artist_album

while True:
    print("\nPlease tell me your artist album name")
    print("(enter 'q' at any time to quit)")

    artist_name = input("artist name:")
    if artist_name == 'q':
        break

    album_name = input("album name: ")
    if album_name == 'q':
        break

    number_songs = input("number of songs : ")
    if album_name == 'q':
        break


    formatted_name = make_album(artist_name, album_name, number_songs)
    print(f"\n {formatted_name}")

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', number_songs=8)
print(album)