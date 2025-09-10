# PYTHONPATH=$(pwd) python3 -m tests.nested_scenes

from framekit.master_scene_element import MasterScene
from framekit.scene_element import Scene
from framekit.text_element import TextElement
from framekit.audio_element import AudioElement

def test_basic_nested_scenes():
    """基本的なネストしたシーンのテスト"""
    
    print("=== Basic Nested Scenes Test ===")
    
    # マスターシーンを作成
    master = MasterScene(width=1920, height=1080, fps=30, quality="low")
    master.set_output("nested_basic.mp4")
    
    # 親シーンを作成
    parent_scene = Scene()
    
    # 子シーン1: タイトル部分
    title_scene = Scene()
    title_text = (
        TextElement("メインタイトル", size=64, color=(255, 255, 255))
            .position(960, 200, anchor="center")
            .start_at(0)
            .set_duration(3)
            .set_background((0, 0, 0), alpha=128, padding=20)
            .set_corner_radius(10)
    )
    title_scene.add(title_text)
    title_scene.start_at(0)
    
    # 子シーン2: サブタイトル部分
    subtitle_scene = Scene()
    subtitle_text = (
        TextElement("サブタイトル", size=36, color=(255, 255, 0))
            .position(960, 350, anchor="center")
            .start_at(0)
            .set_duration(2.5)
            .set_background((50, 50, 50), alpha=200, padding=15)
            .set_corner_radius(8)
    )
    subtitle_scene.add(subtitle_text)
    subtitle_scene.start_at(1)  # 1秒後に開始
    
    # 子シーンを親シーンに追加
    parent_scene.add(title_scene)
    parent_scene.add(subtitle_scene)
    
    # 親シーンに直接的な要素も追加
    footer_text = (
        TextElement("フッター情報", size=24, color=(200, 200, 200))
            .position(960, 900, anchor="center")
            .start_at(0.5)
            .set_duration(3)
    )
    parent_scene.add(footer_text)
    
    # 親シーンの開始時間を設定
    parent_scene.start_at(0)
    
    # マスターシーンに追加
    master.add(parent_scene)
    
    print(f"タイトルシーン時間: {title_scene.duration}秒")
    print(f"サブタイトルシーン時間: {subtitle_scene.duration}秒")
    print(f"親シーン時間: {parent_scene.duration}秒")
    print(f"全体時間: {master.total_duration}秒")
    
    # レンダリング
    master.render()
    print("✅ 基本ネストシーンテスト完了")


def test_deep_nested_scenes():
    """3階層のネストシーンテスト"""
    
    print("\n=== Deep Nested Scenes Test ===")
    
    master = MasterScene(width=1920, height=1080, fps=30, quality="low")
    master.set_output("nested_deep.mp4")
    
    # レベル1: トップシーン
    top_scene = Scene()
    
    # レベル2: セクションシーン
    section_scene = Scene()
    
    # レベル3: アイテムシーン
    item_scene = Scene()
    
    # 最深レベルに要素を追加
    item_text = (
        TextElement("アイテム", size=32, color=(0, 255, 0))
            .position(200, 200)
            .start_at(0)
            .set_duration(1.5)
    )
    item_scene.add(item_text)
    item_scene.start_at(0.5)
    
    # セクションレベルに要素とアイテムシーンを追加
    section_text = (
        TextElement("セクション", size=40, color=(255, 0, 0))
            .position(200, 300)
            .start_at(0)
            .set_duration(2.5)
    )
    section_scene.add(section_text)
    section_scene.add(item_scene)
    section_scene.start_at(1)
    
    # トップレベルに要素とセクションシーンを追加
    top_text = (
        TextElement("トップレベル", size=48, color=(0, 0, 255))
            .position(200, 100)
            .start_at(0)
            .set_duration(4)
    )
    top_scene.add(top_text)
    top_scene.add(section_scene)
    top_scene.start_at(0)
    
    master.add(top_scene)
    
    print(f"アイテムシーン時間: {item_scene.duration}秒")
    print(f"セクションシーン時間: {section_scene.duration}秒")
    print(f"トップシーン時間: {top_scene.duration}秒")
    print(f"全体時間: {master.total_duration}秒")
    
    master.render()
    print("✅ 深いネストシーンテスト完了")


def test_scene_with_audio():
    """オーディオ付きネストシーンテスト"""
    
    print("\n=== Nested Scenes with Audio Test ===")
    
    master = MasterScene(width=1920, height=1080, fps=30, quality="low")
    master.set_output("nested_audio.mp4")
    
    # メインシーン
    main_scene = Scene()
    
    # オーディオ付きサブシーン
    audio_scene = Scene()
    
    try:
        # オーディオ要素
        audio = (
            AudioElement("sample_asset/effect1.mp3")
                .set_volume(0.8)
                .start_at(0)
        )
        
        # オーディオに合わせたテキスト
        audio_text = (
            TextElement("音声付きシーン", size=42, color=(255, 100, 255))
                .position(960, 400, anchor="center")
                .start_at(0)
                .set_duration(audio.duration)
                .set_background((0, 0, 0), alpha=150, padding=25)
        )
        
        audio_scene.add(audio)
        audio_scene.add(audio_text)
        audio_scene.start_at(1)  # 1秒後に開始
        
        # メインシーンにヘッダーテキストとオーディオシーンを追加
        header_text = (
            TextElement("オーディオテストシーン", size=48, color=(255, 255, 255))
                .position(960, 200, anchor="center")
                .start_at(0)
                .set_duration(3)
        )
        
        main_scene.add(header_text)
        main_scene.add(audio_scene)
        main_scene.start_at(0)
        
        master.add(main_scene)
        
        print(f"オーディオシーン時間: {audio_scene.duration}秒")
        print(f"メインシーン時間: {main_scene.duration}秒")
        print(f"収集されたオーディオ要素数: {len(master.audio_elements)}")
        if master.audio_elements:
            print(f"オーディオ開始時間（ネスト後）: {master.audio_elements[0].start_time}秒")
        
        master.render()
        print("✅ オーディオ付きネストシーンテスト完了")
        
    except FileNotFoundError:
        print("⚠️  サンプルオーディオファイルが見つかりません（sample_asset/effect1.mp3）")
        print("    オーディオテストをスキップします")


def test_reusable_scenes():
    """再利用可能シーンのテスト"""
    
    print("\n=== Reusable Scenes Test ===")
    
    master = MasterScene(width=1920, height=1080, fps=30, quality="low")
    master.set_output("nested_reusable.mp4")
    
    # 再利用可能なシーンコンポーネントを作成
    def create_info_card(title: str, color: tuple):
        """情報カードシーンを作成する関数"""
        card_scene = Scene()
        
        card_text = (
            TextElement(title, size=36, color=color)
                .position(960, 400, anchor="center")
                .start_at(0)
                .set_duration(2)
                .set_background((50, 50, 50), alpha=200, padding=30)
                .set_corner_radius(15)
        )
        
        card_scene.add(card_text)
        return card_scene
    
    # 複数のカードを異なるタイミングで使用
    card1 = create_info_card("情報カード 1", (255, 100, 100))
    card1.start_at(0)
    
    card2 = create_info_card("情報カード 2", (100, 255, 100))
    card2.start_at(2.5)
    
    card3 = create_info_card("情報カード 3", (100, 100, 255))
    card3.start_at(5)
    
    # メインシーンに追加
    main_scene = Scene()
    main_scene.add(card1)
    main_scene.add(card2)
    main_scene.add(card3)
    main_scene.start_at(0)
    
    master.add(main_scene)
    
    print(f"カード1時間: {card1.duration}秒")
    print(f"カード2時間: {card2.duration}秒")
    print(f"カード3時間: {card3.duration}秒")
    print(f"全体時間: {master.total_duration}秒")
    
    master.render()
    print("✅ 再利用可能シーンテスト完了")


def main():
    """すべてのネストシーンテストを実行"""
    
    print("🎬 ネストシーン機能テスト開始\n")
    
    # 各テストを実行
    test_basic_nested_scenes()
    test_deep_nested_scenes()
    test_scene_with_audio()
    test_reusable_scenes()
    
    print("\n🎉 すべてのネストシーンテストが完了しました！")
    print("出力ファイル:")
    print("  - output/nested_basic.mp4")
    print("  - output/nested_deep.mp4")
    print("  - output/nested_audio.mp4")
    print("  - output/nested_reusable.mp4")


if __name__ == "__main__":
    main()