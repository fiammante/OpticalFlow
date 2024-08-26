# adapted from OpenCV background suppression example to save the mask in a separate video named fgMask.mp4


from __future__ import print_function
import cv2 as cv
import argparse

parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
args = parser.parse_args()

## [create]
#create Background Subtractor objects
if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
else:
    backSub = cv.createBackgroundSubtractorKNN()
## [create]

## [capture]
capture = cv.VideoCapture(cv.samples.findFileOrKeep(args.input))
if not capture.isOpened():
    print('Unable to open: ' + args.input)
    exit(0)
    
fps = capture.get(cv.CAP_PROP_FPS)
## [capture]
fourcc = cv.VideoWriter_fourcc(*'mp4v')

first=True
while True:
    ret, frame = capture.read()
    if frame is None:
        break
    if first:
        h,w=frame.shape[:2]
        out = cv.VideoWriter(".\\fgMask.mp4", fourcc, fps, (w,h))
        first=False
    ## [apply]
    #update the background model
    fgMask = backSub.apply(frame)
    ## [apply]
    fgMaskcolor = cv.cvtColor(fgMask, cv.COLOR_GRAY2BGR) 
    out.write(fgMaskcolor)
    ## [display_frame_number]
    #get the frame number and write it on the current frame
    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    ## [display_frame_number]

    ## [show]
    #show the current frame and the fg masks
    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)
    ## [show]

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
print(frame.shape)
out.release()    