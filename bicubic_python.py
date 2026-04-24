import cv2
import matplotlib.pyplot as plt

# Load image
original_image = cv2.imread('my_photo.jpeg')

# Check if image is loaded correctly
if original_image is None:
    print("Error: Image not found!")
    exit()

# Scale factor
scale_factor = 2
new_width = int(original_image.shape[1] * scale_factor)
new_height = int(original_image.shape[0] * scale_factor)

# Apply interpolation methods
img_nearest = cv2.resize(original_image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)
img_bilinear = cv2.resize(original_image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
img_bicubic = cv2.resize(original_image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

# Convert BGR to RGB for display
original_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
nearest_rgb = cv2.cvtColor(img_nearest, cv2.COLOR_BGR2RGB)
bilinear_rgb = cv2.cvtColor(img_bilinear, cv2.COLOR_BGR2RGB)
bicubic_rgb = cv2.cvtColor(img_bicubic, cv2.COLOR_BGR2RGB)

# Display images
plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.imshow(original_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(nearest_rgb)
plt.title('Nearest Neighbor')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(bilinear_rgb)
plt.title('Bilinear Interpolation')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(bicubic_rgb)
plt.title('Bicubic Interpolation')
plt.axis('off')

plt.tight_layout()
plt.show()

# Save results
cv2.imwrite('nearest.jpg', img_nearest)
cv2.imwrite('bilinear.jpg', img_bilinear)
cv2.imwrite('bicubic.jpg', img_bicubic)

print("All images saved successfully!")
