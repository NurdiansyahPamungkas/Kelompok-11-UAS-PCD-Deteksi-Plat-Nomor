import glob
import cv2
import easyocr

def readImage():
    folder = glob.glob(r"C:\Selain Sistem\data kuliah\Pengolahan Citra Digital\uas\plat\hasil\*.jpg")
    images = []

    for file in folder:
        images.append(file)

    count = 1

    for image in images:
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 2)

        reader = easyocr.Reader(["en"])
        result = reader.readtext(gray)
        for (bbox, text, prob) in result:
            print(count, "Plat Nomor:", text, "|", "persentase:", prob.encode('utf-8').decode('utf-8', 'ignore'))
            count += 1

        cv2.imshow("Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()