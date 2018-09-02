import cv2
from enum import Enum
class Channel(Enum):
    NONE = -1
    BLUE = 0
    GREEN = 1
    RED = 2

def manageIndeces(entryString):
    if entryString == "b":
        return Channel.BLUE
    if entryString == "g":
        return Channel.GREEN
    if entryString == "r":
        return Channel.RED
    return Channel.NONE

path = "img/rubick.jpg"
img = cv2.imread(path)
img = cv2.resize(img,(600,800))
entryKey = input("Enter color:").lower()
print(entryKey)
COLOR_INDEX = manageIndeces(entryKey)
print(COLOR_INDEX)
if COLOR_INDEX is not Channel.NONE:
    ret, img= cv2.threshold(img[:,:,COLOR_INDEX.value],145,255,cv2.THRESH_BINARY)
cv2.imshow(entryKey.capitalize() + " Color", img)
cv2.imwrite("img/"+entryKey+".jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


