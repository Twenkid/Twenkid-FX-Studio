# Twenkid-FX-Studio

![image](/Releases/TwenkidFX-Alpha-10-2021-Win32/fx.png)

![image](https://user-images.githubusercontent.com/23367640/164568741-bfa84531-4360-4e8d-b781-22d4e90d4c2b.png)

## Video Editing and Visual Effects 

&copy; Todor Arnaudov - Tosh/Twenkid

## Freeware

First Release! ... 29.12.2021

## Twenkid FX Studio Alpha 0.1
* **Binaries (portable): 300 KB**: 
 
http://twenkid.com/fx/TwenkidFXStudioAlpha-12-2021.zip

https://twenkid.com/fx/get.html

* **Manual:** 2 MB: 
https://twenkid.com/fx/TwFXStudio-24-12-2021.pdf


**System requirements:** Windows 7 x86, possibly Windows XP, but not tested. In the past I've tried on Windows with Wine and it run, but I didn't have codecs installed. It may run with a proper Wine, because it's based on pure classic Win32 libraries and the well established Direct3D9 and VFW. May require some VS redistributables - last compiled with VS2017.

Additional mixing with an external audio track, prepared separately (the output file could be also .avi etc.) for publishing on youtube etc.:

```
ffmpeg -i "C:\video.avi" -i C:\audio.mp3 -c:v copy -c:a copy -map 0:v:0 -map 1:a:0 C:\video_with_audio.mp4
```

* **Video Tutorials and Presentation** 
 
 https://www.youtube.com/watch?v=eUtk5Xxb89A
 
* Free Video Editor and Visual Effects Software Introduction - Twenkid FX Studio Alpha - Part 1
Nov 9, 2021

Free NLE Video Editor and Visual Effects project and prototype. Part 1 of many. This software had to be first published back in 2010 as it had a working functional prototype and cool video demos, but it remained as an in-house tool and wasn't developed as much it was supposed to. Now it may revive.

In Bulgarian:

* https://www.youtube.com/watch?v=pWQKyJsv7Ss

Безплатна програма за видеообработка и ефекти - българският видео редактор Twenkid FX Studio Alpha
Dec 30, 2021

Най-общо представяне на програмата Twenkid FX Studio Alpha 0.1 - издание от декември 2021 г. Следват продължения с подробно ръководство за употреба, уроци и пр.  Засега: инфо, ръководство (на английски) и изтегляне на програмата: http://twenkid.com/fx


* Урок 1: Видеообработка с Twenkid FX Studio Alpha 0.1 - Инсталиране, Конфигуриране, Рязане, Експорт
Premiered Dec 31, 2021

![image](https://user-images.githubusercontent.com/23367640/164568958-18bdfc4e-2d5e-482a-88b4-1c9a4f4556fa.png)


https://www.youtube.com/watch?v=Vavrzjq_Abw

Изтеглете програмата от http://twenkid.com/fx
Безплатното българско приложение за видео монтаж и визуални ефекти (прототип): Twenkid FX Studio. Вижте по-общо представяне в предишни клипове и по-стари демота. В тази поредица от уроци ("туториали", tutorials) ще покажа как се работи с програмата: инсталиране, конфигуриране/конфигурация, рязане/Cut/Trimming, експортиране: Export, Rendering ("рендериране"), запис на видеото.


## About

2010-...

Unfortunately heavily underdeveloped and carrying some wrong design decisions since the beginning, abandoned many times for years.
However it may revive. The first alpha release had to be in 2010, in 2011 there were shader effects and "color grading" with possible animations.

http://twenkid.com/fx  (currently redirects here)

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
* Additional Python program for preview and cut of parts of clip (no sound) and for all visual effects in "Star Symphony in Chepelare"


## Select videos produced with Twenkid FX Studio:

* The poetic fantasy music video suite "Star Symphony in Chepelare", 2018
http://twenkid.blogspot.com/2018/11/star-symphony-in-chepelare-poetic-video.html
* The funny cosplay music video "Contra in Hackafe", 2016
* The music video for the song "On the Cherry Tree" (На черешата) by "Cherry Jam", 2017
* The punk rock musical "Give it to me, or Love's no friend of mine", starring Todor and Anya, 2011 (introduction of static and animated color grading)
* The documentary "Аngel versus Terminator", 2011


## Media demos

* TwenkidFX-Studio-16-10-2010-Split-Screen-Title.mp4
* ...

...

![image](/Cpp/image/starsymphony.png)

![изображение](https://user-images.githubusercontent.com/23367640/132602856-bac97bf1-1b15-42ab-8671-c125bb574c7c.png)

![изображение](https://user-images.githubusercontent.com/23367640/132602940-9f6c4d43-01e8-4363-9295-f3ecbb7c3b1d.png)

![изображение](https://user-images.githubusercontent.com/23367640/132603130-1a89bcb4-1b8c-48d0-8eef-8ac45ee98f96.png)

