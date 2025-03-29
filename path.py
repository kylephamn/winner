from PIL import Image
import numpy as np

img = Image.open("Roads_Boundary/South_Clear_Creek_Roads_Mask.tif").convert("L")
img_array = np.array(img)

binary_array = np.where(img_array > 0, 255, 0).astype(np.uint8)
img = Image.fromarray(binary_array)

img.save("output.png")