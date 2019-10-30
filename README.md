# MagnetScript
This is a pretty simple language or a python framework for people who want to keep things simple while also making scientific simulations and calculations.

For now there are very few methods/functions in this framework/language compared to many but, I am continuously developing it. For now it's a bit slow but I am trying to find a soulution so, if any one of you have any suggestion please help me.

# Basic keywords and statements
So in this section I will list a bunch of keywords and statements in this language and more are coming soon

iterate, it's similar to for loop in ther languages and here it is followed by a new variable for loop's local scope, then followed by inside keyword and then followed by an actual already defined variable and for kicks here's a simple example
```
word="Hello World!"

iterate letter inside word:
  echo(letter)
```

𝗲𝗰𝗵𝗼(), pretty much same as print which basically prints out your statement on the console.

𝘀𝘁𝗿𝗿𝗲𝘃𝗲𝗿𝘀𝗲(), this function just takes a string and reverse it.

𝗿𝗲𝗾𝘂𝗶𝗿𝗲(), you can use it to import files in your program. It takes two arguments the first one being path to the file and the second ptional one being name. Here's a simple example
```
o=require("./o.pyclass")
o.userDefinedSum(11, 10)
```
𝗺𝗴𝘀_𝗿𝗲𝗾𝘂𝗶𝗿𝗲(), it takes a single argument that being path to a MagnetScript file(Important: You need to ```import functions``` in imported file) and it imports it and here's an example
```
o=mgs_require("./o.mags")
o.userDefinedSum(11, 10)
```

When, this is similar to while in other languages and is simply followed by a condition inside paranthesis then followed by ```:``` and then indexed similar to python and here's an example
```
x=0
word="Hello"

when(x<len(word)):
  echo(word[x])
  x+=1
```
unless, pretty similar to "if not" and should always be followed by a space to be recogonized correctly and here's an example
```
num=20

unless num>=20:
  echo(num, "is less than 20")
else:
  echo(num, "is greater than or equal to 20")
```

function, this is similat to function keyword in many languages and def in python and by using this, you can execute following example
```
function sum(num1, num2):
  num=num1+num2
  echo(num)

sum(9, 10)
```
## String formatting(Important)
This is by far the most distinct and important to read feature for this language is that certain words that are specifically reserved for this langugage should be covered with curly and then square brace such as ```{[unless]}``` and here are the list of keywords that should be wrapped in curly square brackets (More ight be added).
```
function
iterate
inside
when
unless
>|
```

# Where language/library/framework shines
This shines in it's easy ways to do certain tasks but it doesn't come at too big cost of flexibility because you can just execute python directly if you want to.

𝗺𝗮𝗴𝗻𝗲𝘁_𝘀𝗶𝗺(), this takes two required arguments first one being sources for example what your magnets are and what are there positions and power and the second one being manupulation where you can manipulate your magnets to rotate and move.

𝗵𝗲𝗮𝘁𝗺𝗮𝗽_𝗶𝗺𝗮𝗴𝗲(), this can give you the heatmap of an image by just a single required argument that being image and then there are many optional arguments and here's a list of these argumaents data(boolean) meaning is this image an already read array or just a plain image, cmap(string) default cmap is coolwarm, vmin, vmax, center(float) default is 0.5, robust and figsize(list of two integers that determines size of the figure).

𝘄𝗮𝘀𝗵𝘁𝗿𝗲𝗱_𝗶𝗺𝗮𝗴𝗲(), basically a washtred effect with one required and three optional arguments, required one is image which is quite self explanatory... Optional areguments are data(boolean) meaning that is it an array or just a good ole image, output(boolean) it means that do you want it to be an output image or an output array, figsize(list) should have two indexes and it determines height and width of the displayed image.

𝗯𝗹𝗮𝗰𝗸_𝘀𝗶𝗺(), it can generate simulations for blackholes it takes two parameters both are required but these parameters are basic characteristics of blackhole and you need to give those in order for this function to work.

𝗶𝗺𝗮𝗴𝗲_𝘀𝗵𝗼𝘄(), this basically takes your image and shows it with required argument image and optional argumets cmap, interpolation, alpha, vmin, vmax, filter_radius, figsize, title.

𝗼𝗿𝗯𝗶𝘁_𝗲𝗰𝗰𝗲𝗿_𝘀𝗶𝗺(), this function generates a body orbiting another one and it takes two required and three optional arguments, the first required one is Sphere's properties and second required one is Mass. For optinal one's first one is what is ending lamda, second one is stepsize and the last one is Object that I would explain in a bit sorry, if this was a bit confusing but here I have a bit of sample code for you to understand this function better
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
about that Object argument, honestly the best way to understand it to see the default code here but, I would summarize it a bit by saying you have to define some variables that being bodies with their poperties then link them through a property called 'parent' and then pass last variable(Object) in chain to the function using this argument and here's the default cde for you to easily understand

```
Sun = Body(name="Sun", mass=M, parent=None)
Object = Body(name="Earth", differential=sph_obj, parent=Sun)

#Pass Object in "orbit_eccer_sim()"
```

Now, that I have attempted to explain this so, I hope I have explained this well and that's it for this function.
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
