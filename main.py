import numpy as np
import cv2

#resmi belirtilen konumdan okuduk
img = cv2.imread('sekiller.jpg')
#resim algılama işleminde kolaylık sağlaması için resmi gri yaptık
grayImg= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#threshold eşik ayarlama maskesi için alt eşik ve üst eşiği belirledik
lower = np.array([110, 110, 110])
upper = np.array([255, 255, 255])

#belirlenen degerlerle orjinal görsele threshold uygulandı
threshed = cv2.inRange(img, lower, upper)


cv2.imshow('Thresholded Image', threshed)

#kenarları daha iyi algılamak için  threshold uygulanan görsele canny filtresi uygulandı
canny=cv2.Canny(threshed,100,200)
cv2.imshow('canny Image', canny)

#canny filtresi uygulanmış görseldeki contour değerleri belirlendi
contours , hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# bulunan contour kısımları orjinal resimde çizildi
cv2.drawContours(img, contours, -1, (0, 0, 100), 3)

for c in contours:
    #sınırlayıcı dörtgenin sol üst  x,y koordinatları ,genişlik ve yüksekliğine değişken atanır
    x, y , w, h = cv2.boundingRect(c)
    #bulunan konturleri kapsayan dörtgenler  gri görselde çizilir
    grayImg = cv2.rectangle(grayImg,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Detected Shapes", grayImg)
    aspectRatio = float(w)/h
    area = cv2.contourArea(c)
    extent = area / float(w*h)
    #perimeter = cv2.arcLength(c, True)    
    print(x)
    print(y)
    print(w)
    print(h)
    print(area)
    #print(perimeter)
    if (abs((w*h) - area) < 1500):
       cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
       print("Rectangle")
       print("-------------")

    elif (abs(((w*h) / 2) - area) < 200):
       cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
       print("Triangle")
       print("-------------")
    
    elif (abs(((w*h) * 0.785) - area) < 500):
       cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
       print("Circle")
       print("-------------")

    elif (abs(((w*h) * 0.738) - area) < 1000):
       cv2.putText(img, "Hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
       print("Hexagon")
       print("-------------")
    elif (abs(((w*h)*0.692))- area < 1000):
       cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
       print("Pentagon")
       print("-------------")

cv2.imshow('Shapes', img)
cv2.waitKey(0)

cv2.destroyAllWindows()