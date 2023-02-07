import mediapipe as mp
from math import degrees, acos
import numpy as np

# actualizacion
mp_hands = mp.solutions.hands


def obtenerAngulos(results, width, height):
    """
    Este código utiliza la biblioteca MediaPipe para detectar puntos de referencia de manos en una imagen
    y calcular los ángulos entre los diferentes handmarks de los dedos. Primero, configura un diccionario
    de las coordenadas x e y de la tip, pip, y mcp (articulación metacarpiano-falángica) de cada dedo.
    Luego usa el producto escalar y la función arcocoseno para calcular los ángulos entre cada uno de
    los handmarks de los dedos. Los ángulos se almacenan en una lista de ángulos y la función los devuelve.
    El código convierte la lista de puntos en una matriz de forma (6, 3, 2) para realizar
    operaciones de vector de bloque.
    Se calcula la distancia y se calculan 6 ángulos.
    El código devuelve la lista de ángulos y la posición de la punta del dedo meñique en la imagen.
    """

    def get_xy(index):
        return [
            int(hand_landmarks.landmark[index].x * width),
            int(hand_landmarks.landmark[index].y * height),
        ]

    for hand_landmarks in results.multi_hand_landmarks:
        # Diccionario de coordenadas de cada dedo
        dedos = {
            "meñique": [
                get_xy(mp_hands.HandLandmark.PINKY_TIP),
                get_xy(mp_hands.HandLandmark.PINKY_PIP),
                get_xy(mp_hands.HandLandmark.PINKY_MCP),
            ],
            "anular": [
                get_xy(mp_hands.HandLandmark.RING_FINGER_TIP),
                get_xy(mp_hands.HandLandmark.RING_FINGER_PIP),
                get_xy(mp_hands.HandLandmark.RING_FINGER_MCP),
            ],
            "medio": [
                get_xy(mp_hands.HandLandmark.MIDDLE_FINGER_TIP),
                get_xy(mp_hands.HandLandmark.MIDDLE_FINGER_PIP),
                get_xy(mp_hands.HandLandmark.MIDDLE_FINGER_MCP),
            ],
            "indice": [
                get_xy(mp_hands.HandLandmark.INDEX_FINGER_TIP),
                get_xy(mp_hands.HandLandmark.INDEX_FINGER_PIP),
                get_xy(mp_hands.HandLandmark.INDEX_FINGER_MCP),
            ],
            "pulgar": [
                get_xy(mp_hands.HandLandmark.THUMB_TIP),
                get_xy(mp_hands.HandLandmark.THUMB_IP),
                get_xy(mp_hands.HandLandmark.THUMB_MCP),
            ],
            "pulgar_interno": [
                get_xy(mp_hands.HandLandmark.THUMB_TIP),
                get_xy(mp_hands.HandLandmark.THUMB_MCP),
                get_xy(mp_hands.HandLandmark.WRIST),
            ],
        }
        # Extraccion de puntos (x, y)
        dedos_array = np.concatenate([np.array(dedo) for dedo in dedos.values()])
        # El código convierte la lista de puntos en una matriz con forma (6, 3, 2)
        # para poder realizar operaciones vectoriales en bloque.
        puntos = dedos_array.reshape(-1, 3, 2)

        # Calculo de distancia
        l_list = np.linalg.norm(puntos[:, [0, 1], :] - puntos[:, [1, 2], :], axis=2)

        # Calculo 5 angulos
        num_den_list = np.sum(
            (puntos[:, 0, :] - puntos[:, 1, :]) * (puntos[:, 2, :] - puntos[:, 1, :]),
            axis=1,
        ) / (l_list[:, 0] * l_list[:, 1])

        angulos = np.degrees(np.arccos(num_den_list))
        pinky = [
            int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * width),
            int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * height),
        ]
        angulos = angulos.tolist()
        return [angulos, pinky]