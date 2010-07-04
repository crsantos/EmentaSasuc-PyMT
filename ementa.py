IS_PYMT_PLUGIN = True
PLUGIN_TITLE = 'Ementa Sasuc'
PLUGIN_AUTHOR = 'Carlos Ricardo Santos'
PLUGIN_DESCRIPTION = 'Visualizador da Ementa dos Sasuc para os diversos dias, de acordo com o trimestre'

from pymt import *
import glob,os,urllib
from PIL import Image
from datetime import date

class Ementa(MTWidget):
    """docstring for Ementa"""
    def __init__(self,  **kargs):
        super(Ementa, self).__init__()
        
        url="http://www.uc.pt/sasuc/ServicosApoioEstudantes/Alimentacao/"
        days= [     "Ementa2_Segunda",
                    "Ementa3_Terca",
                    "Ementa4_Quarta",
                    "Ementa5_Quinta",
                    "Ementa6_Sexta",
                    "Ementa7_Sabado",
                    "Ementa1_Domingo"
                                        ]
        self.label = "LOLOLOLOLOL"                     
        
        for day in days: # only retrieve images not cached
            urllib.urlretrieve(url+day, "images/"+day+".png")
        # build a KineticList
        k = MTKineticList( size= getWindow().size, friction=1, do_x=True, padding_x=0,
                          h_limit=1, do_y=False, title="Ementa Sasuc", deletable=False,
                          searchable=False, w_limit=0)
        k.index=date.weekday(date.today())
        # search file in image directory
        for x in xrange(len(days)):
            for filename in glob.glob(os.path.join(os.path.dirname(__file__), 'images', '*.png')):
                k.add_widget(MTKineticImage(image=Loader.image(filename))) # adds each image to list
        self.add_widget(k) # appends widget to main app            

if __name__ == '__main__':
    runTouchApp(Ementa())
