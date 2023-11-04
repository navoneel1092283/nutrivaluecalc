import numpy as np
import pandas as pd


#input in kJ
def energy_points(e):
    e_point=0
        
    if(e>335 and e<=670):
        e_point=1

    if(e>670 and e<=1005):
    	e_point=2        

    if(e>1005 and e<=1340):
        e_point=3

    if(e>1340 and e<=1675):
        e_point=4       

    if(e>1675 and e<=2010):
        e_point=5

    if(e>2010 and e<=2345):
        e_point=6           
 
    if(e>2345 and e<=2680):
        e_point=7

    if(e>2680 and e<=3015):
        e_point=8      
 
    if(e>3015 and e<=3350):
        e_point=9
        
    if(e>3350):
        e_point=10
        
    return e_point*(-1)

#Saturated fat in grams

def saturated_fat_points(f):
    f_point=0
    
    if(f>1 and f<=2):
        f_point=1
        
    if(f>2 and f<=3):
        f_point=2        

    if(f>3 and f<=4):
        f_point=3 

    if(f>4 and f<=5):
        f_point=4       

    if(f>5 and f<=6):
        f_point=5          

    if(f>6 and f<=7):
        f_point=6   
        
    if(f>7 and f<=8):
        f_point=7         

    if(f>8 and f<=9):
        f_point=8   
        
    if(f>9 and f<=10):
        f_point=9   
        
    if(f>10):
        f_point=10            
        
    return f_point*(-1)

#sodium in mgs

def total_sodium_points(f):
    f_point=0
    
    if(f>90 and f<=180):
        f_point=1

    if(f>180 and f<=270):
        f_point=2            
        
    if(f>270 and f<=360):
        f_point=3       

    if(f>360 and f<=450):
        f_point=4 

    if(f>450 and f<=540):
        f_point=5       

    if(f>540 and f<=630):
        f_point=6          

    if(f>630 and f<=720):
        f_point=7   
        
    if(f>720 and f<=810):
        f_point=8         

    if(f>810 and f<=900):
        f_point=9       
    
    if(f>900):
        f_point=10            
        
    return f_point*(-1)

#sugar in grams

def total_sugar_points(f):
    f_point=0
    
    if(f>4.5 and f<=9):
        f_point=1

    if(f>9 and f<=13.5):
        f_point=2            
        
    if(f>13.5 and f<=18):
        f_point=3       

    if(f>18 and f<=22.5):
        f_point=4 

    if(f>22.5 and f<=27):
        f_point=5       

    if(f>27 and f<=31):
        f_point=6          

    if(f>31 and f<=36):
        f_point=7   
        
    if(f>36 and f<=40):
        f_point=8         

    if(f>40 and f<=45):
        f_point=9       
    
    if(f>45):
        f_point=10            
        
    return f_point*(-1)

        
#fruits/veggies/nuts in %

def veggies_points(f):
    f_point=0
    
    if(f>40 and f<=60):
        f_point=1

    if(f>60 and f<=80):
        f_point=2            
        
    if(f>=80):
        f_point=5          
        
    return f_point

        
#fibres in g

def fibres_points(f):
    f_point=0
    
    if(f>0.7 and f<=1.4):
        f_point=1

    if(f>1.4 and f<=2.1):
        f_point=2            

    if(f>2.1 and f<=2.8):
        f_point=3  
      
    if(f>2.8 and f<=3.5):
        f_point=4     
                
    if(f>3.5):
        f_point=5            
        
    return f_point
                    
def protiens_points(f):
    f_point=0
    
    if(f>1.6 and f<=3.2):
        f_point=1

    if(f>3.2 and f<=4.8):
        f_point=2            

    if(f>4.8 and f<=6.4):
        f_point=3  
      
    if(f>6.4 and f<=8.0):
        f_point=4     
                
    if(f>8.0):
        f_point=5            
        
    return f_point