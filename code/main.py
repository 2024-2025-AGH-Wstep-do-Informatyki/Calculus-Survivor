from settings import *
from player import Player
from sprites import *
from random import randint
from pytmx.util_pygame import load_pygame

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Calculus Survivor')
        self.clock = pygame.time.Clock()
        self.running = True
        
        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()
        
        # sprites
        self.player = Player((500, 300), self.all_sprites, self.collision_sprites)

    def setup(self):
        map = load_pygame(join('data', 'maps', 'world.tmx'))
        for x,y,image in map.get_layer_by_name('Ground').tiles():
            Sprite((x*64 , y*64), image, self.all_sprites)
        for obj in map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))
        for obj in map.get_layer_by_name('Collisions'):
	        CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick() / 1000
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # update
            self.all_sprites.update(dt)

            # draw sprites
            self.display_surface.fill('black')
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        
        pygame.quit()


if __name__=='__main__':
    game = Game()
    game.run()
