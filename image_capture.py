import cv2
import time
import os


def image_capture():
    camera = cv2.VideoCapture(0)
    if camera.isOpened():
        while True:
            print('The image capture process has started...')

            return_code, image = camera.read()

            if return_code:
                # the file name in the format of the current date and time
                filename = time.strftime("%Y%m%d-%H%M%S") + '.png'
                os.chdir("images")
                cv2.imwrite(filename, image)
                break

        camera.release()
        print(f'The image is saved to a file {filename}')
    else:
        print('Camera error!')


if __name__ == '__main__':
    if not os.path.isdir("images"):
        os.mkdir("images")

    image_capture()


