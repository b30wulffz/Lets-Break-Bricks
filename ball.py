from colorama import Fore, Back, Style 

class Ball():

    def __init__(self, x, y):
        self.velocity_x = 0
        self.velocity_y = 0

        self.x = x
        self.y = y

        self.height = 1
        self.width = 2

        self.pixel =  Back.RED+' '+Style.RESET_ALL

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def update_velocity(self, velocity_x, velocity_y):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def get_coordinates(self, direction):
        coordinates = []
        if(direction == "left"):
            x_coord = self.x
            for row in range(self.y, self.y+self.height):
                coordinates.append({"x": x_coord, "y": row})
        elif(direction == "right"):
            x_coord = self.x+self.width-1
            for row in range(self.y, self.y+self.height):
                coordinates.append({"x": x_coord, "y": row})
        elif(direction == "top"):
            y_coord = self.y
            for col in range(self.x, self.x+self.width):
                coordinates.append({"x": col, "y": y_coord})
        elif(direction == "bottom"):
            y_coord = self.y+self.height-1
            for col in range(self.x, self.x+self.width):
                coordinates.append({"x": col, "y": y_coord})
        return coordinates
    