# OpticalFlow 
Creates an optical flow from a video in a 3D view with time as depth using VTK Visualization Toolkit and Marching Cubes Algorithm.
Use first backgound_suppression_mask_save_to_video.py derived from OpenCV background suppression example to create the video from the background suppression mask.
The run the notebook to create the optical flow from that mask.
Notebook renders to HTML using Plotly. I did not add the HTML to github as it is big (119 MB with the provided mp4).
Because of the size of the HTML it takes around 10 seconds to display on my laptop.
Source video used in the example is here https://github.com/opencv/opencv/blob/master/samples/data/vtest.avi
![Optical flow to 3D rendering with Plotly](./opticalflow.png?raw=true "Plotly rendering of Optical flow")
Python file uses VTK default rendering window 

Also added a lissajous example, just change the source video in OpticalFlowFromBackground.ipynb to lissajous.mp4 
![Lissajous video flow to 3D rendering with Plotly](./lissajous2plotly.png?raw=true "Plotly rendering of Lissajous flow")
Here is the link to the resulting page with plotly (94MB) expect a few seconds to load
[Plotly 3D rendering of lissajous](http://marc.fiammante.free.fr/lissajous_plotly_output.html)
