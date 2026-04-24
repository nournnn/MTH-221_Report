clc
clear
close all

% Read the original image
original_image = imread('my_photo.jpeg');

% Define scaling factor
scale_factor = 2;

% Apply interpolation methods
img_nearest  = imresize(original_image, scale_factor, 'nearest');
img_bilinear = imresize(original_image, scale_factor, 'bilinear');
img_bicubic  = imresize(original_image, scale_factor, 'bicubic');

% Display images
figure;

subplot(2,2,1);
imshow(original_image);
title('Original Image');

subplot(2,2,2);
imshow(img_nearest);
title('Nearest Neighbor');

subplot(2,2,3);
imshow(img_bilinear);
title('Bilinear Interpolation');

subplot(2,2,4);
imshow(img_bicubic);
title('Bicubic Interpolation');

% Save results
imwrite(img_nearest,  'nearest.jpg');
imwrite(img_bilinear, 'bilinear.jpg');
imwrite(img_bicubic,  'bicubic.jpg');
