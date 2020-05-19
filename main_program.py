import music_reports
import display
import file_handling
"""
The main program should use functions from music_reports and display modules
"""


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    albums = file_handling.import_data(filename='albums_data.txt')
    print("Hello in our CODECOOL store! What do you want to check?\n"
          "Press  key and enter if you want to :\n"
          "1 ---> display album info\n"
          "2 ---> print whole list of our albums\n"
          "3 ---> check albums' names of given genre\n"
          "4 ---> show longest album\n"
          "5 ---> show total lenght of albums\n")
    choice = int(input(">>>"))

    if choice > 0 and choice <=5:
        if choice == 1: # display function is strange
            album = input("Write album you want to check\n")
            display.print_album_info(album)
        elif choice == 2:
            albums_data = file_handling.import_data(filename='albums_data.txt')
            display.print_albums_list(albums_data)
        elif choice == 3:
            genre = input("Write genre you want to show all albums in it\n").lower()
            print(music_reports.get_albums_by_genre(albums, genre))
        elif choice == 4:
            print(music_reports.get_longest_album(albums))
    else:
        print("There is no such choice")
if __name__ == '__main__':
    main()
