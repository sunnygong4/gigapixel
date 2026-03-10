# Gigapixel — Sunny Gong

A professional website to showcase 500+ megapixel photos with smooth zoom and pan, powered by [OpenSeadragon](https://openseadragon.github.io/). Deploy at **gigapixel.sunnygong.com** or on your own server.

## Features

- **Smooth zoom & pan** — Explore massive images without loading the full file
- **Auto dimensions** — Resolution and megapixel count shown automatically
- **Download button** — Optional link to full-resolution original
- **Tile Maker app** — Desktop GUI to convert JPG/TIFF to DZI tiles

## Quick Start

### 1. Install libvips & pyvips

```bash
# Windows
choco install vips
pip install pyvips

# Mac
brew install vips
pip install pyvips

# Linux
sudo apt install libvips
pip install pyvips
```

### 2. Convert images with the Tile Maker app

```bash
cd tile-maker
python tile_maker.py
```

Select your large JPG/TIFF, choose the output folder (use `images` in the project root for paths to work), adjust options, and click **Generate tiles**. The app prints a `photos.js` snippet you can paste.

### 3. Add photos to the gallery

Edit `photos.js` and add each photo (paste the snippet from Tile Maker):

```javascript
{
  dzi: 'images/photo-name/photo-name.dzi',
  thumb: 'images/photo-name/thumb.jpg',
  title: 'Photo Title',
  description: '512 MP • Location',
  width: 22360,
  height: 22360,
  downloadUrl: 'images/photo-name/full.jpg'  // optional: host original for download
}
```

Dimensions are auto-fetched from the DZI if `width`/`height` are omitted.

## Deploy on Your Own Server

### Option A: nginx

1. Copy the project to your server (e.g. `/var/www/gigapixel`).
2. Add an nginx site config:

```nginx
server {
    listen 80;
    server_name gigapixel.sunnygong.com;
    root /var/www/gigapixel;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    # Enable gzip for tile JSON/XML
    gzip on;
    gzip_types application/xml application/json;

    # Optional: cache static assets
    location ~* \.(dzi|jpg|jpeg|png|js|css)$ {
        expires 7d;
        add_header Cache-Control "public, immutable";
    }
}
```

3. `sudo nginx -t` then reload nginx.
4. Point DNS: `gigapixel` → your server IP.

### Option B: Caddy

```bash
cd /var/www/gigapixel
caddy file-server --listen :80 --root .
```

Or use a Caddyfile with `gigapixel.sunnygong.com` and TLS.

### Option C: Python / Node (simple serve)

```bash
# Python
cd Gigapixel
python -m http.server 8080

# Node
npx serve . -l 8080
```

Use a process manager (systemd, PM2) or reverse proxy (nginx, Caddy) in front for production.

### Option D: Docker

Create `Dockerfile`:

```dockerfile
FROM nginx:alpine
COPY . /usr/share/nginx/html
```

Then:

```bash
docker build -t gigapixel .
docker run -p 80:80 gigapixel
```

## Project Structure

```
Gigapixel/
├── index.html          # Main site
├── photos.js           # Gallery config
├── images/             # DZI tiles & thumbnails
│   └── photo-name/
│       ├── photo-name.dzi
│       ├── photo-name_files/
│       ├── thumb.jpg
│       └── manifest.json
├── tile-maker/
│   └── tile_maker.py   # Desktop tile generator
├── generate-tiles.py   # CLI tile generator
└── README.md
```

## Tile Maker App

Run `python tile-maker/tile_maker.py` to open the GUI:

- **Input**: JPG, TIFF, PNG, WebP, BMP
- **Output**: Folder for DZI tiles (use `images` in the project)
- **Options**: Tile size (128–512px), JPEG quality
- Generates: `.dzi`, tiles, thumbnail, `manifest.json`, and a `photos.js` snippet

## Download Button

To enable downloads, host the original full-res image and set `downloadUrl` in `photos.js`:

```javascript
downloadUrl: 'images/photo-name/original.jpg'
```

Or use an external URL. If omitted, the download button is hidden.

## Tips for 500MP+ Photos

- **Storage:** 500MP can produce 500MB–2GB of tiles. Host the `images/` folder on your server or a CDN.
- **Quality:** 85% JPEG is a good default; lower = smaller tiles.
- **Tile size:** 256px is standard; 512px reduces tile count for very large images.

## License

Your photos, your rights. OpenSeadragon is BSD-licensed.
