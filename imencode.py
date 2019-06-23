import cv2
import io
import base64

path = input("path: ")
with io.open(path, 'rb') as image_file:
    content = image_file.read()

    cv2_image = cv2.imread(path)
    res, cv2_encoded = cv2.imencode(".jpg", cv2_image)
    cv2_bytes = cv2_encoded.tobytes()
    print(content[:100])
    print(cv2_encoded[:100])
    print(cv2_bytes[:100])

    # print("raw_content = ", content[:400])
    # decoded = cv2.imread(path)
    # print("decoded = ", decoded[:400])
    # jpg = cv2.imencode(".jpg", decoded)
    # print("jpg = ", jpg[:400])
    # imgstr = jpg[1]
    # print("imgstr = ", imgstr)
    # newstr = imgstr.tostring()
    # print("newstr = ", newstr[:400])
    # str64 = base64.b64encode(bytes(imgstr))
    # print("str64 = ", str64[:400])

    # zz = cv2.imencode('.jpg', decoded)[1].tostring()
    # print("zz=", zz[:400])

    # yy = cv2.imdecode(zz, cv2.IMREAD_UNCHANGED)
    # print("yy=", yy[:400])

    
    # cv2.imshow("decoded", decoded)
    # cv2.waitKey(5000)
    
    # cv2.imshow("yy", yy)
    # cv2.waitKey(5000)
    
    # cv2.imshow("zz", zz)
    # cv2.waitKey(5000)
    
    
    