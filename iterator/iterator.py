class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.songs):
            song = self.songs[self._index]
            self._index += 1
            return song
        else:
            raise StopIteration

playlist = Playlist()

playlist.add_song(Song("Bire", "AEO"))
playlist.add_song(Song("Oceans", "Hillsong"))
playlist.add_song(Song("No Longer Slaves", "Bethel Music"))

iterator = iter(playlist)
print("Playlist Songs:")
for song in iterator:
    print(f"{song.title} by {song.artist}")
