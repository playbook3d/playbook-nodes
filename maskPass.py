from PIL import Image, ImageOps
import numpy as np
import torch
import requests
from io import BytesIO
import hashlib
import time

class MaskRenderPass:
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

    RETURN_TYPES = ("IMAGE", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("Mask", "Color 1", "Color 2", "Color 3", "Color 4", "Color 5", "Color 6", "Color 7", "Color 8")

    FUNCTION = "parse_mask"

    OUTPUT_NODE = { False }

    CATEGORY = "Playbook 3D"

    def parse_mask(self, api_key):
        base_url = "https://accounts.playbookengine.com"

        jwt_request = requests.get(f"{base_url}/token-wrapper/get-tokens/{api_key}")
        try:
            if jwt_request is not None:
                user_token = jwt_request.json()["access_token"]
                headers = {"Authorization": f"Bearer {user_token}"}
                mask_request = requests.get(f"{base_url}/upload-assets/get-download-urls", headers=headers)
                if mask_request.status_code == 200:
                    mask_url = mask_request.json()["mask"]
                    mask_response = requests.get(mask_url)
                    image = Image.open(BytesIO(mask_response.content))
                    image = ImageOps.exif_transpose(image)
                    image = image.convert("RGB")
                    image = np.array(image).astype(np.float32) / 255.0
                    image = torch.from_numpy(image)[None,]
                    return [image, "#ffe906", "#0589d6", "#a2d4d5", "#000016", "#00ad58", "#f084cf", "#ee9e3e", "#e6000c"]
        except Exception as e:
            print(f"Error with node: {e}")
        


NODE_CLASS_MAPPINGS = {
    "Playbook Mask": MaskRenderPass
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Playbook Mask": "Playbook Mask Render Passes"
}