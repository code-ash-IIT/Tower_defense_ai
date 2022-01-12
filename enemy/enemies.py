from os import path
import pygame

class Enemy:

    def __init__(self):
        self.width=40
        self.height=40
        self.animation_count=0
        self.health=1
        self.vel=3
        self.path=[(5, 318), (53, 346), (113, 401), (172, 414), (227, 366), (276, 284), (320, 284), (383, 292), (434, 247), (492, 214), (550, 206), (611, 216), (668, 246), (706, 303), (724, 354), (717, 375), (682, 428), (638, 455), (589, 471), (540, 472), (487, 463), (496, 419), (507, 378), (531, 347)]
        self.x=self.path[0][0]
        self.y=self.path[0][1]
        self.img=None
        self.path_pos=1
        self.imgs=[]
        self.flipped=False

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        self.img=self.imgs[self.animation_count]
        self.animation_count+=1
        if(self.animation_count>=len(self.imgs)):
            self.animation_count=0
        win.blit(self.img,(self.x-self.enemySize[0]//2, self.y-self.enemySize[1]//2))
        self.move()

    def collide(self, X, Y):
        """
        returns whether enemy is being hit
        parameter x: int
        parameter y: int
        return: Bool
        """
        if(X<=self.x+self.width and X>=self.x):
            if(Y<= self.y +self.height and Y>=self.y):
                return True
        return False
    
    def move(self):
        """
        Moves enemies following the path and do nothing else
        returns: none
        """
        # speed=2

        if(self.path_pos<len(self.path)):
            if(self.x<(self.path[self.path_pos])[0]):
                self.x+=self.speed
            elif(self.x>(self.path[self.path_pos])[0]):
                self.x-=self.speed
            if(self.y<(self.path[self.path_pos])[1]):
                self.y+=self.speed
            elif(self.y>(self.path[self.path_pos])[1]):
                self.y-=self.speed
            z=(self.path[self.path_pos][0]-self.x, self.path[self.path_pos][1]-self.y)

            if(z[0]<0 and not(self.flipped)):
                self.flipped=True
                for count, img in enumerate(self.imgs):
                    self.imgs[count]=pygame.transform.flip(img, True, False)
            elif(z[0]>0 and self.flipped):
                self.flipped=False
                for count, img in enumerate(self.imgs):
                    self.imgs[count]=pygame.transform.flip(img, True, False)

            # print(self.x, self.y)
            # print((self.path[self.path_pos])[0], (self.path[self.path_pos])[1])
            
            if(abs(z[0])//self.speed, abs(z[1])//self.speed)==(0,0):
                self.path_pos+=1
        

    def hit(self):
        """
        returns if an enemy has dies and removes health when called
        :return bool
        """
        self.health-=1
        if self.health<=0:
            return True