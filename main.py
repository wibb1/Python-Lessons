import time

import cv2

if __name__ == '__main__':
    first_frame = None

    video = cv2.VideoCapture(0)
    time.sleep(1)

    while True:

        check, frame = video.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame_gua = cv2.GaussianBlur(gray_frame, (21, 21), 0)

        if first_frame is None:
            first_frame = gray_frame_gua

        delta_frame = cv2.absdiff(gray_frame_gua, first_frame)

        thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)
        dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
        cv2.imshow("Video", dil_frame)

        contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) < 5000:
                continue
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))
        cv2.imshow("Video", frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    video.release()
