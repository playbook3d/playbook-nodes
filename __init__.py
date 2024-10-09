from .depthPass import DepthRenderPass
from .outlinePass import OutlineRenderPass
from .maskPass import MaskRenderPass
from .beautyPass import BeautyRenderPass

NODE_CLASS_MAPPINGS = {
    "Playbook Depth": DepthRenderPass,
    "Playbook Outline": OutlineRenderPass,
    "Playbook Mask": MaskRenderPass,
    "Playbook Beauty": BeautyRenderPass
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Playbook Depth": "Playbook Depth Render Pass",
    "Playbook Outline": "Playbook Outline Render Pass",
    "Playbook Mask": "Playbook Mask Render Pass",
    "Playbook Beauty": "Playbook Beauty Render Pass"
}


__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']