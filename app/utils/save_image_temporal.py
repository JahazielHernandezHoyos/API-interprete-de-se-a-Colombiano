import os

def save_in_disk(image_bytes: bytes) -> str:
    filename = "temp.jpg"
    with open(filename, "wb") as f:
        f.write(image_bytes)
    return filename