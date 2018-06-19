import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
playlist ={1:{'name':'Poison','Artist':'Alice Cooper','Album':'Trash','Song_length':'4'},
           2:{'name':'House of fire','Artist':'Alice Cooper','Album':'Trash','Song_length':'3'},
           3: {'name': 'Hey Stoopid', 'Artist': 'Alice Cooper', 'Album': 'Hey Stoopid', 'Song_length': '1'},
           4: {'name': 'Wind-Up Toy', 'Artist': 'Alice Cooper', 'Album': 'Hey Stoopid', 'Song_length': '5'},
           5: {'name': 'Painkiller', 'Artist': 'Judas Priest', 'Album': 'Painkiller', 'Song_length': '6'},
           6: {'name': 'Rock Hard Ride Free', 'Artist': 'Judas Priest', 'Album': 'Defenders Of The Faith', 'Song_length': '3'},
           7: {'name': 'Imagine', 'Artist': 'John Lennon', 'Album': 'Imagine', 'Song_length': '3'},}


while True:
    choice_act = int(input('1-add song ,2-del song,3-size playlist, 4-clear playlist,5-format_song_output,6-time_of_play_all_playlist: '))
    if choice_act == 1 :
        name = str(input('enter song name: '))
        artist = str(input('enter artist: '))
        album = str(input('enter album  : '))
        song_length = str(input('enter song_length: '))
        playlist[len(playlist)+1] = {'name': name, 'Artist':artist , 'Album':album , 'Song_length': song_length }
    elif choice_act == 2:
        key = int(input('enter song`s key: '))
        playlist.pop(key)
    elif choice_act == 3:
        print('size of playlist = '+str(len(playlist)))
    elif choice_act == 4:
        playlist.clear()
    elif choice_act == 5:
        sorting_criterion = str(input(' enter sorting_criterion: '))
        if sorting_criterion == 'All':
            print(playlist)
        else:
          value = str(input('enter value: '))
          c = 1
          while c <= len(playlist):
            if playlist[c][sorting_criterion] == value:
              print(playlist.get(c))
            c += 1
          c = 1
    elif choice_act == 6:
        time_of_play_all_playlist = 0
        c = 1
        while c < len(playlist):
            time_of_play_all_playlist += int(playlist[c+1]['Song_length'])
            c += 1
        print('Time_of_play_all_playlist '+ str(time_of_play_all_playlist )+' minutes')
        time_of_play_all_playlist = 0
        c = 1


