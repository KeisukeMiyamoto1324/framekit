# ネストシーン機能

FrameKitでは、シーンの中に他のシーンを入れる「ネストシーン」機能をサポートしています。これにより、複雑な動画構成を階層的に管理できます。

## 基本的な使い方

### 従来の方法
```python
scene = Scene()
scene.add(TextElement("テキスト1"))
scene.add(TextElement("テキスト2"))
scene.add(TextElement("テキスト3"))
```

### ネストシーンを使用
```python
# 親シーン
parent_scene = Scene()

# 子シーン1
child_scene1 = Scene()
child_scene1.add(TextElement("ヘッダー"))
child_scene1.start_at(0)

# 子シーン2  
child_scene2 = Scene()
child_scene2.add(TextElement("コンテンツ"))
child_scene2.start_at(1)

# 親シーンに子シーンを追加
parent_scene.add(child_scene1)
parent_scene.add(child_scene2)
```

## 利点

1. **整理された構造**: 関連する要素をグループ化
2. **再利用性**: シーンをコンポーネントとして再利用
3. **時間管理**: シーン単位での時間制御が簡単
4. **階層管理**: 複雑な構成を段階的に構築

## 実行例

### 基本テスト
```bash
python tests/nested_scenes.py
```

### シンプルな例
```bash
python tests/simple_nested.py
```

## 注意事項

- ネストしたシーンでも音声の同期は自動的に処理されます
- 時間座標は親シーンからの相対時間で計算されます
- 既存のコードとの互換性は完全に保持されています

## サンプル出力

テストを実行すると以下のファイルが生成されます：
- `output/nested_basic.mp4` - 基本的なネストシーン
- `output/nested_deep.mp4` - 3階層のネストシーン
- `output/nested_audio.mp4` - 音声付きネストシーン
- `output/nested_reusable.mp4` - 再利用可能シーン
- `output/simple_nested_example.mp4` - シンプルな例