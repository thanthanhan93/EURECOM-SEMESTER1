disp = imread('./Images/ground.png');
% Calculate depth
depth = DepthCompute(disp,600,30);
% Median filter to remove outlier
depth = medfilt2(disp,[9 9]);

% 3D Construct
img = imread('./Images/view1.png');
warp(depth,img); rotate3d on;

%% Define threashold for background by clicking points
figure;
img_his = histogram(depth);
[x, ~] = ginput (3);
x = sort(x);

%% Create new depth with 1 black ground - 3 layer frontground
size_d = size(depth);
layer_depth = zeros(size_d(1),size_d(2),3);

layer_r = zeros(size_d(1),size_d(2));
layer_r(find(depth >= x(1) & depth<x(2))) = 255;
layer_depth(:,:,1)=layer_r;

layer_g = zeros(size_d(1),size_d(2));
layer_g(find(depth >= x(2) & depth<x(3))) = 255;
layer_depth(:,:,2)=layer_g;

layer_b = zeros(size_d(1),size_d(2));
layer_b(find(depth >= x(3))) = 255;
layer_depth(:,:,3)=layer_b;

% Best threshold i can get 85 - 160 - 200 as the result i did experiences
% on the histogram.

figure;
imshow(layer_depth);
title ('Different color for each extracted plane');

%% Propose an efficient way to threshold 

% 1/4 Quantile, median, 3/4 quantile is the best option. That means number
% of pixels on each region are equal (4 regions in our problem)
x = [ quantile(depth(:),0.25)  quantile(depth(:),0.5)  quantile(depth(:),0.75)];
size_d = size(depth);
layer_depth = zeros(size_d(1),size_d(2),3);

layer_r = zeros(size_d(1),size_d(2));
layer_r(find(depth >= x(1) & depth<x(2))) = 255;
layer_depth(:,:,1)=layer_r;

layer_g = zeros(size_d(1),size_d(2));
layer_g(find(depth >= x(2) & depth<x(3))) = 255;
layer_depth(:,:,2)=layer_g;

layer_b = zeros(size_d(1),size_d(2));
layer_b(find(depth >= x(3))) = 255;
layer_depth(:,:,3)=layer_b;

figure;
imshow(layer_depth);
title ('Automatic Threshold');
