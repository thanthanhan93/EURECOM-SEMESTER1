function [ disp ] = Matching( imL,imR, dmax, WinSize )
%size of the image
[N M P]=size(imL);
%convert the stereo pair to double
imL=double(imL);
imR=double(imR);
% initialize the disparity map
disp=zeros(N,M);

% Store all values of SAD in different disparity 
SAD = zeros(N,M,dmax+1);

% First, we expand right image on the left side with black pixel (zero value) 
% in case of x+window size-d < 0. 

% Then, we find difference value of 2 image with disparity d and absolute

% Next, we apply convolution square matrix (size = WindowSize) with
% value 1 to calculate dissimilarity between 2 block

% Fianlly, sum all value on 3 diffrent channel RBG

for d = 0:1:dmax
    dif_3channel = abs(imL - cat(2,zeros(N,d,3),imR(:,1:end-d,:)));
    for i=1:3
        dif_3channel(:,:,i) = filter2(ones(WinSize),dif_3channel(:,:,i));
    end;
    SAD(:,:,d+1) = sum(dif_3channel,3);
end

% Find the best disparity

[~, disp] = min(SAD,[],3);

% for i=1:1:N
%     for j=1:1:M
%         disp(i,j) = find(SAD(i,j,:)==disp(i,j),1,'last');
%     end
% end
