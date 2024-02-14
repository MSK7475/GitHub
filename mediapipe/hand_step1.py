# pip install mediapipe opencv-python
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)    
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    x1, x2, y1, y2 = 0,0,0,0
    if results.multi_hand_landmarks:
      for hand in results.multi_hand_landmarks:
        for id, lm in enumerate(hand.landmark):
          
          h, w, c = image.shape
          cx, cy = int(lm.x *w), int(lm.y*h)
          if id == 8:
            x1, y1 = cx, cy
            cv2.circle(image, (cx, cy), 10, (0,0,255), cv2.FILLED)
          if id == 12:
            x2, y2 = cx, cy
            cv2.circle(image, (cx, cy), 10, (0,0,255), cv2.FILLED)
        dt = ((x1-x2)**2 + (y1-y2)**2)**0.5
        if dt < 5:
          print("click")
        elif dt > 80:
          print("clicK")
        cv2.rectangle(image, (x1, y1), (x2, y2), (250, 0, 0), cv2.FILLED)
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()