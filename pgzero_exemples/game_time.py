
class game_time:
    """
    Small object to hold the time variable and time change function

    Using objects allows us to access and change game variables within
    other game functions without declaring global variables
    """
    def __init__(self):
        self.elapsed_time = 0 # elapsed_time variable starts at 0
    
    def set_time(self):  # called at an interval of 1.0 seconds by the clock
        self.elapsed_time += 1
