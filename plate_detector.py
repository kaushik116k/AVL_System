import cv2
import easyocr
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="J72e#05t",
    database = "vehicles"
)
mycursor = mydb.cursor()
frameWidth = 640
franeHeight = 480

plateCascade = cv2.CascadeClassifier("D://haarcascade_russian_plate_number.xml")
minArea = 500

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, franeHeight)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade .detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("D://number_plates//number_plates"+str(count)+".jpg", imgRoi)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        plate = "D://number_plates//number_plates"+str(count)+".jpg"
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)

        img = cv2.imread(plate)
        reader = easyocr.Reader(['en'])
        result = reader.readtext(img)
        print(result)
        text = result[0][-2]

        status_check = "select * from final where license_plate = '%s' AND status = 'in' " % text
        mycursor.execute(status_check)
        row_count = mycursor.fetchone()
        print(row_count)

        if row_count != None:
            print("if entered")
            update = "update final set exit_time = %s, status = 'out' where license_plate = %s"
            input_data = (dt_string, text)
            mycursor.execute(update, input_data)
            mydb.commit()
        else:
            print("entered")
            sql = "INSERT INTO final (license_plate, entry_time, status, exit_time) VALUES (%s, %s, %s, %s)"
            val = (text, dt_string, "in", "-----");
            mycursor.execute(sql, val)
            mydb.commit()

        mycursor.execute("SELECT * FROM final")
        result = mycursor.fetchall()
        for row in result:
            print(row)
            print("\n")
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1