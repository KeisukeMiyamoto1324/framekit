
# PYTHONPATH=$(pwd) python3 -m tests.basic

from framekit import MasterScene, Scene, TextElement, AudioElement, ImageElement
from PIL import Image

# Short1.wav: about 1sec
# Short2.wav: about 1sec
# Short3.wav: about 12sec

def main():
    # Create master scene
    master_scene = MasterScene(
        width=1920, 
        height=1080, 
        fps=60,
        output_filename="output/basic.mp4"
    )
    
    new_scene = Scene()
    audio = AudioElement("sample_asset/short1.wav").set_volume(3)
    text = (
        TextElement("Short1", size=42, font_path="sample_asset/NotoSansJP-Bold.ttf")
            .set_duration(audio.duration+0.25)
            .position(x=1920//2, y=950, anchor="center")
            .set_alignment("center")
            .set_background(color=[0, 0, 0], alpha=150, padding=30)
            .set_corner_radius(20)
    )
    img = (
        # ImageElement(Image.open(("sample_asset/zundamon.png")))
        ImageElement("sample_asset/zundamon.png")
            .set_scale(0.25)
            .position(x=50, y=1030, anchor="bottom-left")
            .set_duration(3)
    )
    new_scene.add(img)
    new_scene.add(audio)
    new_scene.add(text)

    master_scene.add(new_scene)
    master_scene.render()
    
main()


