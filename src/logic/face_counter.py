import cv2

def detect_faces(image_path, output_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    if image is None:
        return 0
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(image_rgb, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(image_rgb, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imwrite(output_path, cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR))
    return len(faces)