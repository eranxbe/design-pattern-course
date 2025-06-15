from abc import ABC, abstractmethod


class PlaylistComponent(ABC):
    @abstractmethod
    def play_song(self):
        pass


class Song(PlaylistComponent):
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def play_song(self):
        print(f"Playing {self.title} by {self.artist}")


class PlaylistComposite(PlaylistComponent):
    def __init__(self):
        self.components: list[Song] = []

    def add_component(self, song: Song):
        self.components.append(song)

    def remove_component(self, song: Song):
        self.components.remove(song)

    def play_song(self):
        for component in self.components:
            component.play_song()


def main():
    songs1 = [
        Song("Homesick", "ADTR"),
        Song("Horizons", "PD"),
        Song("Toxicity", "SOAD"),
    ]
    songs2 = [
        Song("Constellations", "ABR"),
        Song("S/T", "DGD"),
        Song("California Cursed", "DRAIN"),
    ]
    playlist1 = PlaylistComposite()
    playlist2 = PlaylistComposite()

    for song in songs1:
        playlist1.add_component(song)

    for song in songs2:
        playlist2.add_component(song)

    playlist1.add_component(playlist2)

    playlist1.play_song()


main()
