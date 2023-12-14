import time

import cv2


if __name__ == '__main__':
    video = cv2.VideoCapture(0)
    time.sleep(1)
    while True:

        check, frame = video.read()
        cv2.imshow("Video", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    video.release()
