class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

lyrics_kings_never_die = ["Here to stay", 
                        "Even when I'm gone",
                        "When I close my eyes",
                        "Through the passage of time",
                        "Kings never die"]

kings_never_die = Song(lyrics_kings_never_die) 
                        
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

kings_never_die.sing_me_a_song()
