from numpy import *
import numpy as np

from magpylib import source, Collection
from magpylib.source import *
import magpylib.source.magnet as magnet
import matplotlib.pyplot as plt
import magpylib as magpy

from scipy import ndimage as ndi
from sympy import *

import astropy.units as units
from astropy import constants

from einsteinpy.plotting import *
from einsteinpy.coordinates import *
from einsteinpy.bodies import *
from einsteinpy.geodesic import *
from einsteinpy.hypersurface import *
from einsteinpy.symbolic import *
from einsteinpy.metric import *
from einsteinpy.utils import *
from skimage.util import *

from galgebra.printer import *
from galgebra.ga import *
from galgebra.mv import *

import seaborn as sns
from skimage.morphology import watershed, disk
from skimage import data
from skimage.filters import *
from skimage.util import img_as_ubyte
from skimage.io import *
from skimage.color import *

import inspect
from importlib.machinery import SourceFileLoader
import tokens
import types
import sys

#for loop in MagnetScript
def forloop(num_of_times, code):
    frame = inspect.currentframe().f_back
    for x in range(0, num_of_times, 1):
        exec(str(code), frame.f_globals, frame.f_locals)


#'Print' or in this case 'echo' anything in MagnetScript
def echo(*values):
    print(*values)


def processed_input(str_to_show):
    content = input(str_to_show)
    content = tokens.tokenize(content)
    return content

#while loop in MagnetScript
def conloop(condition, code):
    frame = inspect.currentframe().f_back
    while eval(str(condition), frame.f_globals, frame.f_locals):
        exec(str(code), frame.f_globals, frame.f_locals)



#do-while loop in MagnetScript
def do_conloop(code, condition):
    frame = inspect.currentframe().f_back
    while True:
        exec(str(code), frame.f_globals, frame.f_locals)
        if not eval(str(condition), frame.f_globals, frame.f_locals):
           break

#Reverse a string
def str_slice(string, slicevalues=[None,None,-1]):
    if(len(slicevalues) > 3):
        raise ValueError('There can only be three slice values in slice values but {} are given in {}'.format(len(slicevalues), slicevalues))
    else:
        return string[slicevalues[0]:slicevalues[1]:slicevalues[2]]

relpath = lambda path: os.path.dirname(os.path.realpath(os.path.abspath(path)))

#importing a python file in MagnetScript
def require(file, name="imported"):
    loader = SourceFileLoader(name,file)
    loaded = loader.load_module()
    return loaded

#importing a MagnetScript file in MagnetScript
def mgs_require(module_name):
    file = open(module_name, "r+")
    lines = file.readlines()
    linenum = 0
    lines.insert(0, "from functions import * \n")
    while(linenum<len(lines)):
        lines[linenum] = tokens.tokenize(lines[linenum], directory=relpath(module_name))
        linenum+=1
    source = '\n'.join(lines)
    module = types.ModuleType(module_name)
    exec(source, module.__dict__)
    sys.modules[module_name] = module
    return module

#magnetic simulation with MagnetScript
def magnet_sim(sources, manipulation):
    frame = inspect.currentframe().f_back
    
    #manipulation of Magnets
    exec(str(manipulation), frame.f_globals, frame.f_locals)

    #create collection
    magnets_collection = magpy.Collection(*sources)

    #display system geometry
    fig1 = magnets_collection.displaySystem(suppress=True)
    fig1.set_size_inches(6, 6)

    #calculate B-field on a grid
    axis = {'x': linspace(-10,10,30),
            'y': linspace(-10,10,30)
           }
    Bfield = np.array([[magnets_collection.getB([x,0,y]) for x in axis['x']] for y in axis['y']])

    #display field in xz-plane using matplotlib
    fig2, ax = plt.subplots()
    X,Z = np.meshgrid(axis['x'],axis['y'])
    U,V = Bfield[:,:,0], Bfield[:,:,2]
    ax.streamplot(X, Z, U, V, color=np.log(U**2+V**2), density=2)

    #show plots
    plt.show()


#Heatmap for images using MagnetScript
def heatmap_image(image, data=False, cmap='coolwarm', vmin=None, vmax=None, center=0.5, robust=True, figsize=[6,4]):
    #Checking the image
    if not data:
        image = imread(image, as_gray=True)
    else:
        if len(image.shape) is 3:
            image = rgb2grey(image)

    # display results
    sns.set(rc={'figure.figsize':(figsize[0], figsize[1])})
    if vmin == None and vmax == None:
        ax = sns.heatmap(image, cmap=cmap, robust=robust, center=center,cbar=False, yticklabels=False, xticklabels=False)
    else:
        ax = sns.heatmap(image, cmap=cmap, robust=robust, center=center, vmin=vmin, vmax=vmax, cbar=False, yticklabels=False, xticklabels=False)

    ax.imshow(image, cmap=plt.cm.jet)
    ax.set_title("Heatmap")
    plt.show()



#Contrast a image with MagnetScript (Parameters aren't yet configured well)
def washtred_image(image, data=False, output=True, cmap='nipy_spectral', figsize=[6,4]):

    if not data:
        image = imread(image, as_gray=True)
    else:
        if len(image.shape) is 3:
            image = rgb2grey(image)

    # denoise image
    denoised = rank.median(image, disk(2))

    # find continuous region (low gradient -
    # where less than 10 for this image) --> markers
    # disk(5) is used here to get a more smooth image
    markers = rank.gradient(denoised, disk(5)) < 10
    markers = ndi.label(markers)[0]

    # local gradient (disk(2) is used to keep edges thin)
    gradient = rank.gradient(denoised, disk(2))

    # process the watershed
    labels = watershed(gradient, markers)

    if output:
        # display results
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(figsize[0], figsize[1]), sharex=True, sharey=True, squeeze=False)
        ax = axes.ravel()

        ax[0].imshow(gradient, plt.cm.get_cmap(cmap), interpolation='nearest')
        ax[0].set_title("Local Gradient")


        for a in ax:
            a.axis('off')

        fig.tight_layout()
        plt.show()
    else:
        return gradient


#Show image with MagnetScript
def image_show(image, cmap='viridis', interpolation='nearest', alpha=1, vmin=None, vmax=None, filter_radius=4.0, figsize=[6,4], title='Image'):
    # display results
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(figsize[0], figsize[1]), sharex=True, sharey=True, squeeze=False)
    ax = axes.ravel()
    if vmin==None and vmax==None:
        ax[0].imshow(image, plt.cm.get_cmap(cmap), alpha=alpha, interpolation=interpolation, filterrad=filter_radius)
    else:
        ax[0].imshow(image, plt.cm.get_cmap(cmap), alpha=alpha, interpolation=interpolation, filterrad=filterrad, vmin=vmin, vmax=vmax)
    ax[0].set_title(title)


    for a in ax:
        a.axis('off')

    fig.tight_layout()
    plt.show()


#black hole simulation with ergosphere and horizon in MagnetScript
def black_sim(M, a):
    ergo, hori = list(), list()
    thetas = np.linspace(0, np.pi, 720)
    for t in thetas:
        ergo.append(kerr_utils.radius_ergosphere(M, a, t, "Spherical"))
        hori.append(kerr_utils.event_horizon(M, a, t, "Spherical"))
    ergo, hori = np.array(ergo), np.array(hori)


    Xe2, Ye2 = ergo[:,0] * np.sin(ergo[:,1]), ergo[:,0] * np.cos(ergo[:,1])
    Xh2, Yh2 = hori[:,0] * np.sin(hori[:,1]), hori[:,0] * np.cos(hori[:,1])

    # for displaying ordinary blackhole
    fig, ax = plt.subplots()
    ax.fill(Xh2, Yh2, 'b', Xe2, Ye2, 'r', alpha=0.3)
    ax.fill(-1*Xh2, Yh2, 'b', -1*Xe2, Ye2, 'r', alpha=0.3)

    plt.show()


#Frame-dragging effect in Kerr space-time
def frame_drag(BL_obj, M, scatter_val=[0,0], dot_color='black', size=0.2,
               end_lambda=((1 * units.year).to(units.s)).value/930, stepsize=((0.02 * units.min).to(units.s)).value):
    obj = Kerr.from_coords(BL_obj, M)
    ans = obj.calculate_trajectory(
        end_lambda=end_lambda, OdeMethodKwargs={"stepsize": stepsize}, return_cartesian=True
    )
    x, y = ans[1][:,1], ans[1][:,2]

    plt.scatter(x,y, s=size)
    plt.scatter(scatter_val[0],scatter_val[1], c='{}'.format(dot_color))
    plt.show()

#Calculating an orbit's eccentricity and apehelion and making a simulation
def orbit_eccer_sim(sph_obj, M, end_lambda=((1 * units.year).to(units.s)).value, stepsize=((5 * units.min).to(units.s)).value, Object=None):
    obj = Schwarzschild.from_coords(sph_obj, M)
    ans = obj.calculate_trajectory(
        end_lambda=end_lambda, OdeMethodKwargs={"stepsize": stepsize}, return_cartesian=True
    )

    ans[0].shape, ans[1].shape

    r = np.sqrt(np.square(ans[1][:, 1]) + np.square(ans[1][:, 2]))
    i = np.argmax(r)
    (r[i] * units.m).to(units.km)

    ((ans[1][i][6]) * units.m / units.s).to(units.km / units.s)

    xlist, ylist = ans[1][:, 1], ans[1][:, 2]
    i = np.argmax(ylist)
    x, y = xlist[i], ylist[i]
    eccentricity = x / (np.sqrt(x ** 2 + y ** 2))
    eccentricity

    if Object == None:
        Sun = Body(name="Sun", mass=M, parent=None)
        Object = Body(name="Earth", differential=sph_obj, parent=Sun)
        
    geodesic = Geodesic(body=Object, time=0 * units.s, end_lambda=end_lambda, step_size=stepsize)

    sgp = GeodesicPlotter()
    sgp.plot(geodesic)
    sgp.show()
