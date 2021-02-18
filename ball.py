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
    
    def check_overlap_collision(self, board):
        left_coord = self.get_coordinates("left")
        for coord in left_coord:
            if(coord['y']>=0 and coord['y']<board.rows and coord['x']>=0 and coord['x']<board.cols):
                if(board.board[coord['y']][coord['x']] != board.bg_pixel):
                    self.update_position(self.x+1, self.y)
                    self.update_velocity(-self.velocity_x, self.velocity_y)
                    return True

        right_coord = self.get_coordinates("right")
        for coord in right_coord:
            if(coord['y']>=0 and coord['y']<board.rows and coord['x']>=0 and coord['x']<board.cols):
                if(board.board[coord['y']][coord['x']] != board.bg_pixel):
                    self.update_position(self.x-1, self.y)
                    self.update_velocity(-self.velocity_x, self.velocity_y)
                    return True
        
        top_coord = self.get_coordinates("top")
        for coord in top_coord:
            if(coord['y']>=0 and coord['y']<board.rows and coord['x']>=0 and coord['x']<board.cols):
                if(board.board[coord['y']][coord['x']] != board.bg_pixel):
                    self.update_position(self.x, self.y+1)
                    self.update_velocity(self.velocity_x, -self.velocity_y)
                    return True
        
        bottom_coord = self.get_coordinates("bottom")
        for coord in bottom_coord:
            if(coord['y']>=0 and coord['y']<board.rows and coord['x']>=0 and coord['x']<board.cols):
                if(board.board[coord['y']][coord['x']] != board.bg_pixel):
                    self.update_position(self.x, self.y-1)
                    self.update_velocity(self.velocity_x, -self.velocity_y)
                    return True
        return False

    def check_collision(self, board):
        left_coordinates = self.get_coordinates("left")  
        for coord in left_coordinates:
            if coord['x'] < 0:
                self.update_position(0, self.y)
                self.update_velocity(-self.velocity_x, self.velocity_y)
                return True
            elif coord['x'] > 0 and coord['y']>=0 and coord['y']<board.rows:
                if(board.board[coord['y']][coord['x']-1] != board.bg_pixel):
                    # self.update_position(self.x+1, self.y)
                    self.update_velocity(-self.velocity_x, self.velocity_y)
                    return True

        right_coordinates = self.get_coordinates("right")  # todo overflow check
        for coord in right_coordinates:
            if coord['x'] >= board.cols:
                self.update_position(board.cols-self.width-1, self.y)
                self.update_velocity(-self.velocity_x, self.velocity_y)
                return True
            elif coord['x'] < board.cols-1 and coord['y']>=0 and coord['y']<board.rows:
                if(board.board[coord['y']][coord['x']+1] != board.bg_pixel):
                    # self.update_position(self.x-1, self.y)
                    self.update_velocity(-self.velocity_x, self.velocity_y)
                    return True
        
        top_coordinates = self.get_coordinates("top")
        for coord in top_coordinates:
            if coord['y'] < 0:
                self.update_position(self.x, 0)
                self.update_velocity(self.velocity_x, -self.velocity_y)
                return True
            elif coord['y'] > 0 and coord['x']>=0 and coord['x']<board.cols:
                if(board.board[coord['y']-1][coord['x']] != board.bg_pixel):
                    # self.update_position(self.x, self.y+1)
                    self.update_velocity(self.velocity_x, -self.velocity_y)
                    return True
        
        bottom_coordinates = self.get_coordinates("bottom")  # todo overflow check
        for coord in bottom_coordinates:
            if coord['y'] >= board.rows:
                self.update_position(self.x, board.rows-self.height-1)
                self.update_velocity(self.velocity_x, -self.velocity_y)
                return True
            elif coord['y'] < board.rows-1 and coord['x']>=0 and coord['x']<board.cols:
                # print("-->", board.board[coord['y']+1][coord['x']])
                if(board.board[coord['y']+1][coord['x']] != board.bg_pixel):
                    # self.update_position(self.x, self.y-1)
                    new_velocity_y = self.velocity_y
                    if(self.velocity_y>0):
                        new_velocity_y = -self.velocity_y
                    if(coord['y']+1 == board.paddle.y):
                        center_x = board.paddle.x+ (board.paddle.width-1)//2
                        print(board.paddle.x, board.paddle.width, coord['x'], (center_x, coord['y']+1))
                        factor = (coord['x']-center_x)
                        factor = factor*100 / ((board.paddle.width)//2)
                        print("->>>>", factor)
                        if(factor < 0):
                            if(factor<-50):
                                new_velocity_x = self.velocity_x-2
                            else:
                                new_velocity_x = self.velocity_x-1
                            if(new_velocity_x < -2):
                                new_velocity_x = -2
                        else:
                            if(factor>50):
                                new_velocity_x = self.velocity_x+2
                            else:
                                new_velocity_x = self.velocity_x+1
                            if(new_velocity_x > 2):
                                new_velocity_x = 2
                        self.update_velocity(new_velocity_x, new_velocity_y)
                    else:
                        self.update_velocity(self.velocity_x, new_velocity_y)
                    return True
        return False

    def move(self, board):
        # self.update_position(self.x+self.velocity_x, self.y+self.velocity_y)
        init_x = self.x
        init_y = self.y
        final_x = self.x+self.velocity_x
        final_y = self.y+self.velocity_y

        if(self.velocity_x != 0 and self.velocity_y != 0):
            x_step = abs(final_x-self.x) + 1
            y_step = abs(final_y-self.y) + 1

            step = 0
            minimum = 'y'
            if(y_step > x_step):
                step = y_step // x_step
                minimum = 'x'
            else:
                step = x_step // y_step
            if(minimum == 'x'):
                x = self.x
                i = 0
                y = init_y
                while True:
                    # check top bottom left right
                    if i!=0:
                        self.update_position(x,y)
                        if self.check_collision(board) == True:
                            # if x==init_y and y == init_y:
                            #     self.update_position(x,y)
                            break
                    i+=1
                    if(i%step == 0 and x != final_x):
                        if self.velocity_x>0:
                            x = x+1
                        else:
                            x = x-1   
                        # check whether inside any object, or out of bound 
                        self.update_position(x,y)
                        if self.check_overlap_collision(board) == True:
                            break
                    if(self.velocity_y > 0):
                        y = y+1
                        if(y>final_y):
                            break
                    else:
                        y = y-1
                        if(y<final_y):
                            break
            else:
                y = self.y
                i = 0
                x = init_x
                while True:
                    # check top bottom left right
                    if i!=0:
                        self.update_position(x,y)
                        if self.check_collision(board) == True:
                            break
                    i+=1
                    if(i%step == 0 and y != final_y):
                        if self.velocity_y>0:
                            y = y+1
                        else:
                            y = y-1   
                        # check whether inside any object, or out of bound 
                        self.update_position(x,y)
                        if self.check_overlap_collision(board) == True:
                            break
                    if(self.velocity_x > 0):
                        x = x+1
                        if(x>final_x):
                            break
                    else:
                        x = x-1
                        if(x<final_x):
                            break
        else:
            if(self.velocity_x !=0):
                x = init_x
                while True:
                    # print((x,init_y))
                    # check top bottom left right
                    if x!= init_x:
                        self.update_position(x,init_y)
                        if self.check_collision(board) == True:
                            break
                    if(self.velocity_x > 0):
                        x = x+1
                        if(x>final_x):
                            break
                    else:
                        x = x-1
                        if(x<final_x):
                            break
            elif(self.velocity_y != 0):
                y = init_y
                while True:
                    # print((init_x,y))
                    # check top bottom left right
                    if y!=init_y:
                        self.update_position(init_x,y)
                        if self.check_collision(board) == True:
                            break
                    if(self.velocity_y > 0):
                        y = y+1
                        if(y>final_y):
                            break
                    else:
                        y = y-1
                        if(y<final_y):
                            break
        # print((self.x, self.y))
        # for row in range(self.y, self.y+self.height):
        #     for col in range(self.x, self.x+self.width):
        #         board.board[row][col] = board.ball.pixel

        # # left wall collision
        # left_coordinates = self.get_coordinates("left")
        # for coord in left_coordinates:
        #     if coord['x'] < 0:
        #         self.update_position(0, self.y)
        #         self.update_velocity(-self.velocity_x, self.velocity_y)
        #         break
        #     elif coord['x'] > 0:
        #         if(board.board[coord['y']][coord['x']-1] != board.bg_pixel):
        #             self.update_velocity(-self.velocity_x, self.velocity_y)
        #     #     break
                
        # right wall collision