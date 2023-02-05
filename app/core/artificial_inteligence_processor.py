import mediapipe as mp

def process(image_path):
    # Load the image using mediapipe
    image = mp.load_image(image_path)

    # Apply the artificial intelligence processing to the image
    result = mp.run_inference(image)
    print(result)
    return result




