
# Image Compression Script using PIL

## Features
- Compresses images while maintaining quality.
- Supports resizing by ratio or custom width and height.
- Automatically converts images to JPEG if specified.
- Reports original and new image sizes in human-readable format.
- Handles `OSError` by converting images to RGB mode for compatibility.
- Optimizes images while saving to reduce file size efficiently.

## Dependencies
- Python 3.x
- `Pillow` (Python Imaging Library fork)

## Installation
Install the required dependency with pip:
```bash
pip install Pillow
```

## Usage
1. Place your image in the same directory or provide the correct path.
2. Call the function `compress_img()` with desired parameters:
```python
compress_img("your_image.png", new_size_ratio=0.8, quality=85, to_jpg=True)
```
- `new_size_ratio`: Scaling ratio for image resizing (default: 0.9).
- `quality`: Output image quality (default: 90).
- `width`, `height`: Resize to specific dimensions if provided.
- `to_jpg`: Convert output to `.jpg` (default: True).

## Output
- A compressed version of the original image with `_compressed` appended to the filename.
- Logs of image shape and file size before and after compression.

## Notes
- This script is helpful for preparing images for web use or reducing storage space.
- Best used on `.png`, `.jpeg`, and other common image formats.
