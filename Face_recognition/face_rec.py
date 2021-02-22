import face_recognition
import cv2
import numpy as np
import os
import time

video_capture = cv2.VideoCapture(0)
known_person=[] #Name of person string
known_image=[] #Image object
known_face_encodings=[] #Encoding object

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

#Loop to add images in family folder
for file in os.listdir("profiles"):
    try:
        print(file," is being encoded")
        known_person.append(file.replace(".jpg", ""))#Extracting person name
        file=os.path.join("profiles/", file)
        known_image = face_recognition.load_image_file(file)
        known_face_encodings.append(face_recognition.face_encodings(known_image)[0])

    except Exception as e:
        pass
    
#print(len(known_face_encodings))
#print(known_person)

capture_duration = 10
start_time = time.time()
while( int(time.time() - start_time) < capture_duration ):

    ret, frame = video_capture.read()
    frame = cv2.flip(frame, -1)


    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    
    if process_this_frame:
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        
        global name_gui;
        for face_encoding in face_encodings:
            
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_person[best_match_index]
            print(name)
            face_names.append(name)
    
            name_gui = name
    

    process_this_frame = not process_this_frame
    
    # Hit 'q' or Esc on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(face_names)
    

from picamera import PiCamera
from time import sleep

def take_photo():
    camera = PiCamera()
    camera.resolution = (640,480)
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Documents/face_pi/profiles/add_user_name.jpg')
    camera.stop_preview()




