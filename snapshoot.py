import cv2

# Initialise la caméra
CAMERA = cv2.VideoCapture(0)

if not CAMERA.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra.")
    exit()

while True:  # This loop continuously captures and displays frames.
    ret, frame = CAMERA.read()  # Captures a frame from the camera.

    if not ret:  # Checks if the frame was captured successfully.
        print("Erreur : Impossible de lire l'image.")
        break

    # Définir la taille de la fenêtre de capture (format 1:1)
    height, width, _ = frame.shape  # Gets the height and width of the captured frame.
    min_dimension = min(height, width)  # Determines the smaller dimension (either height or width).  This will be the side length of our square.
    x = (width - min_dimension) // 2  # Calculates the x-offset for cropping.  This centers the square horizontally.
    y = (height - min_dimension) // 2  # Calculates the y-offset for cropping. This centers the square vertically.
    cropped_frame = frame[y:y+min_dimension, x:x+min_dimension] # Crops the frame to a square.

    # Affiche l'image
    cv2.imshow('Flux de la Webcam', cropped_frame) # Displays the *cropped* frame.

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Checks if the 'q' key was pressed.
        break  # Exits the loop if 'q' is pressed.

CAMERA.release() # Releases the camera.
cv2.destroyAllWindows()  # Closes the display window.
