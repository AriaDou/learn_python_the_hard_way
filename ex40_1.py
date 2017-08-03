# -*- coding: utf-8 -*-
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def set_lyrics(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
    "With pockets full of shells"])

moves_like_a_jagger = Song(["Want the moves like jagger",
    "I got the moves like jagger"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
moves_like_a_jagger.sing_me_a_song()

lyrics = ["ahhhhhhh"]
happy_bday.set_lyrics(lyrics)

happy_bday.sing_me_a_song()
