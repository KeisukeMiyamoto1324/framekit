# Debug nested scene timing
from framekit.master_scene_element import MasterScene
from framekit.scene_element import Scene
from framekit.text_element import TextElement

def debug_nested_timing():
    print("=== Debug Nested Scene Timing ===")
    
    master = MasterScene(width=1920, height=1080, fps=30, quality="low")
    master.set_output("debug_nested.mp4")
    
    # Create deeply nested scenes
    level1_scene = Scene()
    level2_scene = Scene()
    level3_scene = Scene()
    
    # Add text to deepest level
    level3_text = (
        TextElement("Level 3 Text", size=32, color=(255, 0, 0))
            .position(100, 100)
            .start_at(0)
            .set_duration(2)
    )
    level3_scene.add(level3_text)
    print(f"Level 3 scene - start_time: {level3_scene.start_time}, duration: {level3_scene.duration}")
    
    # Add level3 to level2
    level2_scene.add(level3_scene)
    print(f"Level 2 scene after adding level3 - start_time: {level2_scene.start_time}, duration: {level2_scene.duration}")
    print(f"Level 3 scene after being added - start_time: {level3_scene.start_time}, duration: {level3_scene.duration}")
    
    # Add another scene to level2
    level3_scene2 = Scene()
    level3_text2 = (
        TextElement("Level 3 Text 2", size=32, color=(0, 255, 0))
            .position(100, 200)
            .start_at(0)
            .set_duration(1.5)
    )
    level3_scene2.add(level3_text2)
    level2_scene.add(level3_scene2)
    
    print(f"Level 2 scene after adding second level3 - start_time: {level2_scene.start_time}, duration: {level2_scene.duration}")
    print(f"Level 3 scene 2 after being added - start_time: {level3_scene2.start_time}, duration: {level3_scene2.duration}")
    
    # Add level2 to level1
    level1_scene.add(level2_scene)
    print(f"Level 1 scene after adding level2 - start_time: {level1_scene.start_time}, duration: {level1_scene.duration}")
    print(f"Level 2 scene after being added to level1 - start_time: {level2_scene.start_time}, duration: {level2_scene.duration}")
    
    # Add level1 to master
    master.add(level1_scene)
    print(f"Master scene total duration: {master.total_duration}")
    print(f"Level 1 scene after being added to master - start_time: {level1_scene.start_time}, duration: {level1_scene.duration}")
    
    print(f"\nExpected: Video should start immediately with content")
    print(f"Actual: Video duration is {master.total_duration} seconds")
    
    # Don't render, just show timing info
    print("Timing analysis complete")

if __name__ == "__main__":
    debug_nested_timing()