# PYTHONPATH=$(pwd) python3 -m tests.simple_nested
# Simple nested scene example

from framekit.master_scene_element import MasterScene
from framekit.scene_element import Scene
from framekit.text_element import TextElement

def main():

    # Create master scene
    master = MasterScene(width=1920, height=1080, fps=30, quality="low")
    master.set_output("simple_nested_example.mp4")
    
    # === Method 1: Traditional approach (for comparison) ===
    traditional_scene = Scene()
    
    text1 = TextElement("Traditional Method", size=48, color=(255, 255, 255)).position(100, 100).start_at(0).set_duration(2)
    text2 = TextElement("All elements in one scene", size=36, color=(255, 255, 0)).position(100, 200).start_at(1).set_duration(2)
    text3 = TextElement("Add elements directly", size=36, color=(255, 0, 255)).position(100, 300).start_at(2).set_duration(2)
    
    traditional_scene.add(text1)
    traditional_scene.add(text2)
    traditional_scene.add(text3)
    traditional_scene.start_at(0)
    
    # === Method 2: Using nested scenes ===
    nested_main_scene = Scene()
    
    # Separate header as a scene
    header_scene = Scene()
    header_text = TextElement("Nested Scene Method", size=48, color=(255, 255, 255)).position(100, 500).start_at(0).set_duration(2)
    header_scene.add(header_text)
    header_scene.start_at(0)
    
    # Separate content as a scene
    content_scene = Scene()
    content_text1 = TextElement("Header and content", size=36, color=(255, 255, 0)).position(100, 600).start_at(1).set_duration(2)
    content_text2 = TextElement("managed separately", size=36, color=(255, 0, 255)).position(100, 700).start_at(2).set_duration(2)
    content_scene.add(content_text1)
    content_scene.add(content_text2)
    content_scene.start_at(1)
    
    # Add sub-scenes to main scene
    nested_main_scene.add(header_scene)
    nested_main_scene.add(content_scene)
    nested_main_scene.start_at(4)  # Display after traditional method
    
    # Add both to master scene
    master.add(traditional_scene)
    master.add(nested_main_scene)

    # Render
    master.render()

if __name__ == "__main__":
    main()