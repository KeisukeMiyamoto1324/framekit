# PYTHONPATH=$(pwd) python3 -m tests.yukkuri

from typing import Optional
from framekit.master_scene_element import MasterScene
from framekit.scene_element import Scene
from framekit.text_element import TextElement
from framekit.audio_element import AudioElement
from framekit.image_element import ImageElement
from framekit.video_element import VideoElement
from framekit.animation import AnimationPresets

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
VIDEO_FPS = 60

master = MasterScene(width=VIDEO_WIDTH, height=VIDEO_HEIGHT, fps=VIDEO_FPS, quality="low")
master.set_output("yukkuri.mp4")

scene = Scene()

bg = (
    ImageElement("sample_asset/earth.jpg")
        .set_crop(400, 400, mode="fill")
        .position(VIDEO_WIDTH//3, VIDEO_HEIGHT//3, "center")
        .start_at(0)
        .set_duration(3)
        # .set_blur(10)
        # .set_rotate(100)
        
)

text = (
    TextElement("Hello world")
        .position(VIDEO_WIDTH//2, VIDEO_HEIGHT//2, "center")
        .start_at(0.5)
        # .set_blur(3)
        .set_duration(2.5)
        # .set_rotate(300)
        .set_flip("vertical")
)

scene.add(bg)
scene.add(text)

master.add(scene)
master.render()
