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
    print(f"DEBUG: short1.wav duration: {audio.duration}, start_time: {audio.start_time}")
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
    print(f"DEBUG: new_scene duration after adding audio+text: {new_scene.duration}")
    new_section.add(new_scene)
    print(f"DEBUG: new_section duration after adding new_scene: {new_section.duration}")
    
    new_scene = Scene()
    audio = AudioElement("sample_asset/short2.wav").set_volume(3)
    print(f"DEBUG: short2.wav duration: {audio.duration}, start_time: {audio.start_time}")
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
    print(f"DEBUG: new_scene duration after adding audio+text: {new_scene.duration}")
    new_section.add(new_scene)
    print(f"DEBUG: new_section duration after adding new_scene: {new_section.duration}")
    
    new_scene = Scene()
    audio = AudioElement("sample_asset/short3.wav").set_volume(3)
    print(f"DEBUG: short3.wav duration: {audio.duration}, start_time: {audio.start_time}")
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
    print(f"DEBUG: new_scene duration after adding audio+text: {new_scene.duration}")
    new_section.add(new_scene)
    print(f"DEBUG: new_section duration after adding new_scene: {new_section.duration}")
    
    opening_scene.add(new_section)
    print(f"DEBUG: opening_scene duration after adding new_section: {opening_scene.duration}")
    
    master_scene.add(opening_scene)
    print(f"DEBUG: master_scene total_duration after adding opening_scene: {master_scene.total_duration}")
    
    # Check audio elements after collecting
    print(f"DEBUG: Collected {len(master_scene.audio_elements)} audio elements:")
    for i, audio_elem in enumerate(master_scene.audio_elements):
        print(f"  Audio {i}: path={audio_elem.audio_path}, start_time={audio_elem.start_time}, duration={audio_elem.duration}")

    master_scene.render()
    
main()