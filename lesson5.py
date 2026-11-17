class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = songs  

    def __str__(self):
        return f"Плейлист: {self.name}, песен: {len(self.songs)}"

    def __repr__(self):
        return f"<Playlist object={self.name}, songs={self.songs}>"

    def __eq__(self, other):
        return self.name == other.name


plist1= Playlist("Вайб", songs=[ "Песня1" ," Песня2 "])
plist2= Playlist("Курманбек", songs=[ "Песня3" ," Песня4 "])
print(plist1)
print(repr(plist1))
print(plist2 == plist1)