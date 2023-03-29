import cv2
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('dark_background')
# importing image
image = cv2.imread('image.jpg')
# Denoising
process = cv2.fastNlMeansDenoisingColored(image, None, 12, 7, 5, 20)
# tone mapping
pic = cv2.imread(image, cv2.IMREAD_ANYDEPTH)
tonemap = cv2.createTonemapDurand(2.2)
mapper = tonemapDurand.process(pic)
converter = np.clip(ldrDurand * 255, 0, 255).astype('uint8')
# Displaying
row = 1
column = 2
design = axis = plt.subplots(row, column, figsize=(15, 10))
design.tight_layout()
axis[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axis[0].set_title('Original')
axis[1].imshow(cv2.cvtColor(process, cv2.COLOR_BGR2RGB))
axis[1].set_title('Denoised')
axis[2].imshow(cv2.cvtColor(converter, cv2.COLOR_BGR2RGB))
axis[2].set_title('Tone Mapped')
plt.show()
