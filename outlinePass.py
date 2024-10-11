from PIL import Image, ImageOps
import numpy as np
import torch
import requests
from io import BytesIO
import hashlib
import time


class OutlineRenderPass:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "api_key": ("STRING", { "multiline": False })
            },
        }

    @classmethod
    def IS_CHANGED(s, image):
        # always update
        m = hashlib.sha256().update(str(time.time()).encode("utf-8"))
        return m.digest().hex()

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("Image",)

    FUNCTION = "parse_outline"

    OUTPUT_NODE = { False }

    CATEGORY = "Playbook 3D"

    def parse_outline(self, api_key):
        base_url = "https://accounts.playbookengine.com"
        user_token = None

        jwt_request = requests.get(f"{base_url}/token-wrapper/get-tokens/{api_key}")

        try:
            if jwt_request is not None:
                user_token = jwt_request.json()["access_token"]
        except Exception as e:
            print(f"Error with node: {e}")
            raise ValueError("API Key not found/Incorrect")

        try:
            headers = {"Authorization": f"Bearer {user_token}"}
            outline_request = requests.get(f"{base_url}/upload-assets/get-download-urls", headers=headers)
            if outline_request.status_code == 200:
                outline_url = outline_request.json()["outline"]
                outline_response = requests.get(outline_url)
                image = Image.open(BytesIO(outline_response.content))
                image = ImageOps.exif_transpose(image)
                image = image.convert("RGB")
                image = np.array(image).astype(np.float32) / 255.0
                image = torch.from_numpy(image)[None,]
                return [image]
        except Exception:
            raise ValueError("Canny not uploaded")
        


NODE_CLASS_MAPPINGS = {
    "Playbook Outline": OutlineRenderPass
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Playbook Outline": "Playbook Outline Render Pass"
}