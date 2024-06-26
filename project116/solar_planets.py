import cv2
img = cv2.imread("solar-system.jpg")

txt = "Sun"
cv2.putText(img, txt, (20, 250), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0,255,0) )

txt1 = "Mercury"
cv2.putText(img, txt1, (100, 260), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.655, color=(0,255,0) )

txt2 = "Venus"
cv2.putText(img, txt2, (195, 265), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.7, color=(0,255,0) )

txt3 = "Earth"
cv2.putText(img, txt3, (285, 265), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.7, color=(0,255,0) )

txt4 = "Mars"
cv2.putText(img, txt4, (370, 260), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.7, color=(0,255,0) )

txt5 = "Jupiter"
cv2.putText(img, txt5, (485, 280), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0,255,0) )

txt6 = "Saturn"
cv2.putText(img, txt6, (740, 292), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0,255,0) )

txt7 = "Uranus"
cv2.putText(img, txt7, (945, 284), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.8, color=(0,255,0) )

txt8 = "Neptune"
cv2.putText(img, txt8, (1085, 284), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.8, color=(0,255,0) )

cv2.imshow("solar-system",img)
cv2.waitKey(0)
