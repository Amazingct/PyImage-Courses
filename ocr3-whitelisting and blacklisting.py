import pytesseract
import argparse
import cv2

# tell python when Tesseract is installed if not stored in main drive
# pytesseract.pytesseract.tesseract_cmd = r'A:\tesseract\tesseract.exe'

image = "data/image2.png"
# read image and convert to RGB
image = cv2.imread(image)

# tesseract works with RGB only
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
options = ""

whitelist = "-c tessedit_char_blacklist=0"  # include the characters (0)
blacklist = "-c tessedit_char_blacklist=01"  # exclude the given characters (0,1)

# OCR using tesseract
text = pytesseract.image_to_string(image, config=blacklist)
print(text)
