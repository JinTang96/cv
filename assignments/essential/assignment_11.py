import cv2 as cv
import sys

print(f'Argument array \n{sys.argv}')
print('>>> 1st argument: ', sys.argv[0])

path = sys.argv[1]

# Read video from path
capture = cv.VideoCapture(path)

# Check camera connection
if capture.isOpened() is False:
    print("Error opening camera 0.")
    exit()

else:
    print("Turning the camera on..")

while capture.isOpened():
    # Capture frames
    ret, frame = capture.read()

    # Stop loop if no frame return
    if not ret:
        print("No frame is returned, stop looping.")
        break

    else:
        None

    # Display the video
    cv.imshow("Camera frame", frame)

    # Set frame delay
    k = cv.waitKey(1)

    # Exit when 'z' key is pressed
    if k == ord("z"):
        break
    else:
        None
else:
    print("Please reconnect the camera.")

# Close the video
capture.release()
cv.destroyAllWindows()