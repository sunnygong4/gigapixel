#!/usr/bin/env python3
"""
Generate DZI (Deep Zoom Image) tiles from high-resolution photos for OpenSeadragon.

Requires: pip install pyvips
Also install libvips: https://libvips.org/install.html
  - Windows: choco install vips
  - Mac: brew install vips
  - Linux: apt install libvips

Usage:
  python generate-tiles.py image.jpg
  python generate-tiles.py image.jpg -o output_folder
  python generate-tiles.py image1.jpg image2.jpg image3.jpg
"""

import argparse
import os
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description='Convert high-res images to DZI tiles for gigapixel viewing'
    )
    parser.add_argument(
        'images',
        nargs='+',
        help='Input image file(s) (JPG, PNG, TIFF, etc.)'
    )
    parser.add_argument(
        '-o', '--output-dir',
        default='images',
        help='Output directory for DZI files (default: images)'
    )
    parser.add_argument(
        '-t', '--tile-size',
        type=int,
        default=256,
        help='Tile size in pixels (default: 256)'
    )
    parser.add_argument(
        '-q', '--quality',
        type=int,
        default=85,
        help='JPEG quality 1-100 (default: 85)'
    )
    args = parser.parse_args()

    try:
        import pyvips
    except ImportError:
        print('Error: pyvips is required. Install with:', file=sys.stderr)
        print('  pip install pyvips', file=sys.stderr)
        print('', file=sys.stderr)
        print('Also install libvips:', file=sys.stderr)
        print('  Windows: choco install vips', file=sys.stderr)
        print('  Mac: brew install vips', file=sys.stderr)
        print('  Linux: apt install libvips', file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for img_path in args.images:
        path = Path(img_path)
        if not path.exists():
            print(f'Skipping {path}: file not found')
            continue

        name = path.stem
        out_folder = output_dir / name
        out_folder.mkdir(parents=True, exist_ok=True)
        dzi_path = out_folder / f'{name}.dzi'

        print(f'Processing {path.name} -> {out_folder}/')
        try:
            img = pyvips.Image.new_from_file(str(path))
            img.dzsave(
                str(out_folder / name),
                tile_size=args.tile_size,
                overlap=1,
                suffix='.jpg',
                Q=args.quality,
                depth='onepixel'
            )
            print(f'  Created {dzi_path}')

            # Create thumbnail for gallery (1024px wide)
            thumb_path = out_folder / 'thumb.jpg'
            thumb = img.thumbnail_image(1024, height=768)
            thumb.jpegsave(str(thumb_path), Q=85)
            print(f'  Created {thumb_path}')

        except Exception as e:
            print(f'  Error: {e}', file=sys.stderr)

    print('\nDone! Add your photos to photos.js and refresh the gallery.')


if __name__ == '__main__':
    main()
