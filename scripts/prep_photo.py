import sys
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep(image_path, output_path="source-prepped.png"):
    # 1. Background remove
    inp = Image.open(image_path)
    no_bg = remove(inp)
    
    # 2. White background composite
    white_bg = Image.new("RGBA", no_bg.size, (255, 255, 255, 255))
    composite = Image.alpha_composite(white_bg, no_bg).convert("L")
    
    # 3. CLAHE (Contrast Boost)
    img_arr = np.array(composite)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(img_arr)
    
    cv2.imwrite(output_path, enhanced)
    print(f"Prepped photo saved to {output_path}")

if __name__ == "__main__":
    img_file = sys.argv[1] if len(sys.argv) > 1 else "source-photo.jpg"
    prep(img_file)