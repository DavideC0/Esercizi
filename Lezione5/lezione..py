def create_playllist() -> dict:
    name_playlist: str = str(input("Inserisci un nome per la playlist: "))
    while True:
        try:
            num_song: int = int(input("Inserisci il numero di canzoni che vuoi mettere: "))
            break
        except:
            print("Il valore inserito non è valido")
    playlist: dict = {}
    for i in range(num_song):
        song: str = str(input("Inserisci il nome della canzone desidera: "))
        playlist.update({song: "liked = True"})
    dplaylist: dict = {}
    dplaylist[name_playlist] = playlist

    return dplaylist

def add_favorite(playlist: dict) -> dict:

    pass

print(create_playllist())