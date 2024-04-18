import cv2

# Load the image
img = cv2.imread('comedor4.png')

# Create a window to display the image
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)  # WINDOW_NORMAL allows resizing

# Resize the window to fit the image
cv2.resizeWindow('Image', img.shape[1], img.shape[0])

# Display the image
cv2.imshow('Image', img)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()