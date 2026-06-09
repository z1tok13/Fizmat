class Temperature:
    @staticmethod
    def cel_fa(cel):
        return (cel * 9 / 5) + 32
    def fa_cel(fa):
        return (fa - 32) * 5 / 9