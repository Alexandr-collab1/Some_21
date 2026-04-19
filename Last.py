import cv2

def apply_mask(original_img_path, mask_img_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


    img = cv2.imread(original_img_path)
    mask = cv2.imread(mask_img_path)
    
    if img is None or mask is None:
        print("Помилка: Не вдалося завантажити зображення.")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    print(f"Знайдено патернів: {len(faces)}")

    for (x, y, w, h) in faces:
        resized_mask = cv2.resize(mask, (w, h))

        img[y:y+h, x:x+w] = resized_mask

    cv2.imwrite('result.jpg', img)
    print("Обробка завершена. Файл збережено як result.jpg")

