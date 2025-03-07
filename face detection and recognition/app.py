import face_recognition
import cv2

know_image    = face_recognition.load_image_file('dataset/messi/img2.jpg')
know_encoding = face_recognition.face_encodings(know_image)[0]  

cap = cv2.VideoCapture(0)
while True:
    _ , frame = cap.read()
    
    rgb       = frame[:,:,::-1]

    location  = face_recognition.face_locations(rgb)
    encoding  = face_recognition.face_encodings(rgb, location)
    
    for(top, right, bottom, left),face in zip(location,encoding):
        matches  = face_recognition.compare_faces([know_encoding], face)
        name     = 'Face not recognized'
        
        if True in matches:
            name = 'Face recognized'
            
        cv2.rectangle(frame, (left,top), (right,bottom), (255,255,0),4)
        cv2.putText(frame, name, (left, bottom +20), cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0), 4)
        
    cv2.imshow('FACE DETECTION AND RECOGNITION',frame)
    if cv2.waitKey(3) & 0xff == ord('q'):
        break   