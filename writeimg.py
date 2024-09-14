import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

save_dir = 'dataset'
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)
saved_frames = 0

while saved_frames < 30:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Face Detection', frame)
    if len(faces) > 0:
        cv2.imwrite(f"{save_dir}/frame_{saved_frames:02d}.png", frame)
        saved_frames += 1
        print(f"Saved frame {saved_frames} with detected faces.")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
