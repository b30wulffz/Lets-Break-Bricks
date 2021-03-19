class Utils():

    @staticmethod
    def get_coordinates(object, direction):
        coordinates = []
        if(direction == "left"):
            x_coord = object.x
            for row in range(object.y, object.y+object.height):
                coordinates.append({"x": x_coord, "y": row})
        elif(direction == "right"):
            x_coord = object.x+object.width-1
            for row in range(object.y, object.y+object.height):
                coordinates.append({"x": x_coord, "y": row})
        elif(direction == "top"):
            y_coord = object.y
            for col in range(object.x, object.x+object.width):
                coordinates.append({"x": col, "y": y_coord})
        elif(direction == "bottom"):
            y_coord = object.y+object.height-1
            for col in range(object.x, object.x+object.width):
                coordinates.append({"x": col, "y": y_coord})
        return coordinates
    
    @staticmethod
    def destroy(item, item_list):
        item_list.remove(item)