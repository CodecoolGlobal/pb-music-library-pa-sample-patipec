def print_album_info(album): # something stupid is shown :/ string is sliced into char
    artist_index = 0
    name_index = 1

    print('Album: {} by {}'.format(album[name_index], album[artist_index]))
    print(' | '.join(album[2:]))


def print_albums_list(albums_data):
    for album in albums_data:
        print(' | '.join(album))


def print_program_menu(menu_commands): # I know I shouuld use that but I had another sotution in my head :)
    for option in menu_commands:
        print(str(menu_commands.index(option)) + '----->' + option)


def print_command_result(message): # I know I shouuld use that but I had another sotution in my head :)
    vertical_spacing = 2

    print(vertical_spacing * '\n' + message)
