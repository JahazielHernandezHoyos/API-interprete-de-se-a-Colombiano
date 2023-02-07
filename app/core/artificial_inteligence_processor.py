import mediapipe as mp
import cv2
import os

async def process(image_path):
    """
    Process one image with mediapipe with image_path and return result in dict
    """
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    data = {}
    # For static images:
    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=2,
        min_detection_confidence=0.5) as hands:
        # Read an image, flip it around y-axis for correct handedness output (see
        # above).
        image = cv2.flip(cv2.imread(image_path), 1)
        # Convert the BGR image to RGB before processing.
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # Print handedness and draw hand landmarks on the image.
        # print('Handedness:', results.multi_handedness)
        if not results.multi_hand_landmarks:
            return {}
        image_height, image_width, _ = image.shape
        annotated_image = image.copy()
        for hand_landmarks in results.multi_hand_landmarks:
            # print('hand_landmarks:', hand_landmarks)
            # print(
            #     f'Index finger tip coordinates: (',
            #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
            #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
            # )
            #add x and y to data
            data['x'] = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width
            data['y'] = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height
        #     mp_drawing.draw_landmarks(
        #         annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        # cv2.imwrite(
        #     os.path.join(
        #         os.path.dirname(image_path), 'annotated_image' + os.path.splitext(image_path)[1]),
        #     cv2.flip(annotated_image, 1))
    return data



