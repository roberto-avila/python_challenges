#-----Write a function called city_country() that returns a string formatted like this: "Santiago, Chile". Call your function three times with different
#locations and print the returned values.

def city_country(city, country):
    """Returns information about a city."""
    return f"{city.title()}, {country.title()}"

result = city_country('san salvador', 'el salvador')
print(result)

result = city_country('santiago', 'chile')
print(result)

result = city_country('madrid', 'spain')
print(result)

#-----Write a function called make_album() that builds a dictionary describing a music album. Parameters should be artist name, album title, and an optional
#parameter of number of songs in the album. Call the function three times and print out three dictionaries.

def make_album(name, album, songs=None):
    """Returns a dictionary about an artist's album"""
    album_info = {'artist': name.title(), 'album title': album.title(),}
    if songs:
        album_info['number of songs'] = int(songs)
    return album_info

result = make_album('ghost', 'impera', 12)
print(result)

result = make_album('system of a down', 'toxicity')
print(result)

result = make_album('drake', 'honestly, whatever')
print(result)

#-----Using the function from the previous exercise, write a while loop that allows users to enter an album's artist and title. Call the make_album() function with the
#user's input and print the dictionary that's created.

def make_album(name, album, songs=None):
    """Returns a dictionary about an artist's album"""
    album_info = {'artist': name.title(), 'album title': album.title(),}
    if songs:
        album_info['number of songs'] = int(songs)
    return album_info

while True:
    print("Tell me about your favorite artist. Enter 'q' at any point to quit.")
    name_artist = input("Artist name: ")
    if name_artist == 'q':
        break
    name_album = input("Album's name: ")
    if name_album == 'q':
        break
    
    result = make_album(name_artist, name_album)
    print(result)

    prompt = input('Would you like to ask someone else? (y/n): ')
    if prompt == 'n':
        break
    else:
        continue