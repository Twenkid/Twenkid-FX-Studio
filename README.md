# Twenkid-FX-Studio

Video Editing and Visual Effects 

by Todor Arnaudov - Tosh/Twenkid

2010-...

Unfortunately heavily underdeveloped and carrying some wrong design decisions since the beginning, abandoned many times for years.
However it may revive.

* GUI: pure Win32 with some custom light wrapper; "ugly" for general users
* Direct3D9 for rendering, experiments with OpenGL eventually for effects
* VFW (Video for Windows) for video sampling, opens only AVI files (require encoding .MTS, .mp4)
* A Python app for the effects in "Star Symphony" and other utils
* It worked with a limited set of WAV audio from the streams: mono? which were concatenated, and no audio preview.
* It had a custom D3D9 pixel shaders system for effects since an early version in 2011 (for "Дайте ми" music video) where the user can add new effects as scripts and they automatically generate sliders etc. However they were limited to a single-pass, one effect per clip. In 2016 there was a bit of work on introducing/redesigning the rendering for multipass effects, it worked to some exent and some experiments (a game project with S.), but it wasn't made to "production" version, there were some issues with always reading correctly the render targets after each effects and there was still not a universal multi-pass postprocessing effects.
* In 2017 there was an update, allowing to add a WAV audio track, any format, that is synchronically played with the video for preview with audio - for the "Cherry Jam" clip, Star Symphony in Chepelare etc.
* One advantage of the editor is that it was light on memory and it initially was developed on Windows XP 32-bit, then Windows 7. Current version is compiled on Windows 10 (not tested if working on WinXp or Wine, but it is possible to work)
* For saving on GUI coding, it didn't have the usual time-line view. Instead it had two tracks, one Main, where the videos are concatenated, and a Pool where the clips could be put anywhere and overlap. Blank clips can be added in the main track. Trimming of the clips is very fast on a slider when a video is selected, keys can be used also (, . for left-right side)
* There are some commands which can be entered in the editor as command line to turn on/off flags etc.
* In general the system needs huge refactoring, I consider either SDL, OpenCV, FFMPEG, or a combination, also Python, PyAV, Pyglet/Pygame etc. with tk as GUI: I don't know.



## Select videos produced with Twenkid FX Studio:

* The poetic fantasy music video suite "Star Symphony in Chepelare", 2018
http://twenkid.blogspot.com/2018/11/star-symphony-in-chepelare-poetic-video.html
* The funny cosplay music video "Contra in Hackafe", 2016
* The music video for the song "On the Cherry Tree" (На черешата) by "Cherry Jam", 2017
* The punk rock musical "Give it to me, or Love's no friend of mine", starring Todor and Anya, 2011 (introduction of static and animated color grading)
* The documentary "Аngel versus Terminator", 2011

...

![image](/Cpp/image/starsymphony.png)

![изображение](https://user-images.githubusercontent.com/23367640/132602856-bac97bf1-1b15-42ab-8671-c125bb574c7c.png)

![изображение](https://user-images.githubusercontent.com/23367640/132602940-9f6c4d43-01e8-4363-9295-f3ecbb7c3b1d.png)

![изображение](https://user-images.githubusercontent.com/23367640/132603130-1a89bcb4-1b8c-48d0-8eef-8ac45ee98f96.png)

