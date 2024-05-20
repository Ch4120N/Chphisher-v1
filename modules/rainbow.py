from pystyle import Colors, Colorate

class colorize:
    @staticmethod
    def Diagonal(logo=None):
        return Colorate.Diagonal(Colors.rainbow, logo)
    @staticmethod
    def Vertical(logo=None):
        return Colorate.Vertical(Colors.rainbow, logo)
    @staticmethod
    def Horizontal(logo=None):
        return Colorate.Horizontal(Colors.rainbow, logo)

