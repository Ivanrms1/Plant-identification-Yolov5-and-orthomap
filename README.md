# Plant-identification-Yolov5-and-orthomap
In this we register the algorithm that used to get orthomap, and also to perform yolov5 for object plant detection

### Getting video
The vidio must be taken with a drone, usually we manage a 30m from the floor, actually the paths was settle manually and with average speed of 3 m/s.
The agave plots taken, was mainly in Cotija, Michoacán, like Llano largo R&M, Llano largo1, Los reyes, and La antena. The data of videos was in google drive https://drive.google.com/drive/folders/1TghSp3iJyLnSymabcPBP2Kca9RURveg5?usp=drive_link. An example of data and video preparation https://github.com/Ivanrms1/Plant-identification-Yolov5-and-orthomap/blob/main/assets/videosysubtitulos.png

### Making orthomap
This is in order to take a precisa or unique plot, we reconrsuct them using the videos obtained from drone path, and extracted the subtitles for georefereciation of the path recorded.
The code is here in utils as a esub.sh, this extract the .srt files of all videos on one folder, and kept the same name of the video, this is important for generating orthomap.

The orthomap is created using OpenDroneMap https://github.com/OpenDroneMap/ODM.git, a opencode for drone mapping, that uses SIFT algorithm to matching images and used georeferenced data to reconstruct a 2d map, also it provides
a textured map, in .obj that can be rendererd with blender to get a 3D model with elevations.

### Slashing otrhomap in small images
In this part with code in utils, we split the big orthomap images into small ones in order to put into Yolo code, i take 640x640 images, yolov5 needs a square image, also in the splitting images we get some blank images or blacked ones, 
it removed blank images to kept only the ones that haves any one pixel in it, this is needed because the created orthomap has up to 11k x 8k+ dimensions, and the plot map only fills like 60-70% of them.

### Put in pre-trained yolo
Before we trained yolov5 with agave plant images, Yolov5 has a better perform than U-net segmentation model before, detecting with less error were is a plant, also it's added or edited the code to shown in the inference, how many
plants are in an image. We put the splitted orthomap in the folder that have all splited images, then make inference of all them, and preview results.
The code are in folder called yolo, but u can found also in https://github.com/ultralytics/yolov5.
