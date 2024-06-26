import sys 
from time import sleep
import pygame
from settings import Settings 
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship  
from bullet import Bullet
from alien import Alien 
from button import Button 


class AlienInvasion:
    """Class that manages the resources and behavior of the game"""
    def __init__(self):
        """Initialize the game and creates the game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        
        # Create an instance to store game statistics and scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        # Create Play button 
        self.play_botton = Button(self, "Play")

    
    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()     
        
    
    def _check_events(self):    
        """Monitor mouse and keyboard events"""
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)                
    
    
    def _check_play_button(self, mouse_pos):
        """Start new game when the player click on Play button"""
        button_clicked = self.play_botton.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
            
            # Reset the game statistics 
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            
            # Get rid of any remaining aliens or bullets 
            self.aliens.empty()
            self.bullets.empty()
            
            # Create new fleet and put the ship in the center 
            self._create_fleet()
            self.ship.center_ship()
            
            # Hide the mouse cursor  
            pygame.mouse.set_visible(False)
            
    
    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
   
            
    def _check_keyup_events(self, event):
        """Respond to keyreleases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    
    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Create an alien and find the number of aliens in a row
        # Spacing between each alien is to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Determine the number of rows that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # Create the first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
        
            
    def _create_alien(self, alien_number, row_number):
        """ Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien) 
    
    
    def _check_fleet_edges(self):
        """Respond appropriately if any alien has reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)                
    
    
    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets"""
        self.bullets.update()
        # Get rid of bullets that have disappeared 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
        self._check_bullet_alien_collisions()
     
        
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""
        # Remove all bullets-aliens collisions 
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)   
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet() 
            self.settings.increase_speed()
            
            # Increse the level
            self.stats.level += 1
            self.sb.prep_level()
    
    
    def _update_aliens(self):
        """Check if the fleet is at the edge, then, update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        
        # Look for alien-ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        # Look for aliens hitting the ground 
        self._check_aliens_bottom()
    
    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # Decrement ships_left and reset the dashboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()
        
            # Get rid of any remaining aliens and bullets 
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet of aliens and center ship 
            self._create_fleet()
            self.ship.center_ship()
        
            # Pause 
            sleep(0.5)
        else:
            self.stats.game_active = False 
            pygame.mouse.set_visible(True)
       
            
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship is fit 
                self._ship_hit()
                break 
    
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() 
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        # Draw score information
        self.sb.show_score() 
        
        # Draw the Play button, is the game is not active 
        if not self.stats.game_active:
            self.play_botton.draw_button()
           
        # Show the last drawn screen visible
        pygame.display.flip()  

# Create a game instance and launch the game
if __name__ == '__main__':    
    ai = AlienInvasion()
    ai.run_game()