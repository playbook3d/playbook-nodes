# Playbook3D Render Nodes for ComfyUI

This repository provides custom nodes for ComfyUI that allow you to seamlessly integrate Playbook3D renders into your workflows.

**Features:**

* **Dedicated Render Nodes:**  Access individual nodes for different render passes:
    * **Beauty:**  Get the final rendered image.
    * **Canny:**  Extract edge information with Canny edge detection.
    * **Depth:**  Obtain depth information as a grayscale image.
    * **Mask:**  Generate masks for specific objects or materials.

**Getting Started:**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/playbook3d/playbook-nodes.git
   
## Install
Copy the contents of this repository into your custom_nodes folder within your ComfyUI installation directory.

## Obtain an API Key 
Visit beta.playbook3d.com to sign up for a Playbook3D account and obtain your API key.

## Configure Nodes
In your ComfyUI workflow, add the desired Playbook3D render nodes and input your API key in the designated field.

## Requirements
-ComfyUI (latest version recommended)
-Playbook3D account and API key

## Usage
Connect the Playbook3D render nodes to your existing ComfyUI workflows.  Each node outputs an image corresponding to the selected render pass. You can then use these images as inputs for other nodes in your workflow, such as image processing, compositing, or style transfer.

## Example Workflow:
Use a Playbook3D Beauty node to generate a base render.
Connect a Playbook3D Canny node to extract edges from the render.
Use a Combine node to overlay the edges on the original render for a stylized effect.

## Contributing:
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.   

## License:
This project is licensed under the MIT License.

## Contact:
For questions or support, please contact alex@playbook3d.com or join the Playbook3D Discord server.   
