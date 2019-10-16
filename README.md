# MagnetScript
This is a pretty simple language or a python framework for people who want to keep things simple while also making scientific simulations and calculations.

For now there are very few methods/functions in this framework/language compared to many but, I am continuously developing it. For now it's a bit slow but I am trying to find a soulution so, if any one of you have any suggestion please help me.

# Basic functions and arguments
So in this section I will list a bunch of functions with their required and optional arguments

𝗳𝗼𝗿𝗹𝗼𝗼𝗽(), this will make your code run multiple times in a loop and and there are only two arguments and both are required first one being how many numbers of time should the code run and code should be a string variable or a function called inside of quotes if possible.

𝗲𝗰𝗵𝗼(), pretty much same as print.

𝗰𝗼𝗻𝗹𝗼𝗼𝗽(), this takes to arguments the first one being condition and the second one being code which should be better be a variable declared in quotes or function called inside of quotes in this function.

𝗱𝗼_𝗰𝗼𝗻𝗹𝗼𝗼𝗽(), similar to do-while loop in PHP and is very simple to execute only requiring two arguments the first one being code and the second one being condition.

# Where language/library/framework shines
This shines in it's easy ways to do certain tasks but it doesn't come at too big cost of flexibility because you can just execute python directly if you want to.

𝗺𝗮𝗴𝗻𝗲𝘁_𝘀𝗶𝗺(), this takes two required arguments first one being sources for example what your magnets are and what are there positions and power and the second one being manupulation where you can manipulate your magnets to rotate and move.

𝗵𝗲𝗮𝘁𝗺𝗮𝗽_𝗶𝗺𝗮𝗴𝗲(), this can give you the heatmap of an image by just a single required argument that being image and then there are many optional arguments and here's a list of these argumaents data(boolean) meaning is this image an already read array or just a plain image, cmap(string) default cmap is coolwarm, vmin, vmax, center(float) default is 0.5, robust and figsize(list of two integers that determines size of the figure).

𝘄𝗮𝘀𝗵𝘁𝗿𝗲𝗱_𝗶𝗺𝗮𝗴𝗲(), basically a washtred effect with one required and three optional arguments, required one is image which is quite self explanatory... Optional areguments are data(boolean) meaning that is it an array or just a good ole image, output(boolean) it means that do you want it to be an output image or an output array, figsize(list) should have two indexes and it determines height and width of the displayed image.

𝗯𝗹𝗮𝗰𝗸_𝘀𝗶𝗺(), it can generate simulations for blackholes it takes two parameters both are required but these parameters are basic characteristics of blackhole and you need to give those in order for this function to work.

𝗶𝗺𝗮𝗴𝗲_𝘀𝗵𝗼𝘄(), this basically takes your image and shows it with required argument image and optional argumets cmap, interpolation, alpha, vmin, vmax, filter_radius, figsize, title.

𝗼𝗿𝗯𝗶𝘁_𝗲𝗰𝗰𝗲𝗿_𝘀𝗶𝗺(), this function generates a body orbiting another one and it takes two required and two optional arguments(one more coming soon), the first required one is Sphere's properties and second required one is Mass. For optinal one's first one is what is ending lamda and second one is stepsize sorry, if this was a bit confusing but here I have a bit of sample code for you to understand this function better
```
M = 1.989e30 * units.kg  # mass of sun
distance = 147.09e6 * units.km
speed_at_perihelion = 30.29 * units.km / units.s
omega = (units.rad * speed_at_perihelion) / distance

sph_obj = SphericalDifferential(distance, np.pi / 2 * units.rad, np.pi * units.rad,
                               0 * units.km / units.s, 0 * units.rad / units.s, omega)

orbit_eccer_sim(sph_obj, M)
```
Running this with sciencere would give you earth's orbit and I hope this let's you under this easily, optional arguments are not used here but on source code defaults are

```
end_lambda=((1 * units.year).to(units.s)).value
stepsize=((5 * units.min).to(units.s)).value
```
Now, that I have attempted to try to explain this so, I hope I have explained this and that's it for this function.
# Additional simplifications
This is based on following libraries<br/>
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

# Sciencere
This is the command line tool to use with MagnetScript to speed up this simulation and calculation programs because it loads all libraries and functions from 'functions.py' but to speed it up you need to not add or remove line 'from functions import *' because doing otherwise would reload all functions and libraries. This tool is better then GUI interpreter because it won't stop running after execution of every simulation so, all you need to do to know how to use this tool is to type 'help()' in terminal inside this program to know all currently avalible command and remember that more are indeed coming soon.

# Upcoming plans
:heavy_check_mark:Speeding this up by ~~splitting functions.py in multiple files~~ making a CLI program.<br/>
Adding more functions and make further simplifications.<br/>
Make Galgebra easier.<br/>
Make use of asropy extensively.<br/>
Simple setup.py to install all libraries for use.
