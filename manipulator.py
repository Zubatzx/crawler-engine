class StringManipulator:
    def CleanNumber(self, phrase):
        lst = [".", ",", "Rp ", "rp ", " K", " k ", "Rp", "rp", "K", "k", " (", ") ", "(", ")", "%", " +", " +", "+"]
        for ls in lst:
            phrase = phrase.replace(ls, '')
        return phrase