# Object Detection for Blind with Voice Output

An assistive technology project that uses **OpenCV** and **Python** to detect objects in real-time through a camera and provide **voice feedback** to visually impaired users.

## Features
- Real-time object detection using pre-trained MobileNet SSD model.
- Audio output of detected objects using `pyttsx3`.
- Adjustable voice speed for clear pronunciation.
- Easy to run on any webcam-enabled system.

## Technologies Used
- Python 3.x
- OpenCV
- pyttsx3
- Pre-trained MobileNet SSD Model

## Installation
1. Clone this repository:
   git clone https://github.com/diptibangde10/ObjectDetectionForBlind.git
   cd ObjectDetectionForBlind
2. Install dependencies: pip install opencv-python pyttsx3
3. Download and place the model files (frozen_inference_graph.pb, ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt, coco.names) in the project folder.

## Usage
Run the main script: python code-o-fiesta.py

## For testing with an image:
python myproject.py

## How It Works
1. The webcam captures the live feed.
2. The MobileNet SSD model detects objects from the COCO dataset.
3. The name of each detected object is spoken aloud using text-to-speech.

## Output Example
When the camera sees a "chair":

Detected: CHAIR
Voice Output: "chair"

## Author
Dipti Bangde

## License
This project is open-source under the MIT License.