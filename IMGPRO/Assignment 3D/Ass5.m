%% Ex1: Stereo Matching

% Read image and scale to 0.4
imgL = imread('./Stereo/Dist=2/pair1/x=-0_1.jpg');
imgR = imread('./Stereo/Dist=2/pair1/x=0_1.jpg');
imgL = imresize(imgL,0.4);
imgR = imresize(imgR,0.4);

subplot(1,2,1);imshow(imgL);title('left');
subplot(1,2,2);imshow(imgR);title('right');

%% Try matching function
disp_3 = mat2gray(Matching(imgL,imgR,45,3));
disp_9 = mat2gray(Matching(imgL,imgR,45,9));

imwrite(disp_3,'disp_win3.jpg');
imwrite(disp_9,'disp_win9.jpg');
figure;
subplot(2,2,1);imshow(imgL);title('left');
subplot(2,2,2);imshow(imgR);title('right');
subplot(2,2,3);imshow(disp_3);title('Disparity Map Window=3');
colormap gray
subplot(2,2,4);imshow(disp_9);title('Disparity Map Window=9');
colormap gray

% Diverity map with bigger winder is more smooth than smaller ones.
% Importanly, using small window causes mis-matching. For example, if there
% are same color in a line, so it can detect wrongly the disparity. 
%
% What happens when we increase window size? we compute new value that sum
% of it and its neighbor so that it will reduce mismatching. But if we use
% 
% WindowSize is likely a blurring effect on disparity map (as compared with
% average filtering). Increasing WindowSize helps increase accuracy, but also
% blurs the disparity map.



%% Average filter with small-windowsize image
disp_3_avg = medfilt2(disp_3,[5 5]);
figure;
subplot(1,2,2);imshow(disp_3_avg);title('blurred disparity');
subplot(1,2,1);imshow(disp_3);title('disparity');

%% Try on different dataset
blocksize = 1;
figure;
imgL = imread('./Stereo/Dist=2/pair1/x=-0_1.jpg');
imgR = imread('./Stereo/Dist=2/pair1/x=0_1.jpg');
imgL = imresize(imgL,0.4);
imgR = imresize(imgR,0.4);
disp = medfilt2(mat2gray(Matching(imgL,imgR,45,blocksize)),[3 3]);
subplot(2,2,1);imshow(disp);title('Dist=2,+0.1');

imgL = imread('./Stereo/Dist=2/pair2/x=-0_4.jpg');
imgR = imread('./Stereo/Dist=2/pair2/x=0_4.jpg');
imgL = imresize(imgL,0.4);
imgR = imresize(imgR,0.4);
disp = medfilt2(mat2gray(Matching(imgL,imgR,170,blocksize)),[3 3]);
subplot(2,2,2);imshow(disp);title('Dist=2,+0.4');

imgL = imread('./Stereo/Dist=4/pair1/x=-0_1.jpg');
imgR = imread('./Stereo/Dist=4/pair1/x=0_1.jpg');
imgL = imresize(imgL,0.4);
imgR = imresize(imgR,0.4);
disp = medfilt2(mat2gray(Matching(imgL,imgR,22,blocksize)),[3 3]);
subplot(2,2,3);imshow(disp);title('Dist=4,+0.1');

imgL = imread('./Stereo/Dist=4/pair2/x=-0_4.jpg');
imgR = imread('./Stereo/Dist=4/pair2/x=0_4.jpg');
imgL = imresize(imgL,0.4);
imgR = imresize(imgR,0.4);
disp = medfilt2(mat2gray(Matching(imgL,imgR,85,blocksize)),[3 3]);
subplot(2,2,4);imshow(disp);title('Dist=4,+0.4');

% Increasing Baseline, help us increase the accuracy of detecting depth but also
% make matching confused. Because some region on right image mismatch (black region
% maybe start in object region so that it increases d to get out that
% region) So that is why it obtains a depth of "non-existing" object on right side. 

% Increasing distance, it doesn't help to detect better as i observed.
% Because when you look at it from 2 views, object changes slowly