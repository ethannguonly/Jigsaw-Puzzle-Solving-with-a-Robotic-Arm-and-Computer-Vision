from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt

numpieces = 24
puzzlewidth = 6
puzzleheight = 4

def identify_contour(piece, threshold_low=150, threshold_high=255):
    piece = cv2.cvtColor(piece, cv2.COLOR_BGR2GRAY)  # better in grayscale
    ret, thresh = cv2.threshold(piece, threshold_low, threshold_high, 0)
    image, contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_sorted = np.argsort(map(cv2.contourArea, contours))
    return contours, contour_sorted[-2]

def get_bounding_rect(contour):
    x, y, w, h = cv2.boundingRect(contour)
    return x, y, w, h

if __name__=="__main__":
    img = cv2.imread("frozenblack.jpg")
    height, width, channels = img.shape
    scaleheight = int(height / puzzleheight)
    scalewidth = int(width / puzzlewidth)
    for x in range(0, numpieces):
        y1 = x%puzzleheight*scaleheight
        y2 = (x%puzzleheight+1)*scaleheight
        x1 = x%puzzlewidth*scalewidth
        x2 = (x%puzzlewidth+1)*scalewidth
        crop_img = img[y1:y2, x1:x2]
        cv2.imwrite("piece"+str(x+1)+".png", crop_img)

        im = Image.open("piece"+str(x+1)+".png")
        im = im.convert("RGBA")
        datas = im.getdata()

        newData = []
        for item in datas:
            if item[0] < 132 and item[1] < 132 and item[2] < 132:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        im.putdata(newData)
        im.save("piece"+str(x+1)+".png", "PNG")

    canvas = cv2.imread('Frozenref.jpg')
    piece = cv2.imread('piece1.png')

    contours, contour_index = identify_contour(piece.copy())

    x, y, w, h = get_bounding_rect(contours[contour_index])
    cropped_piece = piece.copy()[y:y + h, x:x + w]

    sift = cv2.xfeatures2d.SIFT_create()

    img1 = piece.copy()
    img2 = canvas.copy()

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1, des2, k=2)

    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    MIN_MATCH_COUNT = 1

    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()

        d, h, w = img1.shape[::-1]
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, M)

        img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
        print(np.int32(dst))
    else:
        print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
        matchesMask = None

    draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                       singlePointColor=None,
                       matchesMask=matchesMask,  # draw only inliers
                       flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)

    plt.imshow(img3), plt.show()