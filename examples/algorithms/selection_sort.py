class PlaylistSorter:
    def sort_by_duration(self, songs):
        # Use selection sort to sort by song duration
        # songs = [("Song A", 180), ("Song B", 210), ("Song C", 165)]
        # Return sorted list by duration (shortest first)
        sorted_playlist = []
        while len(songs) > 0:
            shortest_song_index = self.find_shortest_song(songs)
            sorted_playlist.append(songs.pop(shortest_song_index))

        return sorted_playlist

    def find_shortest_song(self, songs):
        # Helper method - return INDEX of shortest song
        shortest_song = songs[0]
        self.shortest_song_index = 0

        shortest_duration = shortest_song[1]

        for i, song in enumerate(songs):
            duration = song[1]

            if duration < shortest_duration:
                shortest_duration = duration
                self.shortest_song_index = i

        return self.shortest_song_index


if __name__ == "__main__":
    songs = [("Song A", 380), ("Song B", 210), ("Song C", 240)]

    playlist = PlaylistSorter()

    sorted_playlist = playlist.sort_by_duration(songs)
    print(f"{sorted_playlist}")
