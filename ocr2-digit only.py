import pytesseract
import argparse
import cv2

# tell python when Tesseract is installed if not stored in main drive
# pytesseract.pytesseract.tesseract_cmd = r'A:\tesseract\tesseract.exe'

# argument passing
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-d", "--digits", type=int, default=1, help="read digits only or not")
args = vars(ap.parse_args())

# read image and convert to RGB
image = cv2.imread(args["image"])

# tesseract works with RGB only
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
options = ""

if args["digits"] > 0:
    options = "outputbase digits"

# OCR using tesseract
text = pytesseract.image_to_string(image, config=options)
print(text)
