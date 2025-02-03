import base64

def get_base64_image(image_path: str) -> str:
    """
    Lê a imagem do caminho especificado e retorna uma string base64.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()