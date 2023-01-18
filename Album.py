class Album:
    def __init__(self, circleName, albumTitle, songAmount, albumURL, pictureURL):
        self.circleName = circleName
        self.albumTitle = albumTitle
        self.songAmount = songAmount
        self.albumURL = albumURL
        self.pictureURL = pictureURL

    def getCircleName(self):
        return self.circleName

    def getAlbumTitle(self):
        return self.albumTitle

    def getSongAmount(self):
        return self.songAmount

    def getAlbumURL(self):
        return self.albumURL

    def getPictureURL(self):
        return self.pictureURL

    def updateCircleName(self, circleName):
        self.circleName = circleName

    def updateAlbumTitle(self, albumTitle):
        self.albumTitle = albumTitle

    def updateSongAmount(self, songAmount):
        self.songAmount = songAmount

    def updateAlbumURL(self, albumURL):
        self.albumURL = albumURL

    def updatePictureURL(self, pictureURL):
        self.pictureURL = pictureURL