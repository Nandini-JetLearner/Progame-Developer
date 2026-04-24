# Use case: Phone=camera+music+calling
class Camera:
    def click(self):
        print("Photo Clicked")

class MusicPlayer:
    def play_music(self):
        print("Playong Music")

class Smartphone(Camera,MusicPlayer):
    def call(self):
        print("Calling...")

s=Smartphone()
s.click()
s.play_music()
s.call()