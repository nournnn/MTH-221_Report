# MATLAB and Python Implementation Files

This project includes source code files used to show bicubic interpolation for image scaling in both MATLAB and Python environments.

## Included Files

### MATLAB File

**bicubic_matlab.m**
This script reads an input image, applies bicubic interpolation using MATLAB built-in functions, and displays the original and resized images for comparison.

### Python File

**bicubic_python.py**
This script uses OpenCV to load an input image, perform bicubic image scaling, and save/display the resized result.

## Requirements

### MATLAB

* MATLAB R2020a or later (recommended)
* Image Processing Toolbox

### Python

* Python 3.x
* OpenCV (`cv2`)
* NumPy (optional)

Install OpenCV using:

```bash
pip install opencv-python
```

## How to Run

### MATLAB

Open MATLAB, navigate to the project folder, then run:

```matlab
bicubic_matlab
```

### Python

Run in terminal or command prompt:

```bash
python bicubic_python.py
```

## Output

Both implementations generate a resized image using bicubic interpolation and allow comparison with the original image.
