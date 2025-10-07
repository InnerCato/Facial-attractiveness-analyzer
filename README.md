# Facial Attractiveness Calculator

This project estimates facial attractiveness scores based on facial ratios and symmetry.  
It can analyze either **images of faces** or **manual measurements**.

---

## ✨ Features

- Detects faces using **dlib** and **OpenCV**
- Calculates key facial ratios, including:
  - **Eye spacing**
  - **Mouth-to-nose ratio**
  - **Face width-to-height**
  - **Chin-to-mouth-to-nose**
  - **Eye width relative to face**
  - **Facial symmetry**
- Produces a **normalized attractiveness score** (0–100)
- Supports **manual input** for ruler-based analysis
- Uses a **weighted scoring system** to balance feature importance

---

## 🧠 How It Works

1. The program detects facial landmarks using `dlib`’s pre-trained 68-point predictor.
2. It measures distances between specific landmark points.
3. Ratios are computed (e.g., eye spacing vs. face width).
4. Each ratio is compared to an “ideal” ratio using an exponential scoring function.
5. The results are averaged into a final attractiveness score.

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/InnerCato/Face-Mathematical-Attractiveness.git
   cd Face-Mathematical-Attractiveness

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt


"shape_predictor_68_face_landmarks.dat" is already included in the project directory.


## 🚀 Usage

*Analyze An Image*  

python face_checker.py  
Add a face in the Images folder and name it "face[number]", replace [number] with a number.  
Supports ".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"  
Then enter the image number (e.g., 1 for Images/face1.jpg).  


*Analyze Manual Measurements*  

python face_measurements.py  
You’ll be prompted to enter real-world measurements (in millimeters).  

🧩 Requirements
    ```bash
    numpy  
    opencv-python  
    dlib
    ```

📊 Example Output  
    ```bash
    --- Facial Attractiveness Analysis ---  
    Eye Spacing: 90.77/100  
    Mouth to Nose: 69.23/100  
    Face Width/Height: 66.30/100  
    Chin-Mouth-Nose: 93.31/100  
    Eye Width/Face: 76.16/100  
    Symmetry: 82.92/100  

    Final Attractiveness Score: 80.41/100  
    ```

🧾 License  
This project is open-source and available under the MIT License.

👤 Author  
Developed by InnerCato

README written by an AI cause my hands were full with another project