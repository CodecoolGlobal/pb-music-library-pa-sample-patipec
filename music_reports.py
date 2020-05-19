ARTIST = 0
ALBUM = 1
YEAR = 2
GENRE = 3
LENGHT = 4


def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    album_in_genre = []
    for record in albums:
        if record[GENRE] == genre:
            album_in_genre.append(record[ALBUM])
    return ",".join(album_in_genre)


def change_minutes_into_seconds(lasts):
    sec_per_min = 60
    album_sec = lasts.split(':')
    return int(album_sec[0]) * sec_per_min + int(album_sec[1])

def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """

    longest = albums[0]
    for album in albums:
        if int(change_minutes_into_seconds(longest[LENGHT])) < int(change_minutes_into_seconds(album[LENGHT])):
            longest = album
            return ",".join(longest)

def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    time = []
    for album in albums:
        time.append(change_minutes_into_seconds(album[LENGHT]))
    total = sum(time) / 60
    return total




