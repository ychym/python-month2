

class Playlist:
    # magic methods, dunder - double underscore
    def __init__(self, name, songs = None):
        self.name = name
        self.songs = songs

    def __str__(self):
        return f"<Playlist object, name: {self.name}, songs: {self.songs}>"

    def __len__(self):
        return len(self.songs)

    def __contains__(self, item):
        print(f"Item is in playlist: {item}")
        return item in self.songs

    def __bool__(self):
        return len(self.songs) > 0

if __name__ == "__main__":#eger ushul fileda run kylganda gana ishteit.Importtolgon file da koldonulbait
    pop = Playlist("Pop", songs=["Die With A Smile", "So Easy"])
    print(pop)
    print(len(pop))
    print("Billy" in pop)
    print("So Easy" in pop)
    if pop:
        print(f"Playlist is not empty")
    else:
        print(f"Playlist is empty")
