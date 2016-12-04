%% III. Anaglyph producing and perceiving
% Read the image
imL = imread ('./Pair_anaglyph/x=0.1.jpg');
imR = imread ('./Pair_anaglyph/x=0.0.jpg');

% Create the anaglyph
Anaglyph = imR;
Anaglyph(:, :, 1) = imL(:, :, 1);
imshow (Anaglyph, []);