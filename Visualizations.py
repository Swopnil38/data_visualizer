from cProfile import label
import random
import matplotlib.pyplot as plt

import matplotlib.image as mpimg
import numpy as np

from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
from requests import request

from matplotlib.animation import FuncAnimation,PillowWriter

from Value_Processing import read_yt_csv

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)



def horizontal_bar(Labels,value_male,value_female,channel_name):
    image_name = f'static/images/{channel_name}_AgeGender.png'
    def get_flag(gender,name):
        path = 'imgs/{}/{}.png'.format(gender,name)
        
        im = plt.imread(path)
        return im

    def offset_image(x,y, name, gender):
        img = get_flag(gender,name)
        
        im = OffsetImage(img, zoom=0.25)
        
        
        im.image.axes = ax

        ab = AnnotationBbox(im, (x, y),  xybox=(-5., -30.), frameon=False,
                            xycoords='data',  boxcoords="offset points", pad=0)

        ax.add_artist(ab)
        

    
    fig, ax = plt.subplots(figsize=(12,6))
    length_male = len(Labels)
    colors_male = get_cmap(length_male)
    heights = 0.4
    x = np.arange(len(Labels))
    widths = 0.4
    
    horizontal_female = ax.barh(x+widths,value_female,widths,zorder = 0.8)
    horizontal_male = ax.barh(x,value_male,widths,zorder = 0.8)
    
    y_bar_female = [rectangle.get_y()+0.8 for rectangle in horizontal_female]
    y_bar_male = [rectangle.get_y()+0.8 for rectangle in horizontal_male]
    gender_male = "male"
    gender_female = "female"
    plt.yticks(x + widths, Labels, rotation = 20)
    for x,y,val in zip(Labels,value_female,y_bar_female):
        if y>1:
            offset_image(y,val,x,gender_female)
    for x,y,val in zip(Labels,value_male,y_bar_male):
        if y>1:
            offset_image(y,val,x,gender_male)
    
    plt.savefig(image_name, dpi=100)

    return fig
 
def pie(labels,value,channel_name):
    fig, ax = plt.subplots()
    image_name = f'static/images/{channel_name}_Geography.png'
    explode = [0,0,0,1]
    plt.pie(value, labels=labels,autopct='%1.1f%%', shadow=True, startangle=150) 
    plt.axis('auto')
    plt.savefig(image_name, dpi=100)

    return fig
    
def animatedline_chart(label,value,channel_name):

    image_name = f'static/images/{channel_name}_view.gif'
    # create empty lists for the x and y data
    x = []
    y = []

    # create the figure and axes objects
    fig, ax = plt.subplots(figsize=(12,6))
    # function that draws each frame of the animation

    def animate(i):
        if i < len(label):
            x.append(label[i])
            y.append(value[i])
        
        ax.clear()
        ax.plot(x, y,color = "darkgreen",linewidth = 2)
        ax.set_xlim([label[0],label[len(label)-1]])
        if max(value)>100000:
            ax.set_ylim([0,max(value)+10000])
        elif max(value)>10000:
            ax.set_ylim([0,max(value)+1000])
        elif max(value)>100:
            ax.set_ylim([0,max(value)+100])
        else:
            ax.set_ylim([0,max(value)+10])
        axe = plt.gca()
        axe.tick_params(axis='x', labelrotation = 45)

        plt.fill_between(
            x= x, 
            y1= y,
            color= "springgreen",
            alpha= 0.4)
        
        ax.grid(color='#CCCCCC', linestyle='--')
        
    plt.set_loglevel('WARNING')

    ani = FuncAnimation(fig, animate, frames=len(label), interval=900, repeat=False)
    ani.save(image_name, dpi=105, writer=PillowWriter(fps=1))
    return image_name


    
label = ['Python', 'C++', 'Ruby', 'Java']
value = [215, 130, 245, 210]
#pie(label,value)
 
    
value_male = [1,2,5,7,9]
labels = ["18-24","25-34","35-44","45-54","55+"]
value_female = [1,2,5,7,9]

#horizontal_bar(labels,value_male,value_female,"The Doers")


#ages_yt,male_viewer_yt,female_viewer_yt,country_name,country_viewer_per,country_lat,country_lon,viewes,avg_duration,year_month = read_yt_csv("The Doers")

#horizontal_bar(ages_yt,male_viewer_yt,female_viewer_yt,"The Doers")

Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
Unemployment_Rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]

#animatedline_chart(Year,Unemployment_Rate,"The Doers")
