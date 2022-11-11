# imgsorter

Image sorting based on keywords with python.

### Features:

- 🗝 creates a keyword frequency list from a directory of images
- 🗂 sorts images into folders based on keywords
- 🔮 use it to sort AI art that contains prompts in the file name!

### Use:

1. Run `imgsortr.py` in the directory where your folder of images is
2. Prompt will ask for the name of your images folder (or just press enter to use the
default name `images`)
3. Images are sorted! See the demo below:

https://user-images.githubusercontent.com/22015718/201282281-98d41876-3805-4a92-b26f-b4bd71de6d1a.mp4

**Note**: images are only copied, not deleted. 

### Detailed description:

*This is a python version of my imgsortr package for R.*
I’ve been enjoying using [Dall-E 2](https://openai.com/dall-e-2/) to
generate images, and so I wanted a way to quickly sort them into folders
based on keywords.

The requirement is that images contain keywords as text. E.g. 
`fox eating a mango in the matrix.png`. 

I have only used it for `.png` files. And file names I think have to be
separated by spaces but I haven't tested this. 

I use the DALL-E 2 Image Downloader extension in chrome to download the image
results of a prompt, and the file names inherit some of the prompt keywords.
Any files you download like this will be ready to sort. 

Beware 💀 this is my first time using python. Similar things already exist for sure, and
its probably a very inefficient script, but I'm looking for any feedback,
contributions, new features, etc! 

### Credits
The code to clean up text tokens is from KahEm Chu (2021) "Text Processing in Python", source: https://towardsdatascience.com/text-processing-in-python-29e86ea4114c
