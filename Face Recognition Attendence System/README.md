
# Face Recognition Attendance System

## Features
- Real-time face recognition using webcam input.
- Attendance marking for recognized individuals by logging their name and time.
- Supports multiple known faces (can be extended by adding more face images and encodings).
- Creates a CSV file named with the current date to store attendance records.
- Displays live video with recognized faces' names and attendance status.
- Removes recognized individuals from the expected attendance list to avoid duplicate entries.
- Stops attendance on pressing the "q" key.

## Dependencies
- Python 3.x
- `face_recognition` library (for face detection and recognition)
- `opencv-python` (cv2) (for video capturing and image processing)
- `numpy` (for numerical operations)
- `datetime` (for date and time management)
- `csv` (for writing attendance data to CSV file)

## Usage
1. Install dependencies:
   ```bash
   pip install face_recognition opencv-python numpy
   ```
2. Prepare known faces:
   - Add images of known individuals inside the `faces` directory.
   - Update the code to load and encode these images.
3. Run the script.
4. The program will open a webcam window and detect known faces.
5. Press "q" to quit and save the attendance CSV file for the current date.

## Output
- Generates a CSV file named `YYYY-MM-DD.csv` containing attendance entries with the person's name and timestamp.

## Notes
- Ensure good lighting and a clear view of faces for better recognition accuracy.
- Extend the list of known faces by adding more images and corresponding encodings in the script.
