class PlaybookNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {

            }
        }

    RETURN_TYPES = {}
    RETURN_NAMES = {}

    FUNCTION = {}

    OUTPUT_NODE = {}

    CATEGORY = {"Playbook/<node>"}

    def node_function(self):
        # Functions that the node would need
        print("node is running")


    NODE_CLASS_MAPPINGS = {}

    NODE_DISPLAY_NAME_MAPPINGS = {}