# Computer Vision - CV 
import cv2
cap = cv2.VideoCapture(0)

while True:
    _ , frame = cap.read()

    cv2.imshow("Maruf's Camera", frame )
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
