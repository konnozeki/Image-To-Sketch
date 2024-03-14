import cv2
import matplotlib.pyplot as plt
#to read the image
image= cv2.imread('piano_sketch.png')

im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray= cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#converting image to inverted grayscale
inv_gray= 255-gray

blur_img=cv2.GaussianBlur(inv_gray,(101,101),0)


inv_blur=255-blur_img

sketch_img= cv2.divide(gray,inv_blur,scale=255.0)


plt.figure(figsize=(14,7))

plt.subplot(1,2,1)
plt.title('Actual image in Matplotlib')
plt.imshow(image)
plt.axis('off')


plt.subplot(1,2,2)
plt.title('Color converted image in Matplotlib')
rgb_sketch=cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_sketch)
plt.axis('off')
plt.show()


# saving the picture

# Filename
filename = 'piano_sketch_2.png'

cv2.imwrite(filename, sketch_img)