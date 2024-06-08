class Settings:
    """Class to save all game settings."""
    
    def __init__(self):
        """Initialize game static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (9, 2, 15)
        
        # Ship settings 
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullet settings 
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 38, 0)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        
        # How fast the game speed up 
        self.speedup_scale = 1.1
        
        # How fast the aliens value is growing
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.0
        self.bullet_speed = 2.5
        self.alien_speed = 0.5
        
         # fleet_direction 1 represents right; -1 left
        self.fleet_direction = 1
        
        # Points
        self.alien_points = 50
        
        
    def increase_speed(self):
        """Increase speed and value settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale 
        
        self.alien_points = int(self.alien_points * self.score_scale)
        