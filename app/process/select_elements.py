import cv2
import numpy as np

def selectElements(img, convex_hull=False, contours=False, show_number=False):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  edges = cv2.Canny(gray,80,200)

  kernel = np.ones((3,3),np.uint8)
  kernel_closi = np.ones((5,5),np.uint8)
  closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel_closi, iterations=4)

  img_copy = img.copy()
  contours,hierarchy = cv2.findContours(closing, 1, cv2.CHAIN_APPROX_NONE)

  areas = []
  hull = []
  font = cv2.FONT_HERSHEY_SIMPLEX
  for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    areas.append(area)
    convex = cv2.convexHull(contours[i], False)
    hull.append(convex)

  max_val = np.argmax(areas)
  areas[max_val] = 0

  for i in range(len(contours)):
    if (contours):
      cv2.drawContours(img_copy, contours, i, (10,108,28), 2,cv2.LINE_8, hierarchy, 100)
    if (convex_hull):
      cv2.drawContours(img_copy, hull, i, (255,0,0), 3, 8)
    if show_number:
        M = cv2.moments(contours[i])
        m00 = M['m00'] if M['m00'] else 1
        cx = int(M['m10']/m00)
        cy = int(M['m01']/m00)

        cv2.putText(img_copy, f"{i+1}", (cx-25, cy-25), font, 0.9,(255,255,0), 4)
  else:
    return img_copy
