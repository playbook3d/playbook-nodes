from PIL import Image, ImageOps
import numpy as np
import torch
import requests
from io import BytesIO

class BeautyRenderPass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "api_key": ("STRING", { "multiline": False })
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("Beauty",)

    FUNCTION = "parse_beauty"

    OUTPUT_NODE = { False }

    CATEGORY = "Playbook 3D"

    def parse_beauty(self, api_key):
        base_url = "https://accounts.playbookengine.com"

        jwt_request = requests.get(f"{base_url}/token-wrapper/get-tokens/{api_key}")
        try:
            if jwt_request is not None:
                user_token = jwt_request.json()["access_token"]
                headers = {"Authorization": f"Bearer {user_token}"}
                beauty_request = requests.get(f"{base_url}/upload-assets/get-download-urls", headers=headers)
                if beauty_request.status_code == 200:
                    beauty_url = beauty_request.json()["beauty"]
                    beauty_response = requests.get(beauty_url)
                    image = Image.open(BytesIO(beauty_response.content))
                    image = ImageOps.exif_transpose(image)
                    image = image.convert("RGB")
                    image = np.array(image).astype(np.float32) / 255.0
                    image = torch.from_numpy(image)[None,]
                    return [image]
        except Exception as e:
            print(f"Error with node: {e}")
        


NODE_CLASS_MAPPINGS = {
    "Playbook Beauty": BeautyRenderPass
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Playbook Beauty": "Playbook Beauty Render Passes"
}