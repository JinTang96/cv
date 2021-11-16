# import library
import cv2 as cv

# Read image from samples/data folder
img_dir = 'C:\sdk\cv\samples/data/starry_night.jpg'
image = cv.imread(img_dir)

# Display image
cv.imshow(img_dir, image)

# Terminate window
cv.waitKey(0)
cv.destroyAllWindows()