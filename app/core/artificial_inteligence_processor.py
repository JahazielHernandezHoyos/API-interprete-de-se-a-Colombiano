from core.coordinate_normalization import obtenerAngulos
from core.conditions_predict import condicionalesLetras
import mediapipe as mp
import cv2
import os


async def process(image_path):
    """
    Process one image with mediapipe with image_path and return result in dict
    """
    mp_hands = mp.solutions.hands
    with mp_hands.Hands(
        static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5
    ) as hands:
        image = cv2.flip(cv2.imread(image_path), 1)
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if not results.multi_hand_landmarks:
            return {}
        width, height, _ = image.shape
        angulosid = obtenerAngulos(results, width, height)[0]
        dedos = ()
        # pulgar externo
        if angulosid[5] > 125:
            dedos += (1,)
        else:
            dedos += (0,)
        # pulgar interno
        if angulosid[4] > 150:
            dedos += (1,)
        else:
            dedos += (0,)
        # 4 dedos
        for id in range(0, 4):
            if angulosid[id] > 90:
                dedos += (1,)
            else:
                dedos += (0,)
        totalDedos = dedos.count(1)
        data = condicionalesLetras(dedos)

    return data
