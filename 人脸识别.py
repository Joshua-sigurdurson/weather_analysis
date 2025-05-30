import os
import base64
from aip import AipFace
import face_recognition as fr
import cv2

import cv2
img = cv2.imread("unknown.jpg")
top,right,bottom,left=(121, 162, 196, 88)
cv2.rectangle(img,(left, top),(right, bottom),color = (50,255,50),thickness = 3)
def baidu_face(filename,aipFace):
    options = {}
    #读取图片
    with open(filename, "rb") as fp:
        base64_data = base64.b64encode(fp.read())
    image = str(base64_data, 'utf-8')
    imageType = "BASE64"
    # 调用人脸属性检测接口
    options["face_field"] = "age,expression,beauty"
    result = aipFace.detect(image, imageType, options)

    return result


APP_ID = '27092881'
API_KEY = 'uNP0pjOOkiOc36skNtlpgBWD '
SECRET_KEY = 'jq3C3pvcRYTfkZTfLXprfqomQYLT3VOn'
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

result=baidu_face("unknown.jpg",aipFace)
firstman=result['result']['face_list'][0]
img = cv2.imread("unknown.jpg")
cv2.putText(img, str(firstman['age']), (100,100), cv2.FONT_HERSHEY_SIMPLEX , 1.2, (255, 255, 255), 2)
cv2.imshow("age",img)
cv2.imwrite("testout.jpg",img)

print('你今年应该',firstman['age'],'岁了吧')
cv2.waitKey(0)
from aip import AipFace


result=baidu_face("unknown.jpg",aipFace)
print("百度AI平台识别返回结果：")
print(str(result).replace(',','\n'))
firstman=result['result']['face_list'][0]     
print('预计年龄:',firstman['age'])
