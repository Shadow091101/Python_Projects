
# Image Resizing Script using OpenCV

## Features
- Resizes images by a specified percentage of the original dimensions.
- Uses OpenCV for fast and efficient image processing.
- Supports reading, resizing, saving, and displaying images.
- Overwrites the original image (if source and destination are the same).

## Dependencies
- Python 3.x
- `opencv-python`

## Installation
Install OpenCV using pip:
```bash
pip install opencv-python
```

## Usage
1. Place your target image in the same directory or provide the full path.
2. Set the `source` and `destination` file paths in the script.
3. Adjust the `scale_percent` value to the desired resize ratio (e.g., 50 for 50%).

### Example:
```python
scale_percent = 50  # Resize image to 50% of original dimensions
```

## Output
- The resized image will be saved at the `destination` path.
- The original image will be displayed in a window.

## Notes
- The destination path in this script is the same as the source path, so it overwrites the original image.
- You can change the `destination` variable to save the resized image as a new file instead.
- Press any key while the image window is open to close it.
