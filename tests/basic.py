from framekit import MasterScene, Scene, TextElement

def main():
    # Create master scene
    master_scene = MasterScene(
        width=1920, 
        height=1080, 
        fps=60,
        output_filename="basic.mp4"
    )
    
    # Create scene
    scene = Scene()
    
    # Title
    title = (
        TextElement("FrameKit", size=80, color=(255, 255, 255))
            .position(960, 400, anchor="center")
            .start_at(0)
            .set_duration(5)
    )
    scene.add(title)
    
    # Subtitle
    subtitle = (
        TextElement("Programmatic Video Generation with Python", size=40, color=(200, 200, 255))
            .position(960, 500, anchor="center")
            .start_at(1)
            .set_duration(4)
    )
    scene.add(subtitle)
    
    # Description
    description = (
        TextElement("OpenGL Rendering • Text • Images • Video • Audio", size=30, color=(150, 255, 150))
            .position(960, 600, anchor="center")
            .start_at(2)
            .set_duration(3)
    )
    scene.add(description)
    
    # Render
    master_scene.add(scene)
    master_scene.render()

if __name__ == "__main__":
    main()