import cv2
import numpy as np


def selectElements(img):
    # Kmeans segmentation
    image_copy = img.copy()
    pixel_values = image_copy.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)
    stop_criteria = (cv2.TERM_CRITERIA_EPS +
                     cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    centroid_initialization_strategy = cv2.KMEANS_RANDOM_CENTERS
    print("getting kmeans information")
    _, labels, centers = cv2.kmeans(pixel_values,
                                    5,
                                    None,
                                    stop_criteria,
                                    1,
                                    centroid_initialization_strategy)
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]
    segmented_image = segmented_data.reshape(image_copy.shape)

    # Identify objects
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 80, 200)
    edges_final = edges.copy()

    kernel = np.ones((3, 3), np.uint8)
    kernel_closi = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE,
                               kernel_closi, iterations=4)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN,
                               kernel_closi, iterations=3)

    img_copy = img.copy()
    final_mask_c = img.copy()
    final_mask_c[:, :, :] = 0
    final_mask_cH = final_mask_c.copy()
    final_mask_centers = final_mask_c.copy()

    contours, hierarchy = cv2.findContours(
        opening, 1, cv2.CHAIN_APPROX_NONE)

    areas = []
    hull = []
    font = cv2.FONT_HERSHEY_SIMPLEX
    print("creating contours, convex hull")
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        areas.append(area)
        convex = cv2.convexHull(contours[i], False)
        hull.append(convex)

    max_val = np.argmax(areas)
    areas[max_val] = 0

    print("Drawing contours, convex hull")
    contours_lengh = len(contours)
    for i in range(contours_lengh):
        cv2.drawContours(final_mask_c, contours, i,
                         (10, 108, 28), 2, cv2.LINE_8, hierarchy, 100)
        cv2.drawContours(final_mask_cH, hull, i, (255, 1, 1), 3, 8)

        M = cv2.moments(contours[i])
        m00 = M['m00'] if M['m00'] else 1
        cx = int(M['m10']/m00)
        cy = int(M['m01']/m00)
        final_mask_centers=cv2.circle(final_mask_centers, (cx, cy), 10,(255, 254, 0), -1)

    cv2.putText(final_mask_centers, f"Objects: {len(contours)}", (150, 250), font, 5,(0,255,0), 4)

    arr1 = np.array(final_mask_c)
    arr2 = np.array(final_mask_cH)
    arr3 = np.array(final_mask_centers)
    final_mask_c = cv2.cvtColor(final_mask_c, cv2.COLOR_BGR2RGBA)
    final_mask_cH = cv2.cvtColor(final_mask_cH, cv2.COLOR_BGR2RGBA)
    final_mask_centers = cv2.cvtColor(
        final_mask_centers, cv2.COLOR_BGR2RGBA)
    segmented_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGBA)

    final_mask_c[:, :, 3] = 0
    final_mask_cH[:, :, 3] = 0
    final_mask_centers[:, :, 3] = 0
    result = np.where(arr1 == 10)
    for i in range(len(result[0])-1):
        final_mask_c[result[0][i], result[1][i], 3] = 255
    result = np.where(arr2 == 255)
    for i in range(len(result[0])-1):
        final_mask_cH[result[0][i], result[1][i], 3] = 255
    result = np.where(arr3 == 255)
    for i in range(len(result[0])-1):
        final_mask_centers[result[0][i], result[1][i], 3] = 255
    


    return final_mask_c, final_mask_cH, final_mask_centers, segmented_image, edges_final
