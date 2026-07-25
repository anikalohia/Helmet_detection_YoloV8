import cv2
from ultralytics import YOLO

model = YOLO("best.pt")
cap = cv2.VideoCapture("sample_results/test_video.mp4")

while True:
    ret,frame = cap.read()
    if not ret:
        break
    results = model(frame)
    for result in results:
        for box in result.boxes:
            x1,y1,x2,y2 = map(int,box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            
            # Head (No Helmet)
            if model.names[cls] == "head":
                color = (0, 0, 255)      # Red (BGR)
                label = f"No Helmet {conf:.2f}"

            # Helmet
            elif model.names[cls] == "helmet":
                color = (0, 255, 0)      # Green
                label = f"Helmet {conf:.2f}"

            # Person
            else:
                color = (255, 0, 0)      # Blue
                label = f"Person {conf:.2f}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            cv2.putText(frame,
                        label,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        color,
                        2)

    cv2.imshow("Helmet Detection", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
            
