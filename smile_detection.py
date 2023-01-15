import cv2

face_front = cv2.CascadeClassifier('frintalface.xml')

smile = cv2.CascadeClassifier('smile.xml')

webcam = cv2.VideoCapture(0)


while True:
    sucess_true_frame, frame = webcam.read()
    
    grey_man = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    train_face = face_front.detectMultiScale(grey_man)
   
    
    for (x, y, w, h) in train_face:
       cv2.rectangle(frame, (x, y), (x+w, y+h), (225, 225,0), 2)
       
       a_face = frame[y:y+h, x:x+h]       
       train_smile = smile.detectMultiScale(a_face, scaleFactor=1.7, minNeighbors=20)
       
    #    for (x_, y_, w_, h_) in train_smile:
           
    #       cv2.rectangle(a_face, (x_, y_), (x_ + w_, y_ + h_), (225, 0, 150), 2)
    
       if len(train_smile) >0:
           cv2.putText(frame, 'Dirty stinky mouth', (x, y+h+40), fontScale=1, fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))
       
    cv2.imshow('i be dead', frame) 
    end = cv2.waitKey(1)
    
    
    if end == 81 or end == 113:
        break

webcam.release()