function [ DepthMap] = DepthCompute (disp, B, f )
% Find all value =0 in disp and change to second lowest value or we can
% change to 1. 
A =unique(disp);
disp(find(disp==0)) = A(2);
DepthMap = 1./double(disp)*f*B;