
from pytesseract import Output
import pytesseract
import imutils
import cv2

image = "data/image2.png"

# load the input image, convert it from BGR to RGB channel ordering,
# and use Tesseract to determine the text orientation
image = cv2.imread(image)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_osd(rgb, output_type=Output.DICT)

# display the orientation information
print("[INFO] detected orientation: {}".format(
    results["orientation"]))
print("[INFO] rotate by {} degrees to correct".format(
    results["rotate"]))
print("[INFO] detected script: {}".format(results["script"]))

# rotate the image to correct the orientation
rotated = imutils.rotate_bound(image, angle=results["rotate"])

# show the original image and output image after orientation
# correction
cv2.imshow("Original", image)
cv2.imshow("Output", rotated)
cv2.waitKey(0)

