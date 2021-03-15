import cv2
import os
import time
from random import randrange

def cls():
    os.system("cls")


def images():
    print("(1) Detect faces")
    print("(2) Detect cars")
    menu_choice = input("Please enter an option (by number): ")
    if menu_choice == "1":
        path_to_image = input("Please enter the path to the image you'd like to use: ")
        if os.path.exists(path_to_image):
            trained_face_data = cv2.CascadeClassifier('haarcascade_frontface.xml')
            img = cv2.imread(path_to_image)
            grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_coords = trained_face_data.detectMultiScale(grayscaled)
            for (x, y, w, h) in face_coords:
                cv2.rectangle(img, (x, y), (x+h, y+h), (randrange(256), randrange(256), randrange(256)), 2)
            print(face_coords)
            cv2.imshow("Face Detection", img)
            cv2.imwrite("DetectedFace.jpg", img)
            cv2.waitKey()
            main()
        else:
            print("Unable to locate file")
            time.sleep(2)
            cls()
            images()
    elif menu_choice == "2":
        path_to_image = input("Please enter the path to the image you'd like to use: ")
        if os.path.exists(path_to_image):
            trained_car_data = cv2.CascadeClassifier('cars.xml')
            img = cv2.imread(path_to_image)
            grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            car_coords = trained_car_data.detectMultiScale(grayscaled)
            for (x, y, w, h) in car_coords:
                cv2.rectangle(img, (x, y), (x+h, y+h), (randrange(256), randrange(256), randrange(256)), 2)
            print(face_coords)
            cv2.imshow("Car Detection", img)
            cv2.imwrite("DetectedCar.jpg", img)
            cv2.waitKey()
            images()
        else:
            print("Unable to locate file")
            time.sleep(2)
            cls()
            images()

def web_cam():
        trained_face_data = cv2.CascadeClassifier('haarcascade_pedestrian.xml')
        webcam = cv2.VideoCapture(0)
        print(webcam)
        while True:
            sucessful_frame_read, frame = webcam.read()
            grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_coords = trained_face_data.detectMultiScale(grayscaled)
            for (x, y, w, h) in face_coords:
                cv2.rectangle(frame, (x, y), (x+h, y+h), (randrange(256), randrange(256), randrange(256)), 2)
            cv2.imshow("Face Detection", frame)
            key = cv2.waitKey(1)
            if key == 81 or key == 113:
                break
        webcam.release()

def videos():
    print("(1) Detect faces")
    print("(2) Detect cars")
    menu_choice = input("Please enter an option (by number): ")
    if menu_choice == "1":
        video = input("Please enter a video to detect faces in: ")
        if os.path.exists(video):
            trained_face_data = cv2.CascadeClassifier('haarcascade_frontface.xml')
            video = cv2.VideoCapture(video)
            while True:
                sucessful_frame_read, frame = video.read()
                grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face_coords = trained_face_data.detectMultiScale(grayscaled)
                for (x, y, w, h) in face_coords:
                    cv2.rectangle(frame, (x, y), (x+h, y+h), (randrange(256), randrange(256), randrange(256)), 2)
                cv2.imshow("Face Detection", frame)
                key = cv2.waitKey(1)
                if key == 81 or key == 113:
                    break
            video.release()
        else:
            print("Unable to find video!")
            time.sleep(2)
            cls()
            main()
    elif menu_choice == "2":
        video = input("Please enter a video to detect cars in: ")
        if os.path.exists(video):
            trained_car_data = cv2.CascadeClassifier('cars.xml')
            video = cv2.VideoCapture(video)
            while True:
                sucessful_frame_read, frame = video.read()
                grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                car_coords = trained_car_data.detectMultiScale(grayscaled)
                for (x, y, w, h) in car_coords:
                    cv2.rectangle(frame, (x, y), (x+h, y+h), (randrange(256), randrange(256), randrange(256)), 2)
                cv2.imshow("Car Detection", frame)
                key = cv2.waitKey(1)
                if key == 81 or key == 113:
                    break
            video.release()
        else:
            print("Unable to find video!")
            time.sleep(2)
            cls()
            videos()
def main():
    print("(1) Photo")
    print("(2) Web cam")
    print("(3) Video")
    menu_choice = input("Please pick a detector (by number): ")
    if menu_choice == "1":
        images()
    elif menu_choice == "2":
        web_cam()
    elif menu_choice == "3":
        videos()



if __name__ == "__main__":
    cls()
    main()
