# ---------------------------------------------------------
# Chrome playback compatibility fix plan
# ---------------------------------------------------------
- Replace the OpenCV `mp4v` writer in `framekit/master_scene_element.py` with an FFmpeg-powered libx264 pipeline so the project always emits baseline H.264 that every browser decodes, eliminating fallback paths.
- Emit a single warning when libx264 is missing that points developers to install FFmpeg with x264 support, instead of juggling alternate codecs.
- Teach the existing audio mux routine to consume the new encoded video (or interim lossless file) while preserving timing and existing filters.
- Re-render `python tests/basic.py` (and optionally `tests/multi_scene.py`) to validate Chrome playback, keeping generated files out of version control.
