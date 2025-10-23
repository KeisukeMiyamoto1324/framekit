# PYTHONPATH=$(pwd) python3 -m tests.multi_scene

from framekit.master_scene_element import MasterScene
from framekit.scene_element import Scene
from framekit.text_element import TextElement
from framekit.audio_element import AudioElement
from framekit.image_element import ImageElement
from framekit.video_element import VideoElement
from framekit.animation import AnimationPresets

master = MasterScene(width=1920, height=1080, fps=60, quality="low")
master.set_output("output/multi_scene.mp4")

for telop in ["Hello", "Good morning", "Good evening"]:
    scene = Scene()
    audio = AudioElement("sample_asset/effect1.mp3").set_volume(10)
    text = TextElement(telop, size=28).set_duration(audio.duration)
    
    scene.add(text)
    scene.add(audio)
    
    master.add(scene)

text = (
    TextElement("Special", size=28)
        .set_duration(4)
        .start_at(2)
        .position(x=100, y=100)
)
scene = Scene()
scene.start_at(0)
scene.add(text)

master.add(scene)
master.render()