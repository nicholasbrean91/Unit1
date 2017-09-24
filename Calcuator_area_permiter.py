# Created by: Nicholas Brean
# Created on: Aug 2016
# Created for: ICS3U
# This program shows area and perimeter of a rectangle,

import ui

def calculate_button(sender):
    #area and perimeter
    
    #input
    length = int(view['length_textbox'].text)
    width = int(view['width_textbox'].text)
    
    #process
    area = length * width
    perimeter = 2 * (length + width)
    
    #output
    view['Area_Answer'].text = 'The area is: ' + str(area) + ' cm^2'
    view['permiter_answer'].text = 'The perimeter is: ' + str(perimeter) + ' cm'
    
view = ui.load_view()
view.present('full_screen')
