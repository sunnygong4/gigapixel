# Gigapixel Tile Maker

Desktop app to convert large JPG and TIFF images into DZI tiles for the gigapixel viewer.

## Requirements

- **Python 3.7+**
- **pyvips** — `pip install pyvips`
- **libvips** — [Install guide](https://libvips.org/install.html)
  - Windows: `choco install vips`
  - Mac: `brew install vips`
  - Linux: `apt install libvips` (or equivalent)

## Usage

```bash
python tile_maker.py
```

1. **Input** — **File** (single), **Multiple** (Ctrl/Shift to multi-select), or **Folder** (bulk)
2. Choose output folder — use the project’s `images` folder so paths match
3. Optionally adjust tile size (256 default) and JPEG quality (85 default)
4. Click **Generate tiles**
5. Copy the `photos.js` snippet(s) from the log and paste into `photos.js`

## Output

- `{name}.dzi` — DZI manifest
- `{name}_files/` — tile pyramid
- `thumb.jpg` — gallery thumbnail
- `manifest.json` — dimensions and paths
