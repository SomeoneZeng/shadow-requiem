import cv2
import numpy as np 

# Load two images
img1 = cv2.imread('play_stand_1.png',cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('player_move_1.png',cv2.IMREAD_UNCHANGED)

# # Concatenate images horizontally
# concatenated_img = cv2.hconcat([img1, img2])

# # Save the concatenated image
# cv2.imwrite('concatenated_image.jpg', concatenated_img)

# print("Images have been concatenated and saved as 'concatenated_image.jpg'.")

print(img1.shape)

h1,w1,c1 = img1.shape
h2,w2,c2 = img2.shape

final_h = h1+h2
final_w = max(w1, w2)

final_img = np.zeros((final_h, final_w, 4), dtype=np.uint8)
final_img[0:h1, 0:w1,:] = img1
final_img[h1:h1+h2, 0:w2,:] = img2

# cv2.imshow('Final Image', final_img)
# cv2.waitKey(0)

cv2.imwrite('final_image.png', final_img)
