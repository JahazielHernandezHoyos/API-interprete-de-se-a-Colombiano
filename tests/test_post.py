import io
from io import BytesIO
from PIL import Image
import requests
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK
from app.main import app

client = TestClient(app)

def test_call_processing_images_with_valid_image():
    """
    Prueba el endpoint "/processing_images" con una imagen de prueba.
    """
    # Creamos una imagen de prueba
    image = Image.new("RGB", (200, 200), color=(255, 0, 0))
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="JPEG")
    image_bytes.seek(0)

    # Enviamos la imagen en el cuerpo de la solicitud POST
    response = client.post(
        "/processing_images",
        files={"image": ("test_image.jpg", image_bytes, "image/jpeg")},
    )

    # Verificamos la respuesta del servidor
    assert response.status_code == HTTP_200_OK


def test_call_processing_images_with_valid_image_url():
    # Descargamos la imagen de prueba desde una URL
    url = "https://cdn.goconqr.com/uploads/media/image/40154530/desktop_56858307-5cf0-4d5e-a2e7-19023ef8ed96.jpeg"
    response = requests.get(url)
    image_bytes = BytesIO(response.content)

    # Enviamos la imagen en el cuerpo de la solicitud POST
    response = client.post(
        "/processing_images",
        files={"image": ("test_image.jpg", image_bytes, "image/jpeg")},
    )

    # Verificamos la respuesta del servidor
    assert response.status_code == HTTP_200_OK

    # Verificamos que la respuesta del servidor contenga la letra "A"
    assert "A" in response.json()
    assert "B" not in response.json()


def test_read_root():
    """
    Prueba el endpoint "/" y verifica que devuelve un saludo en formato JSON.
    """
    response = client.get("/")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"message": "👋🌎"}
