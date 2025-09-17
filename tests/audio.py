from framekit import MasterScene, Scene, TextElement, AudioElement

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
    
    opening_scene = Scene()
    new_section = Scene()
    
    new_scene = Scene()
    audio = AudioElement("sample_asset/short1.wav").set_volume(3)
    text = (
        TextElement("Short1", size=42, font_path="resource/NotoSansJP-ExtraBold.ttf")
            .set_duration(audio.duration+0.25)
            .position(x=1920//2, y=950, anchor="center")
            .set_alignment("center")
            .set_background(color=[0, 0, 0], alpha=150, padding=30)
            .set_corner_radius(20)
    )
    new_scene.add(audio)
    new_scene.add(text)
    new_section.add(new_scene)
    
    new_scene = Scene()
    audio = AudioElement("sample_asset/short2.wav").set_volume(3)
    text = (
        TextElement("Short2", size=42, font_path="resource/NotoSansJP-ExtraBold.ttf")
            .set_duration(audio.duration+0.25)
            .position(x=1920//2, y=950, anchor="center")
            .set_alignment("center")
            .set_background(color=[0, 0, 0], alpha=150, padding=30)
            .set_corner_radius(20)
    )
    new_scene.add(audio)
    new_scene.add(text)
    new_section.add(new_scene)
    
    new_scene = Scene()
    audio = AudioElement("sample_asset/short3.wav").set_volume(3)
    text = (
        TextElement("Short3", size=42, font_path="resource/NotoSansJP-ExtraBold.ttf")
            .set_duration(audio.duration+0.25)
            .position(x=1920//2, y=950, anchor="center")
            .set_alignment("center")
            .set_background(color=[0, 0, 0], alpha=150, padding=30)
            .set_corner_radius(20)
    )
    new_scene.add(audio)
    new_scene.add(text)
    new_section.add(new_scene)
    
    opening_scene.add(new_section)
    
    master_scene.add(opening_scene)

    master_scene.render()
    
main()