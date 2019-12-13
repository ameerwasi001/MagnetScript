import numpy as np

from magpylib import source, Collection
from magpylib.source import *
import magpylib.source.magnet as magnet
import matplotlib.pyplot as plt
from matplotlib.colors import *
import magpylib as magpy

import scipy as sc
from scipy.ndimage import *
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
from skimage.morphology import *
from skimage import data
from skimage.filters import *
from skimage.util import *
from skimage.io import *
from skimage.color import *
from skimage.segmentation import *
from skimage.transform import *
from skimage.feature import *

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

def relpath(path):
    path = os.path.dirname(os.path.realpath(os.path.abspath(path)))
    path = path.replace('\\', '/')
    return path

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
    axis = {'x': np.linspace(-10,10,30),
            'y': np.linspace(-10,10,30)
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
def heatmap_image(image, data=False, cmap='coolwarm', title='Heatmap', vmin=None, vmax=None, center=0.5, robust=True, figsize=[6,4], cbar=False, ticklabels=[[], []],
fontsize=[10,10], rotation=[0,0], va=['bottom', 'bottom'], ha=['left', 'left'], pad=[10, 10], which=['major', 'major'], axis='off', show=True, xlabel='', ylabel='',
context='paper', style=None, usePlot='default', rc=[{}, {}], font_scale=1, alpha=1, interpolation='nearest', filter_radius=4.0, output=True, disk_entropy=5):
    #Checking the image
    if not data:
        image = imread(image, as_gray=True)
    else:
        if len(image.shape) is 3:
            image = rgb2grey(image)

    if output:
        if style is not None:
            sns.set_style(style, rc=rc[0])

        #set context
        sns.set_context(context, font_scale=font_scale, rc=rc[0])

        # display results
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(figsize[0], figsize[1]), sharex=True, sharey=True, squeeze=False)
        ax = axes.ravel()
        
        if vmin==None and vmax==None:
            ax[0].imshow(rank.entropy(image, disk(disk_entropy)), plt.cm.get_cmap(cmap), alpha=alpha, interpolation=interpolation, filterrad=filter_radius)
        else:
            ax[0].imshow(rank.entropy(image, disk(disk_entropy)), plt.cm.get_cmap(cmap), alpha=alpha, interpolation=interpolation, filterrad=filterrad, vmin=vmin, vmax=vmax)

        ax[0].imshow(image, cmap=plt.cm.get_cmap(cmap))
        ax[0].set_title(title)
        ax[0].set_xticklabels(ticklabels[0], rotation = rotation[0], fontsize = fontsize[0], va=va[0], ha=ha[0])
        ax[0].set_yticklabels(ticklabels[1], rotation = rotation[1], fontsize = fontsize[1], va=va[1], ha=ha[1])
        plt.tick_params(axis='x', which=which[0], pad=pad[0])
        plt.tick_params(axis='y', which=which[1], pad=pad[1])
        plt.axis(axis)
        ax[0].set_xlabel(xlabel)
        ax[0].set_ylabel(ylabel)

        #set usePlot
        plt.style.use(usePlot)
        if show:
            plt.show()
    else:
        return rank.entropy(image, disk(disk_entropy))

def bright_scale(image, data=False, outer_circle=False, grayscale=True, dotted_lines=True, figsize=[6,4], cmap='gray', output=True):
    if not data:
        image = imread(image)

    if grayscale:
        image[:10] = 0
        mask = image < 87
        image[mask] = 255
    if dotted_lines:
        inds_x = np.arange(len(image))
        inds_y = (4 * inds_x) % len(image)
        image[inds_x, inds_y] = 0

    if outer_circle:
        l_x, l_y = image.shape[0], image.shape[1]
        X, Y = np.ogrid[:l_x, :l_y]
        outer_disk_mask = (X - l_x / 2)**2 + (Y - l_y / 2)**2 > (l_x / 2)**2
        image[outer_disk_mask] = 0

    if output:
        plt.figure(figsize=(figsize[0], figsize[1]))
        plt.imshow(image, cmap=cmap)
        plt.axis('off')
        plt.show()
    else:
        return image

#Compact segmentation of an image with MagnetScript
def compact_segmentation_image(image, data=False, outvar='segments_watershed', title='Compact watershed',
figsize=[6,4], output=True, scale=100, sigma=0.5, min_size=50, n_segments=250, compactness=10, kernal_siz=3, max_dist=6, ratio=0.5, markers=250, gray=True,
supress=False, show=True):
    if not data:
        image = imread(image, as_gray=gray)
    else:
        if ((len(image.shape) is 3) and gray):
            image = rgb2grey(image)


    image = img_as_float(image[::2, ::2])

    segments_fz = felzenszwalb(image, scale=scale, sigma=sigma, min_size=min_size)
    segments_slic = slic(image, n_segments=n_segments, compactness=compactness, sigma=sigma)
    try:
        segments_quick = quickshift(image, kernel_size=kernal_siz, max_dist=max_dist, ratio=ratio)
    except:
        if not supress:
            print("Quick segments not declared")
    gradient = sobel(rgb2gray(image))
    segments_watershed = watershed(gradient, markers=markers, compactness=compactness)

    evaluated = eval('outvar')

    if output:
        fig, axes = plt.subplots(1, figsize=(figsize[0], figsize[1]), sharex=True, sharey=True, squeeze=False)
        ax = axes.ravel()

        ax[0].imshow(mark_boundaries(image, eval(evaluated)))
        ax[0].set_title(title)

        for a in ax.ravel():
            a.set_axis_off()

        plt.tight_layout()
        if show:
            plt.show()
    else:
        return eval(evaluated)

        
#Contrast an image with MagnetScript
def watershed_image(image, data=False, output=True, interpolation="nearest", cmap='nipy_spectral', title="Local Gradient", outvar='gradient', figsize=[6,4],
disk_denonised = 2, disk_markers = 5, disk_gradient = 2):

    if not data:
        image = imread(image, as_gray=True)
    else:
        if len(image.shape) is 3:
            image = rgb2grey(image)

    # denoise image
    denoised = rank.median(image, disk(disk_denonised))

    # find continuous region (low gradient -
    # where less than 10 for this image) --> markers
    # disk(5) is used here to get a more smooth image
    markers = rank.gradient(denoised, disk(disk_markers)) < 10
    markers = label(markers)[0]

    # local gradient (disk(2) is used to keep edges thin)
    gradient = rank.gradient(denoised, disk(disk_gradient))

    # process the watershed
    labels = watershed(gradient, markers)

    evluated = eval('outvar')

    if output:
        # display results
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(figsize[0], figsize[1]), sharex=True, sharey=True, squeeze=False)
        ax = axes.ravel()
        ax[0].imshow(eval(evluated), plt.cm.get_cmap(cmap), interpolation=interpolation)
        ax[0].set_title(title)


        for a in ax:
            a.axis('off')

        fig.tight_layout()
        plt.show()
    else:
        return eval(evluated)


#Show image with MagnetScript
def image_show(image, data=True, gray=False, cmap='viridis', interpolation='nearest', alpha=1, vmin=None, vmax=None, filter_radius=4.0, figsize=[6,4], title='Image',
axis='off', ticklabels=[[], []], fontsize=[10,10], rotation=[0,0], va=['bottom', 'bottom'], ha=['left', 'left'], pad=[10, 10], which=['major', 'major'], show=True,
xlabel='', ylabel='', context='paper', style=None, usePlot='default', rc=[{}, {}], font_scale=1):
    if not data:
        image = imread(image, as_gray=gray)
    else:
        if ((len(image.shape) is 3) and gray):
            image = rgb2grey(image)
    #set style
    if style is not None:
        sns.set_style(style, rc=rc[0])

    #set context
    sns.set_context(context, font_scale=font_scale, rc=rc[1])
    
    # display results
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(figsize[0], figsize[1]), sharex=True, sharey=True, squeeze=False)
    ax = axes.ravel()
    if vmin==None and vmax==None:
        ax[0].imshow(image, plt.cm.get_cmap(cmap), alpha=alpha, interpolation=interpolation, filterrad=filter_radius)
    else:
        ax[0].imshow(image, plt.cm.get_cmap(cmap), alpha=alpha, interpolation=interpolation, filterrad=filterrad, vmin=vmin, vmax=vmax)
    ax[0].set_title(title)
    ax[0].set_xticklabels(ticklabels[0], rotation = rotation[0], fontsize = fontsize[0], va=va[0], ha=ha[0])
    ax[0].set_yticklabels(ticklabels[1], rotation = rotation[1], fontsize = fontsize[1], va=va[1], ha=ha[1])
    plt.tick_params(axis='x', which=which[0], pad=pad[0])
    plt.tick_params(axis='y', which=which[1], pad=pad[1])

    for a in ax:
        a.axis(axis)
        a.set_xlabel(xlabel)
        a.set_ylabel(ylabel)

    fig.tight_layout()
    #set usePlot
    plt.style.use(usePlot)
        
    if show:
        plt.show()


#black hole simulation with ergosphere and horizon in MagnetScript
def black_sim(M, a, title='', linspace=[0, np.pi, 720], xlabel='', ylabel='', figsize=[6,4], alpha=0.3, ticklabels=[[], []], fontsize=[10,10], rotation=[0,0],
va=['top', 'top'], ha=['right', 'right'], axis='on', show=True):
    ergo, hori = list(), list()
    thetas = np.linspace(linspace[0], linspace[1], linspace[2])
    for t in thetas:
        ergo.append(kerr_utils.radius_ergosphere(M, a, t, "Spherical"))
        hori.append(kerr_utils.event_horizon(M, a, t, "Spherical"))
    ergo, hori = np.array(ergo), np.array(hori)


    Xe2, Ye2 = ergo[:,0] * np.sin(ergo[:,1]), ergo[:,0] * np.cos(ergo[:,1])
    Xh2, Yh2 = hori[:,0] * np.sin(hori[:,1]), hori[:,0] * np.cos(hori[:,1])

    # for displaying ordinary blackhole
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(figsize[0], figsize[1]), squeeze=False)
    ax = axes.ravel()
    ax[0].fill(Xh2, Yh2, 'b', Xe2, Ye2, 'r', alpha=alpha)
    ax[0].fill(-1*Xh2, Yh2, 'b', -1*Xe2, Ye2, 'r', alpha=alpha)
    ax[0].set_title(title)
    if ticklabels != [[], []]:
        ax[0].set_xticklabels(ticklabels[0], rotation = rotation[0], fontsize = fontsize[0], va=va[0], ha=ha[0])
        ax[0].set_yticklabels(ticklabels[1], rotation = rotation[1], fontsize = fontsize[1], va=va[1], ha=ha[1])
    ax[0].set_xlabel(xlabel)
    ax[0].set_ylabel(ylabel)
    ax[0].axis(axis)

    if show:
        plt.show()


#Frame-dragging effect in Kerr space-time
def frame_drag(BL_obj, M, scatter_val=[0,0], dot_color='black', size=0.2, end_lambda=((1 * units.year).to(units.s)).value/930,
OdeMethodKwargs = {"stepsize": ((0.02 * units.min).to(units.s)).value}, title='', xlabel='', ylabel='', figsize=[6,4], ticklabels=[[], []], fontsize=[10,10],
rotation=[0,0], va=['top', 'top'], ha=['right', 'right'], axis='on', show=True):
    obj = Kerr.from_coords(BL_obj, M)
    ans = obj.calculate_trajectory(
        end_lambda=end_lambda, OdeMethodKwargs = OdeMethodKwargs, return_cartesian=True
    )
    x, y = ans[1][:,1], ans[1][:,2]

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(figsize[0], figsize[1]), squeeze=False)
    ax = axes.ravel()
    ax[0].scatter(x,y, s=size)
    ax[0].scatter(scatter_val[0],scatter_val[1], c='{}'.format(dot_color))
    ax[0].set_title(title)
    if ticklabels != [[], []]:
        ax[0].set_xticklabels(ticklabels[0], rotation = rotation[0], fontsize = fontsize[0], va=va[0], ha=ha[0])
        ax[0].set_yticklabels(ticklabels[1], rotation = rotation[1], fontsize = fontsize[1], va=va[1], ha=ha[1])
    ax[0].set_xlabel(xlabel)
    ax[0].set_ylabel(ylabel)
    ax[0].axis(axis)

    if show:
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
