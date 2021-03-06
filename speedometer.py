from tkinter import *
import math as m
class RadiusError(Exception):
    pass

class Speedometer():
    def changerange(self,Range=(-10,190),rfont=("Verdana",34)):
        for i in range(-10,195,10): #-10,195,10
            self.canvas.itemconfig(self.range_marks[int((i+10)/10)],text=str((i+10)*(Range[1]-Range[0])/Range[0]),font=rfont)
    def moveto(self,value,tag):
        #if(value>self.range[1]):
            #value=self.range[1]
            #self.canvas.itemconfig(self.needle,fill="#000000")
        #elif(value<self.range[0]):
           # value=self.range[0]
            #self.canvas.itemconfig(self.needle,fill="#000000")
        #else:
        self.canvas.itemconfig(self.needle,fill=self.needlecolor)
        #Where the needle points
        self.canvas.coords(self.needle, self.radius+30, self.radius+30, self.radius+self.radius*m.cos((value*self.slope+self.intercept)*m.pi/180)+30, self.radius-self.radius*m.sin((value*self.slope+self.intercept)*m.pi/180)+30)

        #x: self.radius+self.radius*m.cos((value*self.slope+self.intercept)*m.pi/180)+30
        #y: self.radius-self.radius*m.sin((value*self.slope+self.intercept)*m.pi/180)+30

    #needle        
    def __init__(self,canvas,tag,bg="#ffffff",needlecolor="#ff0000",markscolor="#000000",Range=(0,30),digitscolor="#000000"):
        self.range=Range                                                                        #0,30
        self.needlecolor=needlecolor
        self.canvas=canvas
        self.tag=tag
        temp=self.canvas.coords(tag)
        #if((temp[0]-temp[2])!=(temp[1]-temp[3])):
            #raise RadiusError
        #else:
        self.radius=(temp[2]-temp[0])/2
        self.slope=200.0/(self.range[1]-self.range[0]) #slope was 200
        self.intercept=190-self.range[1]*self.slope     #was 190 before
        self.range_marks=[]
        q=10
        u=0
        #Speed markings
        for i in range(-10,195,20): #-10,195,20
            if(i%10==0):
                #Main speed markings
                x1,y1=self.radius+(self.radius-20)*m.cos(i*m.pi/180)+30,self.radius-(self.radius-20)*m.sin(i*m.pi/180)+30   #speed numbers connected to lines
                canvas.create_line(x1,y1,self.radius+self.radius*m.cos(i*m.pi/180)+30,self.radius-self.radius*m.sin(i*m.pi/180)+30,fill=markscolor,width=2)     #lines I think
                self.range_marks.append(canvas.create_text(x1+u,y1+q, text=int((i+10)*(self.range[1]-self.range[0]-20)/300+self.range[0]), font=("Courier",int(self.radius/9)),fill=digitscolor))
            else:                                                            #was i+10                     #(range[0]-20)/300
                #In between markings
                x1,y1=self.radius+(self.radius-10)*m.cos(i*m.pi/180),self.radius-(self.radius-10)*m.sin(i*m.pi/180)
                canvas.create_line(x1,y1,self.radius+self.radius*m.cos(i*m.pi/180)+30,self.radius-self.radius*m.sin(i*m.pi/180)+30,fill="#acace6",width=2)
            if(i>=90):
                q=+10
                u=q
            else:
                q=10
                u=0

        #Fucking magic or some shit i dont know
        self.needle=canvas.create_line(self.radius,self.radius,self.radius,20,fill=needlecolor,width=3)
        canvas.create_oval(self.radius+20,self.radius+20,self.radius+40,self.radius+40,fill="#ffff00")      #center oval
