# Video-Compression-Bitrate-Comparison-using-FFMPEG
This report is about a video processing project that compares the quality of different resolutions and bitrates for streaming. It uses python, FFMPEG, and PSNR to generate RD curves and evaluate the trade-off between quality and rate.

## Video Processing Project
This project investigates the trade-off between different strategies of transcoding DASH (H.264) representations for streaming. To do this, the same short video file is encoded at several different bitrates and various resolutions, and the quality is compared quantitatively (using PSNR) and qualitatively.

## Requirements
- Python 3
- FFMPEG
- FFMPEG Quality Metrics

## Usage
1. Clone this repository
2. Download the source video file
3. Run the python script `python video_processing.py`

## Methodology
The python script performs the following steps for each resolution and bitrate combination:
- Convert the raw YUV file to an MP4 file using lossy encoding, at a given constant bitrate. It uses the H.264 video compression standard and uses ffmpeg's "slow" preset.
- Convert the MP4 file back to a YUV file using lossless encoding.
- Upscale the resolution to 720p using ffmpeg. This is done so that each of the files can be evenly compared with the original 720p video file.
- Compare the compressed, encoded, up-scaled file with the original file using the FFMPEG Quality Metrics package. The package calculates the average SSIM and PSNR of each video and appends it to an array so it can be displayed in a graph later.

The following resolutions and bitrates were used to assess the video quality:
- **720p**
  - Suggested Bitrates for RD Curves (Kbps): 512, 1024, 2048
- **360p**
  - Suggested Bitrates for RD Curves (Kbps): 96, 128, 256, 284, 512, 1024, 2048
- **180p**
  - Suggested Bitrates for RD Curves (Kbps): 64, 96, 128, 256, 512, 1024

PSNR is calculated by computing the Mean Square Error (MSE) between the original frames and the compressed frames. The MSE is the sum of the squared differences between each pixel in the two frames, divided by the total number of pixels. The MSE is then used in the PSNR formula:

<div style=“text-align:center;”> <span style=“font-size:1.5em;”> PSNR = 10 log<sub>10</sub> <span style=“position:relative; top:-0.5em;”>(MAX<sup>2</sup> / MSE)</span> </span> </div>

where MAX is typically 255 for an 8-bit video.

### Comparison of quality of 360p (left) and 720p (right) at same bitrate 1024Kbps.

<p align="center">
</br>
<img src="1024kbps%20comparison.png" alt="1024Kbps Comparison" width = "80%" height="50%">
</p>
