# Smart-Cursor

Python Script to use the mouse with your hand✨ 

## Installation

Open the terminal and run the following commands

```bash
git clone https://github.com/Bhanu-mbvg/Smart-Cursor.git
pip install -r requirements.txt
python Cursor.py

```

## Usage
This application works by detecting dips/low contours (DEFECTS) present on our hands. For each finger, we have 1 less DEFECT.

3 Fingers = 2 Defects => For moving the cursor  
4 Fingers = 3 Defects => Left click  
5 Fingers = 4 Defects => Right click

## Technical Stack  

1. OpenCV
2. Pyautogui
3. Numpy

## License
[MIT](https://choosealicense.com/licenses/mit/)
