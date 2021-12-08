# Question 03 - run 'python assignment_11.py cam_out.mp4' in the terminal
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

# Get and print video information
frame_width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv.CAP_PROP_FPS)
frame_count = capture.get(cv.CAP_PROP_FRAME_COUNT)
frame_delay = frame_count/fps

print(f'Frame per seconds: {fps:.2f} fps')
print(f'Video W x H: {frame_width} x {frame_height} px')
print(f'Frame count: {frame_count}')
print(f'Frame delay: {frame_delay:.2f} ms')

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
    k = cv.waitKey(int(frame_delay))

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