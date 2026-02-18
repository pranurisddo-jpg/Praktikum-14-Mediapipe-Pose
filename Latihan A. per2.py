import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_pose.Pose() as pose:

    while True:
        success, img = cap.read()
        if not success or img is None:
            continue

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        hasil = pose.process(img_rgb)

        teks = "Tangan tidak terangkat"   # default

        if hasil.pose_landmarks:

            mp_draw.draw_landmarks(img, hasil.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            titik = hasil.pose_landmarks.landmark
            tinggi = img.shape[0]

            # ambil posisi pundak & pergelangan
            y_pundak_kiri = int(titik[mp_pose.PoseLandmark.LEFT_SHOULDER].y * tinggi)
            y_tangan_kiri = int(titik[mp_pose.PoseLandmark.LEFT_WRIST].y * tinggi)

            y_pundak_kanan = int(titik[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * tinggi)
            y_tangan_kanan = int(titik[mp_pose.PoseLandmark.RIGHT_WRIST].y * tinggi)

            # cek jika salah satu tangan terangkat
            if y_tangan_kiri < y_pundak_kiri or y_tangan_kanan < y_pundak_kanan:
                teks = "Tangan terangkat"

        # tampilkan teks
        cv2.putText(img, teks, (20,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0,255,0), 2)

        cv2.imshow("Webcam", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
