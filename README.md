# Vehicle-Front-Rear-Detection-for-License-Plate-Detection-Enhancement
## How to run
1. Clone the Repo in home.
```
git clone https://github.com/nicky7767/Vehicle-Front-Rear-Detection-for-License-Plate-Detection-Enhancement.git
```
2. Download the weights from [link](https://drive.google.com/file/d/1gD0NjgptC_ZxOoYY56cnN7I88UL2ei4G/view?usp=sharing). Place this file inside data/FRD.
3. cd into darknet and run 
```
$ make
```
4. cd into the main folder and run the Front_Rear_Detect.py file.
5. The output will be stored in output folder.
6. To give your own image, place the image in samples/test_samples and change name of the image in line 53 of Front_Rear_Detect.py.

#### Note : The code is tested on Ubuntu system, it won't work in windows based system.
