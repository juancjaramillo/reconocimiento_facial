import cv2
import face_recognition
import os
import pickle
import numpy as np
import time
from playsound import playsound
from collections import defaultdict  # NUEVO: Para contar detecciones

# Configuración
IMAGES_PER_PERSON = 5  # Número de imágenes a capturar por persona
CAPTURE_DELAY = 1  # Segundos entre capturas
SOUND_NEW_PERSON = 'new_person.mp3'  # Archivo de sonido

# Crear carpetas si no existen
if not os.path.exists('known_faces'):
    os.makedirs('known_faces')

# Cargar base de datos existente
if os.path.exists('encodings.pickle'):
    with open('encodings.pickle', 'rb') as f:
        known_faces = pickle.load(f)
else:
    known_faces = {}

# NUEVO: Crear contador de detecciones
detections_counter = defaultdict(int)

# Función para guardar codificaciones
def save_encodings():
    with open('encodings.pickle', 'wb') as f:
        pickle.dump(known_faces, f)

# Inicializar cámara
camera = cv2.VideoCapture(0)

print("Presiona 's' para capturar una imagen o 'q' para salir.")

while True:
    ret, frame = camera.read()
    if not ret:
        break

    frame_small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small = cv2.cvtColor(frame_small, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb_small)
    encodings = face_recognition.face_encodings(rgb_small, faces)

    for encoding, face_location in zip(encodings, faces):
        found = False
        name_detected = "Unknown"

        for name, known_encoding_list in known_faces.items():
            matches = face_recognition.compare_faces(known_encoding_list, encoding)
            if True in matches:
                name_detected = name
                found = True
                break

        top, right, bottom, left = [v * 4 for v in face_location]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        if found:
            # NUEVO: Incrementar contador
            detections_counter[name_detected] += 1
            # Mostrar nombre + número de detecciones
            label = f"{name_detected} ({detections_counter[name_detected]})"
            print(f"Detectado: {label}")
        else:
            label = name_detected

        cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        if not found:
            print("Nueva persona detectada.")

            if os.path.exists(SOUND_NEW_PERSON):
                playsound(SOUND_NEW_PERSON)

            # Pedir nombre
            person_name = input("Ingrese el nombre de la nueva persona: ")
            known_faces[person_name] = []

            # Capturar varias imágenes
            print(f"Capturando {IMAGES_PER_PERSON} imágenes de {person_name}...")
            count = 0
            while count < IMAGES_PER_PERSON:
                ret, frame = camera.read()
                if not ret:
                    continue

                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                face_locations = face_recognition.face_locations(rgb_frame)
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

                if face_encodings:
                    known_faces[person_name].append(face_encodings[0])

                    if not os.path.exists(f'known_faces/{person_name}'):
                        os.makedirs(f'known_faces/{person_name}')
                    img_path = f'known_faces/{person_name}/{person_name}_{count}.jpg'
                    top, right, bottom, left = face_locations[0]
                    face_image = frame[top:bottom, left:right]
                    cv2.imwrite(img_path, face_image)

                    print(f"Imagen {count + 1}/{IMAGES_PER_PERSON} capturada.")
                    count += 1
                    time.sleep(CAPTURE_DELAY)

            save_encodings()
            print(f"Registro actualizado para {person_name}.")
    cv2.startWindowThread()

    cv2.imshow('Reconocimiento Facial', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        continue

camera.release()
cv2.destroyAllWindows()
save_encodings()
