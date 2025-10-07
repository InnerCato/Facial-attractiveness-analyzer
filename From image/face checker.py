import cv2
import dlib
import numpy as np
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
predictor_path = os.path.join(base_dir, "shape_predictor_68_face_landmarks.dat")
num = int(input("Enter image num: "))

image_dir = os.path.join(base_dir, "Images")
image_path = None
for ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"]:
    candidate = os.path.join(image_dir, f"face{num}{ext}")
    if os.path.exists(candidate):
        image_path = candidate
        break

if image_path is None:
    print("❌ No image found for that number (supported: jpg, png, bmp, tiff, webp).")
    exit()

# Load face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

# Ideal ratios for facial attractiveness
IDEAL_RATIOS = {
    "eye_spacing": 1.5,
    "mouth_nose": 1.5,
    "face_width_height": 1.5,
    "chin_mouth_nose": 1.6,
    "eye_width_face": 0.15,
    "symmetry" : 0.05
}

def calculate_ratio(p1, p2, p3, p4):
    """Calculate proportion between two distances."""
    d1 = np.linalg.norm(np.array(p1) - np.array(p2))
    d2 = np.linalg.norm(np.array(p3) - np.array(p4))
    return d1 / d2 if d2 != 0 else 0

def score_ratio(measured, ideal, weight=1.0):
    deviation = abs(measured - ideal) / ideal
    print(deviation)
    score = 100 * np.exp(-2 * deviation)  # exponential penalty
    return score


def analyze_face(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)
    if len(faces) == 0:
        print("No face detected.")
        return
    
    for face in faces:
        landmarks = predictor(gray, face)
        points = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(68)]
        
        # Calculate ratios
        left_eye_width  = np.linalg.norm(np.array(points[36]) - np.array(points[39]))
        right_eye_width = np.linalg.norm(np.array(points[42]) - np.array(points[45]))
        inter_eye_dist  = np.linalg.norm(np.array(points[39]) - np.array(points[42]))

        eye_spacing = inter_eye_dist / ((left_eye_width + right_eye_width)/2)
        mouth_nose_ratio = calculate_ratio(points[48], points[54], points[31], points[35])
        face_width_height = calculate_ratio(points[0], points[16], points[8], points[27])
        chin_mouth_nose = calculate_ratio(points[8], points[48], points[48], points[33])
        eye_width_face = calculate_ratio(points[36], points[39], points[0], points[16])

        face_width = np.linalg.norm(np.array(points[0]) - np.array(points[16]))
        sym_points = [(36, 45), (39, 42), (21, 22), (17, 26), (3, 13)]
        sym_devs = []
        for left, right in sym_points:
            dev = abs(points[left][0] - (points[0][0] + points[16][0] - points[right][0]))
            sym_devs.append(dev / face_width)
        symmetry = np.mean(sym_devs)

        # Calculate individual scores
        scores = {
            "Eye Spacing": score_ratio(eye_spacing, IDEAL_RATIOS["eye_spacing"]),
            "Mouth to Nose": score_ratio(mouth_nose_ratio, IDEAL_RATIOS["mouth_nose"]),
            "Face Width/Height": score_ratio(face_width_height, IDEAL_RATIOS["face_width_height"]),
            "Chin-Mouth-Nose": score_ratio(chin_mouth_nose, IDEAL_RATIOS["chin_mouth_nose"]),
            "Eye Width/Face": score_ratio(eye_width_face, IDEAL_RATIOS["eye_width_face"]),
            "Symmetry": score_ratio(symmetry, IDEAL_RATIOS["symmetry"])
        }

        weights = {
            "Symmetry": 4.0,
            "Eye Spacing": 2.0,
            "Mouth to Nose": 1.0,
            "Face Width/Height": 2.0,
            "Chin-Mouth-Nose": 1.0,
            "Eye Width/Face": 1.0
        }
        final_score = sum(scores[key] * weights[key] for key in scores) / sum(weights.values())
        
        # Print results
        print("\n--- Facial Attractiveness Analysis ---")
        for key, value in scores.items():
            print(f"{key}: {value:.2f}/100")
        print(f"\nFinal Attractiveness Score: {final_score:.2f}/100")

    cv2.imshow("Face Analysis", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the function with an image
analyze_face(image_path)
