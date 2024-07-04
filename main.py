class MusicStore:
    pass




if __name__ == '__main__':
    music_new_age = MusicStore()
    music_rock = MusicStore()

    music_new_age.name_album = "Mandolinoage"

    music_rock.name_album = "Rocchettari"

    print(music_new_age.name_album)

    print(music_rock.name_album)