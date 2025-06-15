from abc import ABC, abstractmethod


class Vinyl:
    def __init__(self, name: str, title: str = None):
        self.name = name
        self.title = title


class RecordPlayer:
    def __init__(self, vinyl: Vinyl) -> None:
        self.vinyl = vinyl

    def play_vinyl(self):
        print(f"Playing vinyl {self.vinyl.name}")

    def stop_vinyl(self):
        print(f"Stopped playing vinyl {self.vinyl.name}")


class MediaPlayer(ABC):
    @abstractmethod
    def play_media():
        pass

    @abstractmethod
    def stop_media():
        pass


class RecordPlayerAdapter(MediaPlayer):
    def __init__(self, record_player: RecordPlayer):
        self.record_player = record_player

    def play_media(self):
        self.record_player.play_vinyl()

    def stop_media(self):
        self.record_player.stop_vinyl()


def main():
    vinyls = [
        Vinyl("Homesick", "ADTR"),
        Vinyl("Horizons", "PD"),
        Vinyl("Toxicity", "SOAD"),
    ]
    for vinyl in vinyls:
        record_player = RecordPlayer(vinyl)
        record_player_adapter = RecordPlayerAdapter(record_player)
        record_player_adapter.play_media()
        print("listening...\n" * 3)
        record_player_adapter.stop_media()


main()
