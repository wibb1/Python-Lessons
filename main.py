import glob
import os
import time
import datetime
import cv2

from emailing import send_email


def empty_images_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)


if __name__ == '__main__':
    first_frame = None

    video = cv2.VideoCapture(0)
    time.sleep(1)

    status_list = []

    while True:
        status = 0
        check, frame = video.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame_gua = cv2.GaussianBlur(gray_frame, (21, 21), 0)

        if first_frame is None:
            first_frame = gray_frame_gua

        delta_frame = cv2.absdiff(first_frame, gray_frame_gua)

        thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
        dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
        cv2.imshow("Video", dil_frame)

        contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) < 5000:
                continue
            # Object detected
            x, y, w, h = cv2.boundingRect(contour)
            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))
            if rectangle.any():
                status = 1
                date_time = datetime.datetime.now()
                format_datetime = date_time.strftime("%Y%m%d%H%M%S.%f")
                print(format_datetime)
                cv2.imwrite(f"images/{format_datetime}.png", frame)
                all_images = glob.glob("images/*.png")
                print(str(len(all_images)))
                index = int(len(all_images) / 2)
                image_with_object = all_images[index]

        status_list.append(status)
        status_list = status_list[-2:]

        if status_list[0] == 1 and status_list[1] == 0:
            send_email(image_with_object)
            empty_images_folder()

        cv2.imshow("Video", frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    video.release()
