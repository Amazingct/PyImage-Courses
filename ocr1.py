import pytesseract
import argparse
import cv2

# tell python when Tesseract is installed if not stored in main drive
# pytesseract.pytesseract.tesseract_cmd = r'A:\tesseract\tesseract.exe'

# argument passing
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

# read image and convert to RGB
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# OCR using tesseract
text = pytesseract.image_to_string(image)
print(text)
