# Astronomical Super-Resolution

<p align="center">
  <img src="images/original.jpg" alt="Image 1" width="30%" />
  <img src="images/superes.jpg" alt="Image 2" width="30%" />
</p>


## Table of contents

- [SRCNN-PyTorch](##Background)
- [Dataset](##Dataset)
- [System](##System)
    - [System Architecture](#SystemArchitecture)
- 



## Background

The goal of this project is to enhance low-resolution astronomical images using a Convolutional Neural Network (CNN) designed for super-resolution. Given the high computational cost and large dataset typically required to train such a model from scratch, I applied transfer learning on a smaller dataset, allowing for shorter training times while still achieving effective results.

## Dataset

<p align="center">
  <img src="images/dataset1.jpg" alt="Image 1" width="20%" />
  <img src="images/dataset2.jpg" alt="Image 2" width="20%" />
  <img src="images/dataset3.jpg" alt="Image 1" width="20%" />
  <img src="images/dataset4.jpg" alt="Image 2" width="20%" />
</p>

Finding a suitable dataset of astronomical images was more challenging than anticipated. Ultimately, I used images from the European Space Agency (ESA) archives. The dataset preparation involved several steps:

1. **Data Download**: The images were downloaded using a script located at `data/image_downloader.py`.
2. **Image Filtering**: Many images in the ESA archive were either illustrations or computer-generated. These images were manually sorted to exclude non-astronomical visuals.
3. **Image Preprocessing**:
   - All images were resized to a uniform resolution of **256x256 pixels** to serve as the ground truth for the model’s output.
   - Each image was then downscaled to **128x128 pixels** to generate the input images for the model.

   The preprocessing steps are saved in `data/image_preprocess.py`.

Due to GitHub’s size restrictions, the final dataset is hosted externally. You can access it here: [Google Drive Link](https://drive.google.com/drive/folders/1o1gHGsB3rfzVlgF-8NLJUdxz0WzPK0zq?usp=sharing).


## System

I used a pre-trained Super-Resolution CNN from [this repository](https://github.com/Lornatang/SRCNN-PyTorch?tab=readme-ov-file). The original model was modified to include an initial bicubic interpolation layer to upscale the input image, as the original model required the input and output to have the same dimensions. it is important to note that this system processes each image channel (RGB) independently.

### System Architecture

The system starts with a bicubic interpolation layer that upsamples the input image from `(batch_size, 1, H, W)` to `(batch_size, 1, 2H, 2W)`. After this layer, the model includes three convolutional layers:

1. **Feature Extraction Layer**: 
   - Input size: `(batch_size, 1, 2H, 2W)`
   - Output size: `(batch_size, 64, 2H, 2W)`
   - This layer is followed by a ReLU activation function.

2. **Non-Linear Mapping Layer**: 
   - Input size: `(batch_size, 64, 2H, 2W)`
   - Output size: `(batch_size, 32, 2H, 2W)`

3. **Reconstruction Layer**: 
   - Input size: `(batch_size, 32, 2H, 2W)`
   - Output size: `(batch_size, 1, 2H, 2W)`

This architecture allows the model to upsample and enhance each color channel individually, resulting in a higher-resolution output for each input channel.

<p align="center">
  <img src="images/systems_architecture.jpg" alt="Image 1" width="80%" />
</p>
systems_architecture

## Training

During training, I fine-tuned the model’s parameters using transfer learning and added a data augmentation layer to improve generalization. The augmentations included random horizontal and vertical flips, as well as rotations up to 10 degrees. This helped the model adapt to various image orientations and details, enhancing its performance on unseen data. Training was conducted over 1,022 epochs, allowing the model to converge effectively while avoiding overfitting.

## Results

The final model achieved strong performance, with a Peak Signal-to-Noise Ratio (PSNR) of **32.42 dB** and a Structural Similarity Index Measure (SSIM) of **0.8134**. These metrics indicate that the model successfully enhanced image quality and preserved structural details, achieving results comparable to or better than standard bicubic interpolation in terms of both clarity and fidelity.


<p align="center">
  <img src="images/superes3.jpg" alt="Image 1" width="20%" />
  <img src="images/superes4.jpg" alt="Image 2" width="20%" />
  <img src="images/superes5.jpg" alt="Image 1" width="20%" />
  <img src="images/superes6.jpg" alt="Image 2" width="20%" />
</p>



