import pygame
import os

class AssetLoader:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}
        self.sound_paths = {}

    def load_image(self, path, name=None):
        if name is None:
            name = os.path.basename(path).split(".")[0]
        if name not in self.images:
            try:
                image = pygame.image.load(path).convert_alpha()
                self.images[name] = image
                print(f"Loaded image: {name} from {path}")
            except pygame.error as e:
                print(f"Error loading image {path}: {e}")
                # Try loading without convert_alpha if that fails
                try:
                    image = pygame.image.load(path)
                    self.images[name] = image
                    print(f"Loaded image: {name} from {path} (without convert_alpha)")
                except pygame.error as e2:
                    print(f"Failed to load image {path}: {e2}")
        return self.images.get(name)

    def load_sound(self, path, name=None):
        if not pygame.mixer or not pygame.mixer.get_init():
            print(f"Pygame mixer not initialized. Skipping sound loading for {path}")
            return None

        if name is None:
            name = os.path.basename(path).split(".")[0]
        if name not in self.sounds:
            try:
                sound = pygame.mixer.Sound(path)
                self.sounds[name] = sound
                self.sound_paths[name] = path # Store the path
                print(f"Loaded sound: {name} from {path}")
            except pygame.error as e:
                print(f"Error loading sound {path}: {e}")
        return self.sounds.get(name)

    def load_font(self, path, size, name=None):
        if name is None:
            name = os.path.basename(path).split(".")[0]
        key = f"{name}_{size}"
        if key not in self.fonts:
            try:
                font = pygame.font.Font(path, size)
                self.fonts[key] = font
                print(f"Loaded font: {name} (size {size}) from {path}")
            except pygame.error as e:
                print(f"Error loading font {path}: {e}")
        return self.fonts.get(key)

    def get_image(self, name):
        return self.images.get(name)

    def get_sound(self, name):
        return self.sounds.get(name)

    def get_sound_path(self, name):
        return self.sound_paths.get(name)

    def get_font(self, name, size):
        key = f"{name}_{size}"
        return self.fonts.get(key)


