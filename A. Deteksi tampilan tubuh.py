import cv2
import mediapipe as mp
mpose = mp.solutions.pose  # inisiasi mediapipe pose
pose = mpose.Pose()
cap = cv2.VideoCapture(0)  # video dari webcam
while True:
    succes, img = cap.read() #pembacaan image
    if not succes:
        continue
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #konversi warna dari bgr ke rgb
    hasil = pose.process(imgrgb) #ekstraksi dari image
    if hasil.pose_landmarks:
        print("terdeteksi")
    else:
        print("tidak terdeteksi")
    # tampilkan webcam juga di loop ini
    cv2.imshow("webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('n'):
        break
while True:
    success, img = cap.read()
    if not success:
        continue

    cv2.imshow("webcam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
