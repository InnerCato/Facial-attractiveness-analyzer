import numpy as np

# Ideal ratios for facial attractiveness (these should be customized or based on research)
IDEAL_RATIOS = {
    "golden_ratio": 1.618,
    "eye_spacing": 1.0,
    "mouth_nose": 1.5,
    "face_width_height": 1.5,
    "chin_mouth_nose": 1.6,
    "eye_width_face": 0.3
}

def calculate_ratio(p1, p2, p3, p4):
    """Calculate proportion between two distances."""
    d1 = p1 / p2 if p2 != 0 else 0
    d2 = p3 / p4 if p4 != 0 else 0
    return d1 / d2 if d2 != 0 else 0

def score_ratio(measured, ideal, weight=1.0):
    """Calculate how close a ratio is to the ideal value (normalized to 0-100)."""
    deviation = abs(measured - ideal) / ideal
    return max(0, 100 - (deviation * 100 * weight))  # Higher score = closer to ideal

def analyze_face_from_measurements():
    """Analyze face based on user-provided measurements."""
    print("\nPlease enter the following measurements in millimeters:")

    # Prompt user for measurements
    eye_length = float(input("Right Eye Length: "))
    left_eye_length = float(input("Left Eye Length: "))
    nose_width = float(input("Nose Width: "))
    eye_to_eye_distance = float(input("Distance Between Eyes: "))
    face_width = float(input("Face Width (from ear to ear): "))
    face_length = float(input("Face Length (from chin to forehead): "))
    mouth_width = float(input("Mouth Width: "))
    mouth_to_nose_length = float(input("Mouth to Nose Length: "))

    # Calculate ratios based on the user input
    eye_spacing_ratio = calculate_ratio(eye_to_eye_distance, eye_length, left_eye_length, eye_length)
    face_width_height_ratio = calculate_ratio(face_width, face_length, face_width, face_length)  # Placeholder, should compare actual proportions
    golden_ratio = calculate_ratio(eye_length, nose_width, face_width, face_length)
    chin_mouth_nose = calculate_ratio(mouth_width, mouth_to_nose_length, mouth_width, nose_width)  # Placeholder for chin-related calculations

    # Calculate individual scores
    scores = {
        "Golden Ratio": score_ratio(golden_ratio, IDEAL_RATIOS["golden_ratio"]),
        "Eye Spacing": score_ratio(eye_spacing_ratio, IDEAL_RATIOS["eye_spacing"]),
        "Mouth to Nose": score_ratio(chin_mouth_nose, IDEAL_RATIOS["mouth_nose"]),
        "Face Width/Height": score_ratio(face_width_height_ratio, IDEAL_RATIOS["face_width_height"]),
        "Chin-Mouth-Nose": score_ratio(chin_mouth_nose, IDEAL_RATIOS["chin_mouth_nose"]),
    }

    # Final score (average of all scores)
    final_score = sum(scores.values()) / len(scores)

    # Print results
    print("\n--- Facial Attractiveness Analysis (from Measurements) ---")
    for key, value in scores.items():
        print(f"{key}: {value:.2f}/100")
    print(f"\nFinal Attractiveness Score: {final_score:.2f}/100")

analyze_face_from_measurements()