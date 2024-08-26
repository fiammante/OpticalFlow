# OpticalFlow 
Creates an optical flow from a video in a 3D view with time as depth using VTK Visualization Toolkit and Marching Cubes Algorithm.
Use first backgound_suppression_mask_save_to_video.py derived from OpenCV background suppression example to create the video from the background suppression mask.
The run the notebook to create the optical flow from that mask.
Notebook renders to HTML using Plotly. I did not add the HTML to github as it is big (119 MB with the provided mp4).
Because of the size of the HTML it takes around 10 seconds to display on my laptop.
Source video used in the example is here https://github.com/opencv/opencv/blob/master/samples/data/vtest.avi
![Optical flow to 3D rendering with Plotly](./opticalflow.png?raw=true "Plotly rendering of Optical flow")
Python file uses VTK default rendering window 
