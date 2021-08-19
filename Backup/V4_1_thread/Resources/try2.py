import pygame as pg

class pgtextbox:#By K1521
    def __init__(self,width=100,height=10,fontname=None):
        self.surface=pg.Surface((width,height))
        self.text=""
        self.width=width
        self.height=height
        self.font=pg.font.Font(fontname,pgtextbox.getMaxFontSize(fontname,lineheight=height))
        self.curserindex=0
        self.cursersurface=pg.Surface((self.font.size("|")[0]//2,self.font.size("|")[1]))
        self.cursersurface.fill((255,255,255))
        #self.cursersurface=self.font.render("|",False,(255,255,255),(0,0,0))
        self.offsety=int((height-self.font.get_linesize())/2)
        self.offsetx=0


    def curserpos(self):
        return self.font.size(self.text[:self.curserindex])[0]

    def addPgEvent(self,event):
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_BACKSPACE:
                self.deleteAtCurser()
            elif event.key==pg.K_RIGHT:
                self.offsetCurser(1)
            elif event.key==pg.K_LEFT:
                self.offsetCurser(-1)
            else:
                self.insertAtCurser(event.unicode)

    def render(self):
        self.surface.fill((0,0,0))

        width=self.width-self.cursersurface.get_width()
        text=self.font.render(self.text,False,(255,255,255),(0,0,0))


        if self.curserindex>=0:
            curserpos=self.curserpos()+self.offsetx

            curserposnew=max(0,min(curserpos,width))
            self.offsetx+=curserposnew-curserpos
            curserpos=curserposnew
            #if curserpos<0:
                #self.offsetx-=curserpos
                #curserpos=0
            #if curserpos>width:
                #curserpos=curserpos-width
                #self.offsetx-=curserpos
        else:
            #self.offsetx=min(width-text.get_width(),0)
            self.offsetx=0

        self.surface.blit(text,(self.offsetx,self.offsety))
        if self.curserindex>=0:
            self.surface.blit(self.cursersurface,(curserpos,self.offsety))
            #print((curserpos,self.offsety))
        return self.surface

    def insertAtCurser(self,t):
        if self.curserindex<0:
            self.curserindex=len(self.text)
        self.text=self.text[:self.curserindex]+t+self.text[self.curserindex:]
        self.curserindex+=len(t)

    def deleteAtCurser(self,length=1):
        if self.curserindex<0:
            self.curserindex=len(self.text)

        newcurserindex=max(0,self.curserindex-length)
        self.text=self.text[:newcurserindex]+self.text[self.curserindex:]
        self.curserindex=newcurserindex

    def offsetCurser(self,i):
        self.curserindex=max(min(self.curserindex+i,len(self.text)),0)


    @staticmethod
    def longestline(self,fontname,lines):
        size=pg.font.Font(fontname,1000)
        return max(lines,key=lambda t:size(t)[0])

    @staticmethod
    def getMaxFontSize(fontname,width=None,lineheight=None,line=None):
        def font(size):
            return pg.font.Font(fontname,size)
        fontsize=float("inf")# inf

        if width:
            aproxsize=width*1000//font(1000).size(line)[0]
            while font(aproxsize).size(line)[0]<width:
                aproxsize+=1
            while font(aproxsize).size(line)[0]>width:
                aproxsize-=1
            fontsize=min(aproxsize,fontsize)

        if lineheight:
            aproxsize=lineheight*4//3
            while font(aproxsize).get_linesize()<lineheight:
                aproxsize+=1
            while font(aproxsize).get_linesize()>lineheight:
                aproxsize-=1
            fontsize=min(aproxsize,fontsize)
        return fontsize

    @staticmethod
    def rendermultilinetext(text,width=None,height=10,fontname=None,antialias=False,color=(255,255,255),background=None):
        if(len(text)-text.count("\n")==0):
            return pg.Surface((0,0))
        def font(size):
            return pg.font.Font(fontname,size)

        text=text.split("\n")
        fontsize=1000000000# inf

        longestline=None
        if height:
            longestline=pgtextbox.longestline(fontname,lines)
        fontsize=pgtextbox.getMaxFontSize(fontname,width,lineheight,longestline)

        font=font(fontsize)
        width=font.size(longestline)[0]
        lineheight=font.get_linesize()
        heigth=len(text)*lineheight
        textsurface=pg.Surface((width,heigth))
        if background:
            textsurface.fill(background)
        for i,line in enumerate(text):
            textsurface.blit(font.render(line,antialias,color,background),(0,i*lineheight))
        return textsurface

import pygame as pg
pg.init()

screen=pg.display.set_mode((1000,500))
textbox=pgtextbox(200,20)
textbox.insertAtCurser('Hallo')

while True:
    e = pg.event.wait(30000)
    if e.type == pg.QUIT:
        raise StopIteration

    textbox.addPgEvent(e)#uses keydown events
    
    print(textbox.text)

    screen.fill((0,0,0))
    screen.blit(textbox.render(),(10,0))
    pg.display.flip()
pg.display.quit()