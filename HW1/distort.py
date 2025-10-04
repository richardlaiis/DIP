import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_radial_distortion(img, k1=0.0, k2=0.0, k3=0.0):
    k1 = -k1
    k2 = -k2
    h, w = img.shape[:2]
    cx, cy = w / 2.0, h / 2.0  # principal point = image center
    fx = fy = w                # focal length (heuristic choice)

    # Build meshgrid of pixel coordinates
    x = np.linspace(0, w-1, w)
    y = np.linspace(0, h-1, h)
    xx, yy = np.meshgrid(x, y)

    # Normalize to camera coordinates
    x_norm = (xx - cx) / fx
    y_norm = (yy - cy) / fy
    r2 = x_norm**2 + y_norm**2

    # Apply radial distortion model
    factor = 1 + k1*r2 + k2*r2**2 + k3*r2**3
    x_distorted = x_norm * factor
    y_distorted = y_norm * factor

    # Convert back to pixel coordinates
    u = x_distorted * fx + cx
    v = y_distorted * fy + cy

    # Build remap maps (must be float32 for cv2.remap)
    map_x = u.astype(np.float32)
    map_y = v.astype(np.float32)

    # Warp the image
    distorted = cv2.remap(img, map_x, map_y, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    return distorted


# Load image
img = cv2.imread("me.jpg")   # Replace with your image
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

x = 0.5

# Apply barrel (k1 < 0) and pincushion (k1 > 0)
barrel = apply_radial_distortion(img, k1=-x)
pincushion = apply_radial_distortion(img, k1=x)

# Show results
plt.figure(figsize=(12,6))
plt.subplot(1,3,1), plt.imshow(img), plt.title("Original")
plt.subplot(1,3,2), plt.imshow(barrel), plt.title(f"Barrel (k1={-x})")
plt.subplot(1,3,3), plt.imshow(pincushion), plt.title(f"Pincushion (k1={x})")
plt.show()

