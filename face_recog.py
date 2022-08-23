import face_recognition
import cv2
from PIL import Image, ImageDraw, ImageFont
import sys
import pandas as pd
import datetime
import os


# Reference Data

emp_data = pd.read_csv('/Users/vardaan/Downloads/Employeelist.csv')
#print(emp_data)
empno = emp_data["Employee No"].tolist()
firstname = emp_data["FirstName"].tolist()
lastname = emp_data["LastName"].tolist()
photolocation = emp_data["Photo Location"].tolist()
n = len(empno)
emp = []
emp_encod = []

for i in range(n):
    emp.append(face_recognition.load_image_file(photolocation[i]))
    emp_encod.append(face_recognition.face_encodings(emp[i])[0])



# Face Image Capture

camera = cv2.VideoCapture(0)
path='/Users/vardaan/Downloads/face recognition udemy/Images'
for i in range(10):
    return_value, image = camera.read()
    cv2.imwrite(os.path.join(path,'Employee'+str(i)+'.png'), image)
del(camera)
uk =face_recognition.load_image_file('/Users/vardaan/Downloads/face recognition udemy/Images/Employee5.png')

# Face Recognition Block

def identify_person(photo):
    try:
        uk_encode = face_recognition.face_encodings(photo)[0]
    except IndexError as e:
        print(e)
        sys.exit(1)
    found = face_recognition.compare_faces(
                emp_encod, uk_encode, tolerance = 0.5)    
    print(found)
    
    index = -1
    for i in range(n):
        if found[i]:
            index = i
    return(index)


emp_index = identify_person(uk)    
print(emp_index)   

# Recording attandance to a file

if (emp_index != -1):
    x = str(datetime.datetime.now())
    eno = str(empno[emp_index])
    f = firstname[emp_index]
    l = lastname[emp_index]
    ar = "\n"+eno+" "+f+" "+ l+ "  "+x
    f = open("/Users/vardaan/Downloads/Attendance.txt", "a")
    f.write(ar)
    f.close()  
    print(ar)
    
# Display Attendance

img_dis = Image.fromarray(uk)
draw = ImageDraw.Draw(img_dis)
fnt = ImageFont.truetype(
    "Pillow/Tests/fonts/Arial", 60)

if emp_index ==-1:
    name ="Face NOT Recognized"
else:
    name = firstname[emp_index]+" "+lastname[emp_index]
x = 100
y = uk.shape[0] - 100
draw.text((x, y), name, font=fnt, fill=(0,0,0))
img_dis.show()


