from brick import EasyBrick, MediumBrick, HardBrick, UnbreakableBrick, SuperBrick
import random
from time import sleep

class Pattern():

    @staticmethod
    def level_1(cols):
        ub = UnbreakableBrick(0,0)

        upper_limit = 8

        x, y = 1, 1

        bricks = []

        while True:
            x = random.choice([1, ub.width//2, ub.width//2 + 1])
            while True:
                if((x+ub.width)>=cols):
                    break
                index = random.choice([0,0,0,0,0,1,1,2])
                if(index == 0):
                    bricks.append(EasyBrick(x,y))
                elif(index == 1): 
                    bricks.append(MediumBrick(x,y))
                else:
                    bricks.append(HardBrick(x,y))
                x+=ub.width+1
            y+=ub.height+1
            if(y>=upper_limit):
                break
        
        # adding unbreakable bricks
        ind = random.randint(2,6)
        if(len(bricks) > 6):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(18,20)
        if(len(bricks) > 20):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(35,38)
        if(len(bricks) > 38):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)

        ind = random.choice([13, 24, 29])
        if(len(bricks) > ind):
            bricks[ind] = SuperBrick(bricks[ind].x, bricks[ind].y)

        # for rainbow brick
        filtered_bricks = list(filter(lambda x: type(x) not in [UnbreakableBrick, SuperBrick], bricks))
        
        for brick in random.sample(filtered_bricks, random.randint(4,8)):
            brick.is_rainbow = True
        
        return bricks

    @staticmethod
    def level_2(cols):
        ub = UnbreakableBrick(0,0)

        upper_limit = 10

        x, y = 1, 1

        bricks = []

        while True:
            x = random.choice([1, ub.width//2, ub.width//2 + 1])
            while True:
                if((x+ub.width)>=cols):
                    break
                index = random.choice([0,0,0,1,1,2])
                if(index == 0):
                    bricks.append(EasyBrick(x,y))
                elif(index == 1): 
                    bricks.append(MediumBrick(x,y))
                else:
                    bricks.append(HardBrick(x,y))
                x+=ub.width+1
            y+=ub.height+1
            if(y>=upper_limit):
                break
        
        # adding unbreakable bricks
        ind = random.randint(2,6)
        if(len(bricks) > 6):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(18,20)
        if(len(bricks) > 20):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(35,38)
        if(len(bricks) > 38):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(60,62)
        if(len(bricks) > 62):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
            
        ind = random.choice([13, 24, 29, 37])
        if(len(bricks) > ind):
            bricks[ind] = SuperBrick(bricks[ind].x, bricks[ind].y)
        
        # for rainbow brick
        filtered_bricks = list(filter(lambda x: type(x) not in [UnbreakableBrick, SuperBrick], bricks))
        
        for brick in random.sample(filtered_bricks, random.randint(4,8)):
            brick.is_rainbow = True
        
        return bricks

    
    @staticmethod
    def level_3(cols):
        ub = UnbreakableBrick(0,0)

        upper_limit = 14

        x, y = 1,5

        bricks = []

        while True:
            x = random.choice([1, ub.width//2, ub.width//2 + 1])
            while True:
                if((x+ub.width)>=cols):
                    break
                index = random.choice([0,0,0,1,1,2])
                if(index == 0):
                    bricks.append(EasyBrick(x,y))
                elif(index == 1): 
                    bricks.append(MediumBrick(x,y))
                else:
                    bricks.append(HardBrick(x,y))
                x+=ub.width+1
            y+=ub.height+1
            if(y>=upper_limit):
                break
        
        # adding unbreakable bricks
        ind = random.randint(2,6)
        if(len(bricks) > 6):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(18,20)
        if(len(bricks) > 20):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(35,38)
        if(len(bricks) > 38):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
        ind = random.randint(60,62)
        if(len(bricks) > 62):
            bricks[ind] = UnbreakableBrick(bricks[ind].x, bricks[ind].y)
            
        ind = random.choice([13, 24, 29, 37])
        if(len(bricks) > ind):
            bricks[ind] = SuperBrick(bricks[ind].x, bricks[ind].y)
        
        # for rainbow brick
        filtered_bricks = list(filter(lambda x: type(x) not in [UnbreakableBrick, SuperBrick], bricks))
        
        for brick in random.sample(filtered_bricks, random.randint(4,8)):
            brick.is_rainbow = True
        
        return bricks

    