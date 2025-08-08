# BlindAssist-ObjectDetection

**BlindAssist-ObjectDetection** is an AI-powered assistive vision tool that uses **OpenCV** and a pre-trained object detection model to identify objects in real time and provide voice feedback.  
It is designed to help visually impaired individuals navigate their surroundings more safely and independently.

---

## 🚀 Features
- 🎯 Real-time object detection using the **MobileNet SSD** pre-trained model.
- 🔊 Voice feedback for each detected object using `pyttsx3`.
- ⚙️ Adjustable voice speed for clear pronunciation.
- 💻 Works on any standard webcam-enabled system.

---

## 🛠 Technologies Used
- Python **3.8 or greater**
- OpenCV
- pyttsx3
- Pre-trained MobileNet SSD Model (TensorFlow)

---

## 📥 Installation
1. **Check Python version** (must be 3.8 or greater):
   ```bash
   python --version
   
2. **Clone this repository:**
```bash
git clone https://github.com/diptibangde10/BlindAssist-ObjectDetection.git
cd BlindAssist-ObjectDetection
```

3. **Install dependencies:**
```bash
pip install opencv-python pyttsx3
```

4. **Download and place the following model files in the project folder:**
```bash
-frozen_inference_graph.pb
-ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt
-coco.names
```
## 📌 Important Note on Missing Files
This repository does not include two essential model files required to run the project:  
- `frozen_inference_graph.pb` (MobileNet SSD model file)  
- `yolov3.weights` (YOLOv3 model file — larger than GitHub's 25 MB file size limit)
  
Without these files, the project will not run fully.  
If you wish to use the complete project, please email me at **diptibangde100@gmail.com** to obtaining the missing files.

## ▶️ Usage
- Live Webcam Detection:
```bash
python code-o-fiesta.py
```
- Static Image Detection:
```bash
python myproject.py
```
## ⚙️ How It Works
1. The webcam captures the live feed.
2. The MobileNet SSD model detects objects from the COCO dataset.
3. Detected object names are displayed on the screen and spoken aloud using text-to-speech.

## 📌 Example Output
When the camera detects a chair:<img width="330" height="371" alt="chair" src="https://github.com/user-attachments/assets/068740c6-89db-4734-9ad3-d54e3167f042" />
```bash

Detected: CHAIR
Voice Output: "chair"
```
## 👩‍💻 Author
- Dipti Bangde
- GitHub: @diptibangde10

## 📜 License
This project is open source under the MIT License.

## 🔖 Tags
`blindassist` `object-detection` `opencv` `python` `ai` `computer-vision` `assistive-technology` `accessibility` `voice-output` `blind-assistance`
