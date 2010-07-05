#!/usr/bin/env python
# encoding: utf-8
"""
ementa.py

Created by crsantos on 2010-07-05.
Copyright (c) 2010 DEI-FCTUC. All rights reserved.
"""

IS_PYMT_PLUGIN = True
PLUGIN_TITLE = 'Ementa Sasuc'
PLUGIN_AUTHOR = 'Carlos Ricardo Santos'
PLUGIN_DESCRIPTION = 'Visualizador da Ementa dos Sasuc para os diversos dias, de acordo com o trimestre'

from pymt import *
import glob,os,urllib
from PIL import Image
from datetime import date

exit_button_css = '''
.exit_button {
    draw-border: 1;
    border-radius: 5;
    draw-text-shadow: 1;
    text-shadow-color:#333333;
    draw-alpha-background: 1;
}

.list{
    /*draw-border: 1;*/
    /*border-radius: 10;*/
}
'''
css_add_sheet(exit_button_css)

class Ementa(MTWidget):
    """docstring for Ementa"""
    def __init__(self,  **kargs):
        super(Ementa, self).__init__()
        self.exit_size=35
        self.bg_image = Loader.image("images/back.jpg")
        #self.bg_image.scale = float(self.width)/self.bg_image.width
        
        url="http://www.uc.pt/sasuc/ServicosApoioEstudantes/Alimentacao/"
        days= [     "Ementa2_Segunda", "Ementa3_Terca",
                    "Ementa4_Quarta", "Ementa5_Quinta",
                    "Ementa6_Sexta", "Ementa7_Sabado", "Ementa1_Domingo" ]

        for day in days: # only retrieve images not cached
            urllib.urlretrieve(url+day, "images/"+day+".png")

        # build a KineticList
        self.k = MTKineticList( size= getWindow().size, friction=1, do_x=True, padding_x=0,
                          h_limit=1, do_y=False, title="Ementa Sasuc", deletable=False,
                          searchable=False, w_limit=0,cls=('list'))
        
        # point to the index of the current day -not working
        #self.k.index=date.weekday(date.today())

        # search file in image directory
        for x in xrange(len(days)):
            for filename in glob.glob(os.path.join(os.path.dirname(__file__), 'images', '*.png')):
                self.k.add_widget(MTKineticImage(image=Loader.image(filename))) # adds each image to list
        self.add_widget(self.k) # appends widget to main app
        self.label=MTLabel(label='crsantos',font_size=8,bold=True, color=(1, 1, 1, .5), pos=(getWindow().size[0]-70,10))
        self.add_widget(self.label)
        
        exit_button = MTButton( label="X", size=(self.exit_size,self.exit_size),pos=(getWindow().size[0]-self.exit_size-2, getWindow().size[1]-self.exit_size-2),cls=('exit_button'))
        @exit_button.event
        def on_release(touch):
            exit()
        self.add_widget(exit_button)        

    def draw(self):
        self.bg_image.draw()
        
    def on_update(self):
        pass#print self.k.index

if __name__ == '__main__':
    runTouchApp(Ementa())
