# # Importing all necessary libraries
# import cv2
# import os

# # Read the video from specified path
# cam = cv2.VideoCapture("gauravphn.mp4")

# try:

#     # creating a folder named data
#     if not os.path.exists('data'):
#         os.makedirs('data')

# # if not created then raise error
# except OSError:
#     print('Error: Creating directory of data')

# # frame
# currentframe = 661

# while (True):

#     # reading from frame
#     ret, frame = cam.read()

#     if ret:
#         # if video is still left continue creating images
#         name = './dataset/frame' + str(currentframe) + '.jpg'
#         print('Creating...' + name)

#         # writing the extracted images
#         cv2.imwrite(name, frame)

#         # increasing counter so that it will
#         # show how many frames are created
#         currentframe += 1
#     else:
#         break

# # Release all space and windows once done
# cam.release()
# cv2.destroyAllWindows()


import cv2
vidcap = cv2.VideoCapture('.mp4')


def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        # save frame as JPG file
        name = './dataset/new/img' + str(count) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, image)
    return hasFrames


sec = 0
frameRate = 1  # //it will capture image in each 0.25 second
count = 1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
