#FFMPEG PyAV ... + opencv
#13.1.2021
#https://pyav.org/docs/develop/#cookbook + ...

import av
import cv2
import numpy as np

dir = "z:\\"
file = "ooo.mp4"
path_to_video = dir + file
container = av.open(path_to_video)

def ExtractFrames(path, outdir):
  container = av.open(path)
  for frame in container.decode(video=0):
    frame.to_image().save(outdir+"\\"+ '%04d.jpg' % frame.index)
  container.close()
  
def Play():
    for frame in container.decode(video=0):
        #frame.to_image().save('frame-%04d.jpg' % frame.index)    
        #img = frame.to_image()
        #arr = frame.to_ndarray(format='rgb24')
        arr = frame.to_ndarray(format='bgr24')
        cv2.imshow("SHOW", arr)
        cv2.waitKey(1)
        
    container.close()

def Create():
    duration = 4
    fps = 25
    total_frames = duration * fps
    w = 640
    h = 480

    container = av.open('test.mp4', mode='w')
    #stream = container.add_stream('mpeg4', rate=fps)
    type = 'xvid'
    type = 'libx264'
    stream = container.add_stream(type, rate=fps)
    stream.width = w
    stream.height = h
    stream.pix_fmt = 'yuv420p'
    
    i=0
    for frame_i in range(total_frames):
        img = np.empty((w, h, 3))
        img[:, :, 0] = 0.5 + 0.5 * np.sin(2 * np.pi * (0 / 3 + frame_i / total_frames))
        img[:, :, 1] = 0.5 + 0.5 * np.sin(2 * np.pi * (1 / 3 + frame_i / total_frames))
        img[:, :, 2] = 0.5 + 0.5 * np.sin(2 * np.pi * (2 / 3 + frame_i / total_frames))

        img = np.round(255 * img).astype(np.uint8)
        img = np.clip(img, 0, 255)
        i+=1
        cv2.line(img, (0,0), (i*3, i*3), (100, 80+i%20, 140-i%20), 3)

        frame = av.VideoFrame.from_ndarray(img, format='rgb24')
        for packet in stream.encode(frame):
            container.mux(packet)
    # Flush stream
    
    for packet in stream.encode():
        container.mux(packet)

    # Close the file
    container.close()
    
Create()
