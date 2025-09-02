import pygame
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self, color, size, position, velocity):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=position)
        self.velocity = velocity
        self.alpha = 255

    def update(self, dt):
        self.rect.x += self.velocity[0] * dt * 60 # Scale with dt
        self.rect.y += self.velocity[1] * dt * 60 # Scale with dt
        self.alpha -= 5 # Fade out
        if self.alpha <= 0:
            self.kill()
        else:
            self.image.set_alpha(self.alpha)

class KissParticle(pygame.sprite.Sprite):
    def __init__(self, position, velocity, size):
        super().__init__()
        self.image = self.create_kiss_emoji(size)
        self.rect = self.image.get_rect(center=position)
        self.velocity = velocity
        self.alpha = 255
        self.life = 1.5

    def create_kiss_emoji(self, size):
        """Create a kiss emoji surface"""
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Draw kiss emoji (simplified)
        # Background circle
        pygame.draw.circle(surface, (255, 255, 0), (size//2, size//2), size//2)
        pygame.draw.circle(surface, (255, 200, 0), (size//2, size//2), size//2 - 2)
        
        # Eyes
        pygame.draw.circle(surface, (0, 0, 0), (size//2 - size//10, size//2 - size//8), size//20)
        pygame.draw.circle(surface, (0, 0, 0), (size//2 + size//10, size//2 - size//8), size//20)
        
        # Kiss mouth (simplified)
        pygame.draw.circle(surface, (255, 100, 100), (size//2, size//2 + size//8), size//10)
        
        return surface

    def update(self, dt):
        self.rect.x += self.velocity[0] * dt
        self.rect.y += self.velocity[1] * dt
        self.velocity[1] += 200 * dt  # Gravity
        self.life -= dt
        self.alpha = int(255 * (self.life / 1.5))
        
        if self.life <= 0:
            self.kill()
        else:
            self.image.set_alpha(self.alpha)

class ParticleManager:
    def __init__(self):
        self.particles = pygame.sprite.Group()
        self.custom_particles = []

    def create_explosion(self, position, color, num_particles=10):
        for _ in range(num_particles):
            size = random.randint(5, 15)
            velocity = [random.uniform(-5, 5), random.uniform(-5, 5)]
            self.particles.add(Particle(color, size, position, velocity))

    def add_custom_particle(self, particle_data):
        """Add a custom particle (like kiss emoji)"""
        self.custom_particles.append(particle_data)

    def update(self, dt):
        self.particles.update(dt)
        
        # Update custom particles
        for particle in self.custom_particles[:]:
            particle['x'] += particle['vx'] * dt
            particle['y'] += particle['vy'] * dt
            particle['vy'] += 300 * dt  # Gravity
            particle['life'] -= dt
            
            if particle['life'] <= 0:
                self.custom_particles.remove(particle)

    def draw(self, screen):
        self.particles.draw(screen)
        
        # Draw custom particles
        for particle in self.custom_particles:
            if particle['type'] == 'kiss':
                # Draw kiss emoji particle
                kiss_surface = pygame.Surface((particle['size'], particle['size']), pygame.SRCALPHA)
                
                # Draw kiss emoji
                pygame.draw.circle(kiss_surface, (255, 255, 0), (particle['size']//2, particle['size']//2), particle['size']//2)
                pygame.draw.circle(kiss_surface, (255, 200, 0), (particle['size']//2, particle['size']//2), particle['size']//2 - 2)
                
                # Eyes
                pygame.draw.circle(kiss_surface, (0, 0, 0), (particle['size']//2 - particle['size']//10, particle['size']//2 - particle['size']//8), particle['size']//20)
                pygame.draw.circle(kiss_surface, (0, 0, 0), (particle['size']//2 + particle['size']//10, particle['size']//2 - particle['size']//8), particle['size']//20)
                
                # Kiss mouth
                pygame.draw.circle(kiss_surface, (255, 100, 100), (particle['size']//2, particle['size']//2 + particle['size']//8), particle['size']//10)
                
                # Apply alpha
                alpha = int(255 * (particle['life'] / 1.5))
                kiss_surface.set_alpha(alpha)
                
                screen.blit(kiss_surface, (particle['x'] - particle['size']//2, particle['y'] - particle['size']//2))


