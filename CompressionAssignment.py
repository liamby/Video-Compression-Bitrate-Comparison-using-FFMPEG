# Motion Picture Engineering 
# Assignment 2 Compression 
# Liam Byrne, Student I.D. 18326579

# Imports
import subprocess
import matplotlib.pyplot as plt
from ffmpeg_quality_metrics import FfmpegQualityMetrics

# Declare constants
bit1280 = [512, 1024, 2048, 3072]
bit640 = [96, 128, 256,384, 612, 1024, 2048]
bit320 = [64, 96, 128, 256, 512, 1024]

bitratesArr = [bit320, bit640, bit1280]
resolutionNames = ["320x138","640x274","1280x548"]

# convert To MP4 Lossless
subprocess.run(f'''ffmpeg -s 1280x548 -i Source\\dancing1280x548.yuv Source\\compressed_lossless.mp4''',shell = True)

for resolution, bitrates in zip(resolutionNames, bitratesArr):
    psnrs = []
    
    for rate in bitrates:
        
        # Convert To MP4 Lossy
        subprocess.run(f'''ffmpeg -s {resolution} -i Source\\dancing{resolution}.yuv -b:v {rate}k -c:v libx264 -preset slow Output\\{resolution}_{rate}.mp4''',shell = True)
        # Convert MP4 To YUV Lossless
        subprocess.run(f'''ffmpeg -i Output\\{resolution}_{rate}.mp4 -c:v libx264 Output\\{resolution}_{rate}.yuv''',shell=True)
        # upscale(resolution, "1280x548", rate)
        subprocess.run(f'''ffmpeg -i Output\\{resolution}_{rate}.yuv -vf scale=1280x548:flags=lanczos -c:v libx264 -preset slow -crf 21 Output\\upscaled_{resolution}_{rate}.yuv''',shell=True)
        
        # Calculate PSNRs
        qualityMetrics = FfmpegQualityMetrics(f"Output\\upscaled_{resolution}_{rate}.yuv ", "Source\\compressed_lossless.mp4")
        metrics = qualityMetrics.calculate(["psnr", "ssim"])
        psnr = qualityMetrics.get_global_stats()["psnr"]["psnr_avg"]["average"]
        psnrs.append(psnr)
    
    # Plot PSNRs
    plt.plot(bitrates, psnrs, label = resolution, marker = 'o')

# Estimates for crossover bitrates
plt.plot([100], [30], label = "720p intersect 360p", marker = 'o')
plt.plot([950], [40], label = "360p interects 180p", marker = 'o')

# Show Graph
plt.title('Bitrate vs PSNR')
plt.legend()
plt.xlabel('Bitrate (Kbps)')
plt.ylabel('PSNR (dB)')
plt.show()

