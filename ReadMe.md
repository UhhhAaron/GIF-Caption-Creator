<p align=center><a href=http://ifunny.co><img src=https://raw.githubusercontent.com/UhhhAaron/iFunny-Captions/master/Documents/Pictures/Main/gifcaptioncreator.png width=675></a></p>

<p align=center><a href=http://python.org/downloads/release/python-376><img src=https://img.shields.io/badge/Python-3.7.6-brightgreen?logo=python&logoColor=white&link=http://python.org/downloads/release/python-376&style=for-the-badge></a>

<p align=center><a href=http://github.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/releases/><img src=https://img.shields.io/github/v/release/Amirhan-Taipovjan-Greatest-I/iFunny-Captions?style=for-the-badge></a> <a href=http://github.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/blob/master/License.txt><img src=https://img.shields.io/github/license/Amirhan-Taipovjan-Greatest-I/iFunny-Captions?logo=readthedocs&color=red&logoColor=white&style=for-the-badge></a></p>


### iFunny-Captions is a pack of scripts providing widely customizable [GIF caption](http://knowyourmeme.com/memes/gif-captions) generation.

## Capabilities 
|  | iFunny App | `iFunny-Captions` |
|:-:|:-:|:-:|
| PNG Captions | ✔️ | ✔️ |
| GIF Captions | ✔️ | ✔️ |
| MP4 Captions | ✔️ | ✔️ |
| Image optimization | ❌ | ✔️ |
| Custom Fonts | ❌ | ✔️ |
| Emoji support | ✔️ | ✔️ |
| Crop support | ✔️ | ❌ |
| Graphical User Interface | ✔️ | ❌ <img src=https://raw.githubusercontent.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/master/Documents/Pictures/Main/Google_Colab.svg width=25> |
| Batch Processing | ❌ | ✔️ |
---
## Completed & Planned Features
- ✔️ PNG Captions
- ✔️ GIF Captions
- ✔️ Local file support
- ✔️ GIF size reduction
- ✔️ Custom fonts support
- ✔️ Transparent GIF support
- ❌ [Program Showcase](http://youtube.com/watch?v=r8KTluI9Q5Q) ([Broken Colab](http://youtube.com/watch?v=Uf-D2iEOvDU))
- ❌ Colab Notebook
- ✔️ Emoji support<sup>3</sup>
- ✔️ Automatic text wrap

<sup>1</sup> - Please look at [Custom Fonts](http://github.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/wiki/Custom-Fonts) section in wiki.<br>
<sup>2</sup> - Problems with wrap height might occur.

## Requirements
Programs:
- [`Python >= 3.7`](http://www.python.org/downloads) 

Modules:
- [`Pillow >= 5.1.0`](http://github.com/python-pillow/Pillow) - Making images 
- [`requests >= 2.13`](http://github.com/psf/requests) - URL fetching 
- [`emoji >= 0.4.5`](http://github.com/carpedm20/emoji) - Text to emoji support 
- [`clipboard >= 0.0.4`](http://github.com/terryyin/clipboard) - Clipboard values handling 
- [`sty >= 0.0.4`](https://github.com/feluxe/sty) - Colored prints 
- [`colour >= 0.1.5`](https://github.com/vaab/colour) - Colored text values handling 
- [`unidecode`](http://github.com/avian2/unidecode) - [Text normalization](http://wikipedia.org/wiki/Text_normalization#Techniques) 
- [`distro >= 1.7`](https://github.com/python-distro/distro)<sup>1</sup> - Directory opening helper 
- [`pyshortcuts >= 1.8`](https://github.com/newville/pyshortcuts) - Shortcuts making 

Packages (bold links are **Windows** static executable binaries):
- [**`FFmpeg >= 4.2.0`**](http://videohelp.com/software/ffmpeg/old-versions) - Since `PIL.ImageSequence.Iterator` messes up the frames colors.
- [**`Gifsicle >= 1.92-2`**](http://eternallybored.org/misc/gifsicle/releases) - **Check after 64-bit if possible!** ([`Scale_Back`](http://github.com/kubinka0505/iFunny-Captions/wiki/Known-Issues-%F0%9F%93%9D%F0%9F%90%9B#4-scale_back-option-doesnt-work) option)
- [**`PNGQuant >= 2.14`**](http://pngquant.org/#download) *(optional)*
- [**`OxiPNG >= 5.0.1`**](https://github.com/shssoichiro/oxipng/releases) *(optional)*
- [`Python3-PIP`](http://packages.debian.org/sid/python3-pip)</a><sup>1</sup>
- [`Python3-TK`](http://packages.debian.org/sid/python3-tk)</a><sup>1</sup>

<sup>1</sup> - Required on Linux

---
## Linux Installation & Usage
`sudo apt-get install git python3-apt python3-pip python3-tk ffmpeg pngquant gifsicle`

**For non-Debian distros, use the equivalent package manager to install these dependencies.**
1. Clone the repository and move to its directory.
	```bash
	git clone http://github.com/UhhhAaron/GIF-Caption-Creator
	cd iFunny-Captions
	```
2. Install required modules	by inputting `pip install -r requirements.txt`
3. Allocate [the required files](http://github.com/UhhhAaron/GIF-Caption-Creator#requirements-) to `PATH` system environment variable.
4. Modify the parameters in the `Config.json` file. [Its documentation can be found here](http://github.com/UhhhAaron/GIF-Caption-Creator/wiki/Configuration-Documentation).
5. Open shell script file named `Run`. Supports positional arguments - type `python iFunny_Captions.pyw -h` for more.
6. Output should be in the `Images` folder.

## Support
This project was tested on:
| OS | Python Version |
|:-:|:-:|
Windows 10 | 3.7.6 

[**If there are problems, create an issue here.**](http://github.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/issues/new/choose)

---
### Supported GIF services

Be sure to copy the **raw image URL**.
<table>
  <thead>
	<tr>
		<th>Tenor</th>
		<th>Giphy</th>
		<th>Gfycat</th>
		<th>Tumblr<br>(<code>GIFV</code>)</th>
		<th>ImgFlip</th>
		<th>GifImage</th>
		<th>BestAnimations</th>
		<th>GifFinder</th>
		<th>ReactionGIFs</th>
	</tr>
  </thead>
  <tbody>
	<tr align=center>
		<td><a href=http://tenor.com target="_blank"><img src=https://raw.githubusercontent.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Tenor.svg alt=Tenor width=65></a></td>
		<td><a href=http://giphy.com target="_blank"><img src=https://raw.githubusercontent.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Giphy.svg alt=Giphy width=65></a></td>
		<td><a href=http://gfycat.com target="_blank"><img src=https://raw.githubusercontent.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Gfycat.svg alt=Gfycat width=65></a></td>
		<td><a href=http://tumblr.com target="_blank"><img src=https://raw.githubusercontent.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/Tumblr.svg alt=Tumblr width=65></a></td>
		<td><a href=http://imgflip.com target="_blank"><img src=https://raw.githubusercontent.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/ImgFlip.svg alt=ImgFlip width=65></a></td>
		<td><a href=http://gifimage.net target="_blank"><img src=https://raw.githubusercontent.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/GifImage.png alt=GifImage width=65></a></td>
		<td><a href=http://bestanimations.com target="_blank"><img src=https://raw.githubusercontent.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/BestAnimations.png alt=BestAnimations width=65></a></td>
		<td><a href=http://gif-finder.com target="_blank"><img src=https://raw.githubusercontent.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/GifFinder.png alt=GifFinder width=65></a></td>
		<td><a href=http://reactiongifs.us target="_blank"><img src=https://raw.githubusercontent.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/master/Documents/Pictures/GIF_Image_Services_Logos/ReactionGIFs.svg alt=ReactionGIFs width=65></a></td>
	</tr>
  </tbody>
</table>

---
### Comparisons

- | iFunny Android App | `GIF-Caption-Creator` |
  |:-:|:-:|
  | <img src=https://raw.githubusercontent.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/master/Documents/Pictures/Comparison_Graphics/1/iFunny.gif width=150> | <img src=https://raw.githubusercontent.com/UhhhAaron/GIF-Caption-Creator/master/Documents/Pictures/Comparison_Graphics/1/iFunny-Captions.gif width=150> 
  | <img src=https://raw.githubusercontent.com/Amirhan-Taipovjan-Greatest-I/iFunny-Captions/master/Documents/Pictures/Comparison_Graphics/2/iFunny.gif width=150> | <img src=https://raw.githubusercontent.com/UhhhAaron/GIF-Caption-Creator/master/Documents/Pictures/Comparison_Graphics/2/iFunny-Captions.gif width=150> |
