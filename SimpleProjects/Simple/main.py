import cv2
import streamlit as st
import datetime as dt

if __name__ == '__main__':
    st.title("Game Camera")
    start = st.button("Place Camera")

    if start:
        streamlit_image = st.image([])
        camera = cv2.VideoCapture(0)
        date_time = dt.datetime.now()
        day = date_time.strftime("%A")
        time = date_time.strftime("%H:%M:%S")

        while True:
            check, frame = camera.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            cv2.putText(img=frame, text=day, org=(20, 30),
                        fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20, 100, 200),
                        thickness=2, lineType=cv2.LINE_AA)
            cv2.putText(img=frame, text=time, org=(20, 60),
                        fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 0, 0),
                        thickness=2, lineType=cv2.LINE_AA)
            streamlit_image.image(frame)
