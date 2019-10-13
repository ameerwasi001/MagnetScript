# MagnetScript
This is a pretty simple language or a python framework for people who want to keep things simple while also making scientific simulations and calculations.

For now there are very few methods/functions in this framework/language compared to many but, I am continuously developing it. For now it's a bit slow but I am trying to find a soulution so, if any one of you have any suggestion please help me.

# Basic functions and arguments
So in this section I will list a bunch of functions with their required and optional arguments

forloop(), this will make your code run multiple times in a loop and and there are only two arguments and both are required first one being how many numbers of time should the code run and code should be a string variable or a function called inside of quotes if possible.

echo(), pretty much same as print.

conloop(), this takes to arguments the first one being condition and the second one being code which should be better be a variable declared in quotes or function called inside of quotes in this function.

do_conloop(), similar to do-while loop in PHP and is very simple to execute only requiring two arguments the first one being code and the second one being condition.

# Where language/library/framework shines
This shines in it's easy ways to do certain tasks but it doesn't come at too big cost of flexibility because you can just execute python directly if you want to.

magnet_sim(), this takes two required arguments first one being sources for example what your magnets are and what are there positions and power and the second one being m,anupulation where you can manipulate your magnets to rotate and move.

heatmap_image(), this can give you the heatmap of an image by just a single required argument that being image and then there are many optional arguments and here's a list of these argumaents data(boolean) meaning is this image an already read array or just a plain image,
cmap(string) default cmap is coolwarm, vmin, vmax, center(float) default is 0.5, robust and figsize(list of two integers that determines size of the figure).

washtred_image(), basically a washtred effect with one required and three optional arguments, required one is image which is quite self explanatory... Optional areguments are data(boolean) meaning that is it an array or just a good ole image, output(boolean) it means that do you want it to be an output image or an output array, figsize(list) should have two indexes and it determines height and width of the displayed image.

image_show(), this basically takes your image and shows it with required argument image and optional argumets cmap, interpolation, alpha, vmin, vmax, filter_radius, figsize, title.

# Additional simplifications
This is based on following libraries
numpy<br/>
scipy<br/>
magpylib<br/>
seaborn<br/>
astropy<br/>
EinsteinPy<br/>
galgebra<br/>
skimage<br/>
PySimpleGUI is required for running interpreter.py<br/>

and many functions can't be simplified for example in test.mags there's a really simple way to make basic Schwarzschild spacetime simulation which in my opinion cannot be further simplified but, you can contribute to this project and you might have a better idea.

# Upcoming plans
Speeding this up and splitting functions.py in multiple files<br/>
Adding more functions and mak further simplifications<br/>
Make Galgebra easier<br/>
Make use of asropy extensively<br/>
Simple setup.py to install all libraries for use
