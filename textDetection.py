# Video
from pytesseract import pytesseract
import os
import cv2

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# name path to image files
image_frames = 'image_frames'

def getScreenShots(video_source):
    try:
        os.remove(image_frames)
    except OSError:
        pass
    if not os.path.exists(image_frames):
        os.makedirs(image_frames)
    
    cap = cv2.VideoCapture(video_source)

    idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # name each frame and save as png
        name = './image_frames/frame' + str(idx) + '.png'
        print('Extracting frames...' + name)
        cv2.imwrite(name, frame)
        idx = idx + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# do image to text on each png

def get_text():
    for i in os.listdir(image_frames):
        print(str(i))
        img =  cv2.imread(image_frames + "/" + i)
        text = pytesseract.image_to_string(img, lang='eng')
        print(text)


# main driver
if __name__ == '__main__':
    video_source = 'a.mp4'
    getScreenShots(video_source)
    get_text()



# Image
# import cv2
# from pytesseract import pytesseract

# pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# img = cv2.imread("sample.png")

# words_in_image = pytesseract.image_to_string(img)

# print(words_in_image)
