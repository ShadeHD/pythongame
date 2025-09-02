import pygame
from settings import VOLUME_MUSIC, VOLUME_SFX

class SoundManager:
    def __init__(self, asset_loader):
        self.asset_loader = asset_loader
        if pygame.mixer.get_init():
            pygame.mixer.music.set_volume(VOLUME_MUSIC)

    def play_music(self, music_name, loops=-1):
        if not pygame.mixer.get_init():
            print("Pygame mixer not initialized. Cannot play music.")
            return

        music_path = self.asset_loader.get_sound_path(music_name)
        if music_path:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(loops)
        else:
            print(f"Music not found: {music_name}")

    def stop_music(self):
        if not pygame.mixer.get_init():
            print("Pygame mixer not initialized. Cannot stop music.")
            return
        pygame.mixer.music.stop()

    def play_sfx(self, sfx_name):
        if not pygame.mixer.get_init():
            print("Pygame mixer not initialized. Cannot play sound effect.")
            return

        sfx = self.asset_loader.get_sound(sfx_name)
        if sfx:
            # Only play coin and collision sounds - NO MOVEMENT SOUNDS
            if sfx_name in ["coin_sfx", "collision_sfx"]:
                sfx.set_volume(VOLUME_SFX)
                sfx.play()
        else:
            print(f"SFX not found: {sfx_name}")

    def play_victory_sound(self):
        """Play a pleasant victory sound - just one nice sound"""
        if not pygame.mixer.get_init():
            return
        
        # Play a single, pleasant sound for victory
        sfx = self.asset_loader.get_sound("coin_sfx")
        if sfx:
            sfx.set_volume(VOLUME_SFX * 0.8)  # Quieter, more pleasant
            sfx.play()

    def play_level_complete_sound(self):
        """Play a pleasant level complete sound"""
        if not pygame.mixer.get_init():
            return
        
        # Play a single, pleasant sound for level complete
        sfx = self.asset_loader.get_sound("coin_sfx")
        if sfx:
            sfx.set_volume(VOLUME_SFX * 0.6)  # Even quieter for level complete
            sfx.play()


