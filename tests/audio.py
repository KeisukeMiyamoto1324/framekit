from framekit import MasterScene, Scene, TextElement, AudioElement

def main():
    # Create master scene
    master_scene = MasterScene(
        width=1920, 
        height=1080, 
        fps=60,
        output_filename="output/basic.mp4"
    )
    
    # Scene 1: Title
    scene1 = Scene()
    effect1 = AudioElement("sample_asset/short1.wav")
    title = (
        TextElement("FrameKit", size=80, color=(255, 255, 255))
            .position(960, 400, anchor="center")
            .start_at(0)
            .set_duration(effect1.duration)
    )
    scene1.add(title)
    scene1.add(effect1)
    
    # Scene 2: Subtitle
    scene2 = Scene()
    effect2 = AudioElement("sample_asset/short2.wav")
    subtitle = (
        TextElement("Programmatic Video Generation with Python", size=40, color=(200, 200, 255))
            .position(960, 500, anchor="center")
            .start_at(0)
            .set_duration(effect2.duration)
    )
    scene2.add(subtitle)
    scene2.add(effect2)
    
    # Scene 3: Description
    scene3 = Scene()
    description = (
        TextElement("OpenGL Rendering • Text • Images • Video • Audio", size=30, color=(150, 255, 150))
            .position(960, 600, anchor="center")
            .start_at(0)
            .set_duration(2)
    )
    effect3 = AudioElement("sample_asset/effect1.mp3")
    scene3.add(description)
    scene3.add(effect3)
    
    scene = Scene()
    
    # Add scenes with sequential timing
    scene.add(scene1)  # 0-2 seconds
    scene.add(scene2)  # 2-4 seconds
    scene.add(scene3)  # 4-6 seconds
    
    # Render
    master_scene.add(scene)
    master_scene.render()

if __name__ == "__main__":
    main()