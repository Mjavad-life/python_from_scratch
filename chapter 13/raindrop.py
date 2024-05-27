import sys
import pygame
class Rain :
    # kelasi ke dar an ghatrehaye baran az balaye safhe be paeen miayand
    def __init__(self) :
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0 , 0) , pygame.FULLSCREEN)
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230 , 230, 230 )  
        self.image = pygame.image.load('ghatreh.jpg')
        self.rect = self.image.get_rect()
        #makane avalie biganeha ra moshakhas mikonad
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # makane x bigane ra zakhireh mikonad
        self.x =float(self.rect.x)
        self.ghatreha = pygame.sprite.Group()
      #  self._create_ghatreha()


    def blitme(self) :
        # ghatreh ra dar makane feli mikeshad
        self.screen.blit(self.image , self.rect)   


    def _create_ghatreha(self) :
        ghatreh_width , ghatreh_height = self.rect.size
        current_x , current_y = ghatreh_width , ghatreh_height
        while current_y < (self.screen_height - 3 *ghatreh_height):  
            while  current_x < ( self.screen_width - 2*ghatreh_width) :
                self._create_ghatreh(current_x , current_y)
                current_x += 2*ghatreh_width
            # yek satr tamam mishavad va satr no aghaz
            current_x = ghatreh_width
            current_y += 2 * ghatreh_height  


    def _create_ghatreh(self , x_position , y_position) :
        new_ghatreh = Rain()
        new_ghatreh.x = x_position
        new_ghatreh.rect.x = x_position
        new_ghatreh.rect.y = y_position
        self.ghatreha.add(new_ghatreh)


    def _update_screen(self) :
        self.screen.fill(self.bg_color)   
        self.blitme()
      #  self._create_ghatreha()
        self.ghatreha.draw(self.screen)
        pygame.display.flip()


    def run_game(self):
        # halghe asli bazi ra aghaz mikonad
        while True :            
            self._update_screen()
            self.clock.tick(60)


baran = Rain()
baran.run_game()
        