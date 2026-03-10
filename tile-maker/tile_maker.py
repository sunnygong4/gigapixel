#!/usr/bin/env python3
"""
Gigapixel Tile Maker — Desktop app to convert large JPG/TIFF images to DZI tiles.

Requires: pip install pyvips
Install libvips: https://libvips.org/install.html
  - Windows: choco install vips
  - Mac: brew install vips
  - Linux: apt install libvips

Run: python tile_maker.py
"""

import json
import sys
import threading
import tkinter as tk
from pathlib import Path
from tkinter import ttk, filedialog, messagebox, scrolledtext

# Add parent for sibling imports if needed
sys.path.insert(0, str(Path(__file__).parent))


def run_tiled(master, func, *args, **kwargs):
    """Run func in a thread and schedule callback on main thread."""
    result = [None]
    err = [None]

    def work():
        try:
            result[0] = func(*args, **kwargs)
        except Exception as e:
            err[0] = e

    def on_done():
        if err[0]:
            messagebox.showerror("Error", str(err[0]))
        if result[0] is not None:
            return result[0]

    t = threading.Thread(target=work, daemon=True)
    t.start()
    master.after(100, lambda: _poll_done(master, t, on_done))


def _poll_done(master, thread, on_done):
    if thread.is_alive():
        master.after(100, lambda: _poll_done(master, thread, on_done))
    else:
        on_done()


class TileMakerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gigapixel Tile Maker")
        self.root.minsize(520, 480)
        self.root.geometry("560x540")

        self.input_path = tk.StringVar()
        self.input_files = []  # list of paths for bulk mode
        self.output_path = tk.StringVar()
        self.tile_size = tk.IntVar(value=256)
        self.quality = tk.IntVar(value=85)
        self.is_running = False

        self._build_ui()

    def _build_ui(self):
        main = ttk.Frame(self.root, padding=16)
        main.pack(fill=tk.BOTH, expand=True)

        # Input
        ttk.Label(main, text="Input image(s)").pack(anchor=tk.W)
        row1 = ttk.Frame(main)
        row1.pack(fill=tk.X, pady=(4, 4))
        ttk.Entry(row1, textvariable=self.input_path, width=50).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))
        ttk.Button(row1, text="File", command=self._browse_single).pack(side=tk.RIGHT, padx=(0, 4))
        ttk.Button(row1, text="Multiple…", command=self._browse_multiple).pack(side=tk.RIGHT, padx=(0, 4))
        ttk.Button(row1, text="Folder", command=self._browse_folder).pack(side=tk.RIGHT)

        # Output
        ttk.Label(main, text="Output folder (DZI tiles)").pack(anchor=tk.W)
        row2 = ttk.Frame(main)
        row2.pack(fill=tk.X, pady=(4, 12))
        ttk.Entry(row2, textvariable=self.output_path, width=50).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))
        ttk.Button(row2, text="Browse…", command=self._browse_output).pack(side=tk.RIGHT)

        self.file_list_var = tk.StringVar()
        self.file_list_label = ttk.Label(main, text="", foreground="gray", font=("", 9))
        self.file_list_label.pack(anchor=tk.W, pady=(0, 8))

        # Options
        opts = ttk.LabelFrame(main, text="Options", padding=12)
        opts.pack(fill=tk.X, pady=(0, 12))

        ttk.Label(opts, text="Tile size:").grid(row=0, column=0, sticky=tk.W, padx=(0, 8), pady=4)
        spin_tile = ttk.Spinbox(opts, from_=128, to=512, textvariable=self.tile_size, width=6)
        spin_tile.grid(row=0, column=1, sticky=tk.W, pady=4)

        ttk.Label(opts, text="JPEG quality (1–100):").grid(row=1, column=0, sticky=tk.W, padx=(0, 8), pady=4)
        spin_quality = ttk.Spinbox(opts, from_=50, to=100, textvariable=self.quality, width=6)
        spin_quality.grid(row=1, column=1, sticky=tk.W, pady=4)

        # Progress
        self.progress_var = tk.DoubleVar(value=0)
        self.progress = ttk.Progressbar(main, variable=self.progress_var, maximum=100)
        self.progress.pack(fill=tk.X, pady=(0, 8))

        self.status = ttk.Label(main, text="Ready", foreground="gray")
        self.status.pack(anchor=tk.W)

        # Log
        ttk.Label(main, text="Log").pack(anchor=tk.W, pady=(12, 4))
        self.log = scrolledtext.ScrolledText(main, height=10, font=("Consolas", 10), wrap=tk.WORD)
        self.log.pack(fill=tk.BOTH, expand=True, pady=(0, 12))

        # Buttons
        btn_frame = ttk.Frame(main)
        btn_frame.pack(fill=tk.X)
        self.run_btn = ttk.Button(btn_frame, text="Generate tiles", command=self._run)
        self.run_btn.pack(side=tk.RIGHT)

    def _log(self, msg):
        self.log.insert(tk.END, msg + "\n")
        self.log.see(tk.END)

    def _update_file_list_display(self):
        n = len(self.input_files)
        if n == 0:
            self.file_list_label.config(text="")
        elif n == 1:
            self.file_list_label.config(text=self.input_files[0])
        else:
            self.file_list_label.config(text=f"{n} images selected: " + ", ".join(Path(p).name for p in self.input_files[:5]) + (f" … +{n-5} more" if n > 5 else ""))

    def _browse_single(self):
        path = filedialog.askopenfilename(
            title="Select image",
            filetypes=[
                ("Images", "*.jpg *.jpeg *.tif *.tiff *.png *.webp *.bmp"),
                ("All files", "*.*"),
            ],
        )
        if path:
            self.input_files = [path]
            self.input_path.set(path)
            out = Path(path).parent / "images"
            if not self.output_path.get():
                self.output_path.set(str(out))
            self._update_file_list_display()

    def _browse_multiple(self):
        paths = filedialog.askopenfilenames(
            title="Select images (Ctrl/Shift to select multiple)",
            filetypes=[
                ("Images", "*.jpg *.jpeg *.tif *.tiff *.png *.webp *.bmp"),
                ("All files", "*.*"),
            ],
        )
        if paths:
            self.input_files = list(paths)
            self.input_path.set(paths[0] if len(paths) == 1 else f"{len(paths)} files")
            if not self.output_path.get():
                self.output_path.set(str(Path(paths[0]).parent / "images"))
            self._update_file_list_display()

    def _browse_folder(self):
        path = filedialog.askdirectory(title="Select folder with images")
        if path:
            exts = {".jpg", ".jpeg", ".tif", ".tiff", ".png", ".webp", ".bmp"}
            files = sorted(
                str(p) for p in Path(path).iterdir()
                if p.is_file() and p.suffix.lower() in exts
            )
            if not files:
                messagebox.showinfo("No images", f"No image files found in:\n{path}")
                return
            self.input_files = files
            self.input_path.set(path)
            if not self.output_path.get():
                self.output_path.set(str(Path(path) / "images"))
            self._update_file_list_display()

    def _browse_output(self):
        path = filedialog.askdirectory(title="Output folder")
        if path:
            self.output_path.set(path)

    def _run(self):
        files = self.input_files if self.input_files else []
        if not files:
            inp = self.input_path.get().strip()
            if inp and Path(inp).is_file():
                files = [inp]
            elif inp and Path(inp).is_dir():
                exts = {".jpg", ".jpeg", ".tif", ".tiff", ".png", ".webp", ".bmp"}
                files = sorted(str(p) for p in Path(inp).iterdir() if p.is_file() and p.suffix.lower() in exts)
        if not files:
            messagebox.showwarning("Missing input", "Select an image file or folder.")
            return
        out = self.output_path.get().strip()
        if not out:
            messagebox.showwarning("Missing output", "Select an output folder.")
            return

        try:
            ts = int(self.tile_size.get())
            q = int(self.quality.get())
        except ValueError:
            messagebox.showerror("Invalid options", "Tile size and quality must be numbers.")
            return

        self.is_running = True
        self.run_btn.config(state=tk.DISABLED)
        self.progress_var.set(0)
        self.log.delete(1.0, tk.END)

        def thread_main():
            try:
                self._process_batch(files, out, ts, q)
            finally:
                self.root.after(0, lambda: self._batch_done(len(files)))

        t = threading.Thread(target=thread_main, daemon=True)
        t.start()

    def _batch_done(self, count):
        self.is_running = False
        self.run_btn.config(state=tk.NORMAL)
        self.progress_var.set(100)
        messagebox.showinfo("Complete", f"Processed {count} image(s).\n\nCheck the log for photos.js snippets.")

    def _process_batch(self, files: list, out: str, tile_size: int, quality: int):
        try:
            import pyvips
        except ImportError:
            self.root.after(0, lambda: self._log("Error: pyvips not installed. Run: pip install pyvips"))
            self.root.after(0, lambda: self._log("Also install libvips: choco install vips (Windows) / brew install vips (Mac)"))
            return

        out_dir = Path(out)
        total = len(files)
        snippets = []

        for i, inp in enumerate(files):
            path = Path(inp)
            if not path.exists():
                self.root.after(0, lambda p=path: self._log(f"Skipping (not found): {p}"))
                continue

            name = path.stem
            out_folder = out_dir / name
            out_folder.mkdir(parents=True, exist_ok=True)

            progress = int((i / total) * 100)
            self.root.after(0, lambda p=progress: self.progress_var.set(p))
            self.root.after(0, lambda n=name: self._status(f"Processing {i+1}/{total}: {n}"))
            self.root.after(0, lambda n=name: self._log(f"[{i+1}/{total}] {n}"))

            try:
                img = pyvips.Image.new_from_file(str(path))
            except Exception as e:
                self.root.after(0, lambda n=name, err=str(e): self._log(f"  Error: {err}"))
                continue

            w, h = img.width, img.height
            mp = w * h / 1e6
            self.root.after(0, lambda w=w, h=h, mp=mp: self._log(f"  Size: {w:,} × {h:,} px ({mp:.1f} MP)"))

            img.dzsave(
                str(out_folder / name),
                tile_size=tile_size,
                overlap=1,
                suffix=".jpg",
                Q=quality,
                depth="onepixel",
            )
            self.root.after(0, lambda p=out_folder, n=name: self._log(f"  DZI: {p / f'{n}.dzi'}"))

            thumb_path = out_folder / "thumb.jpg"
            thumb = img.thumbnail_image(1024, height=768)
            thumb.jpegsave(str(thumb_path), Q=85)

            manifest = {
                "name": name,
                "width": w,
                "height": h,
                "megapixels": round(mp, 1),
                "dzi": f"images/{name}/{name}.dzi",
                "thumb": f"images/{name}/thumb.jpg",
            }
            with open(out_folder / "manifest.json", "w") as f:
                json.dump(manifest, f, indent=2)

            safe_title = name.replace("_", " ").replace("-", " ").title().replace("'", "\\'")
            snippet = f"""  {{
    dzi: 'images/{name}/{name}.dzi',
    thumb: 'images/{name}/thumb.jpg',
    title: '{safe_title}',
    description: '{int(mp)} MP',
    width: {w},
    height: {h},
    downloadUrl: 'images/{name}/original.jpg'
  }},\n"""
            snippets.append(snippet)

        self.root.after(0, lambda: self.progress_var.set(100))
        self.root.after(0, lambda: self._status("Done"))
        if snippets:
            combined = "\nAdd to photos.js:\n" + "".join(snippets)
            self.root.after(0, lambda s=combined: self._log(s))

    def _status(self, text):
        self.status.config(text=text)


def main():
    app = TileMakerApp()
    app.root.mainloop()


if __name__ == "__main__":
    main()
