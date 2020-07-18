from skimage.measure import compare_ssim
import argparse
import imutils
import cv2 as cv2

class ImageComparison(object):

    def __init__(self):
        pass

    def compare_images(self, imageA, imageB, DifferenceImage):

        # load the two input images using openCV
        imageA = cv2.imread(imageA)
        imageB = cv2.imread(imageB)

        # convert the images to grayscale
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        # print("SSIM: {}".format(score))

        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # loop over the contours
        for c in cnts:
            # compute the bounding box of the contour and then draw the
            # bounding box on both input images to represent where the two
            # images differ
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # save the differance highlighted image `DifferenceImage`
        # cv2.imwrite(DifferenceImage, imageB)
        # show the output images
        cv2.imshow("Original", imageA)
        cv2.imshow("Modified", imageB)
        # cv2.imshow("Diff", diff)
        # cv2.imshow("Thresh", thresh)
        cv2.waitKey(0)

        
# # Test the compare_images()
image = ImageComparison()
image.compare_images("D:\\Automation\\python\\pythonframework_v2\\project\\TestScreenshots\\LoginTestScenario\\loginWithProblemUser\\LoginPage\\navigateLoginPage.png",
"D:\\Automation\\python\\pythonframework_v2\\project\\TestScreenshots\\LoginTestScenario\\loginWithProblemUser\\WelcomePage\\baseline_navigateWelcomePage.png",
"D:\\Automation\\python\\pythonframework_v2\\project\\TestScreenshots\\differenceLogin.png")