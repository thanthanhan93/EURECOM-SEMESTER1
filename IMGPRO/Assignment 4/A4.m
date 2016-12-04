%% Step 1: Load the image and add noice

I = imread('ic.tif');
I = rgb2gray(I);
I_noise = imnoise(I,'gaussian',0,.04);

figure;
subplot(1,2,1); imshow(I_noise); title('noise');
subplot(1,2,2); imshow(I); title('origin');

%% Step 2: denoise
I_med = medfilt2(I_noise, [3 3],'symmetric');
I_wien = wiener2(I_noise,[3 3]);
I_ave = imfilter(I_noise,fspecial('average',3));

figure;
subplot(2,3,2); imshow(I_noise); title('noise');
subplot(2,3,4); imshow(I_med); title('median 3x3');
subplot(2,3,5); imshow(I_ave); title('average 3x3');
subplot(2,3,6); imshow(I_wien); title('wiener 3x3');

%% Step 3: Highlight edge

% GRADIENT METHOD

% Find Gradient
[gradX,gradY] = imgradientxy(I);
% Find norm
grad_norm = sqrt(gradX.^2+gradY.^2)/255;
% Get threshold
level = graythresh(grad_norm);
% Build edge dection image
img_GR = im2bw(grad_norm,level);
img_GR = bwmorph(img_GR,'thin');

% LAPLACIAN 
img_Lap = edge(I_med,'log');
% CANNY
img_Canny = edge(I_med,'Canny');

% Show result
figure;
subplot(2,3,2); imshow(I_med); title('median 3x3');
subplot(2,3,4); imshow(img_GR); title('Gradient M.');
subplot(2,3,5); imshow(img_Lap); title('Laplacian M.');
subplot(2,3,6); imshow(img_Canny); title('Canny M.');

%% Step 4: Radon transform

figure;
[R,xp]= radon(img_GR);
imagesc(0:180,xp,R); xlabel('\theta (degrees)'); ylabel('X\prime'); set(gca,'XTick',0:10:180);
colormap(hot);
colorbar

% How Radon transform ralte to Hough transform?
% It map from Cartesian coordinate to polar coordinate (\phi,\theta). That
% means we can define position of edge by a pair (\phi,\theta)

% Explain why sum of any column of Radon transform is always the same?
% At each angel, it only changes distribution of pixel contains information
% (white value in edge picture) so that we can detect edge by seeing
% whether the peak is clear or not. As you can see from plot below, plot x'
% with phi=130 we cannot define peak, the peak is not clear but in plot x'
% with phi=6 we can easily detect peak that is also be brightest points in
% color map. 
plot(1:293,R(:,130));
plot(1:293,R(:,6));

%% Step 5: Radon trasnform and observe associated lines
interactiveLine(img_GR,R,5);

%% Step 6: Find The image orientation and rotate it
col_90 = max(R(:,1:90));
col_180 = max(R(:,91:180));
figure;
subplot(1,3,1); plot(col_90); title('V(1:90)');
subplot(1,3,2); plot(91:180,col_180); title('V(91:180)');
subplot(1,3,3); plot(col_90+col_180); title('V(1:90)+V(91:180)');
% Why we find maximum on 2 ranges. It depends on the characteristic of
% image. In this image. There are lots of line that are orthorgonal, the 
% range from 0:90 to find vertical line and 91:180 find horizontal line, so
% rotate \phi or \phi+90 is not different. Sum operation is a good way to
% enhance our result because we combine both information horizontal and
% vertical line rather than using one of them (find maximum of whole array)

sum = col_90+col_180;
%Find maximum and index of V(1:90)+V(91:180)
[max_i index_i] = max(sum(:));
%Find \phi and \theta in R that satisfy value of maximum
[rowOfMax, columnOfMax] = find(R == col_90(index_i));
rotatedImage = imrotate(I, -columnOfMax);
rotatedImage2 = imrotate(I, -columnOfMax+90);
%rotate image
figure;
subplot(1,3,1); imshow(I); title('origina');
subplot(1,3,2); imshow(rotatedImage); title('rotate \phi');
subplot(1,3,3); imshow(rotatedImage2); title('ratate \phi+90');

%% Advance question
% Gaussian noise = 0.01:0.03:0.6. Median filter [3 3]
dirNoise='/Users/nyr/Documents/MATLAB/Noise';
dirRotated='/Users/nyr/Documents/MATLAB/Rotate';
 % No need to worry about slashes now!
k=1;
for i = 0.01:0.04:0.8
    % Noise
    I_noise = imnoise(I,'gaussian',0,i);
    % Reduce noise
    I_med = medfilt2(I_noise, [3 3]);
    % Edge
    I_edge = edge(I_med,'Canny');
    % Rotate
    [R,xp]= radon(I_edge);
    col_90 = max(R(:,1:90));
    col_180 = max(R(:,91:180));
    sum = col_90+col_180;
    [max_i,index_i] = max(sum(:));
    [rowOfMax, columnOfMax] = find(R == col_90(index_i));
    rotatedImage = imrotate(I_noise, -columnOfMax);
    %Write file
    baseFileName = sprintf('MED3%d.png', k); % e.g. "1.png"
    fullFileName = fullfile(dirRotated, baseFileName);
    imwrite(rotatedImage, fullFileName);
    k = k+1;
end;

% In my experiment when gaussian noise with var~0.53. It can't find correct
% angel. Because when we reduce noise. it lost information about edge. the
% edge is not clear enough to detect.