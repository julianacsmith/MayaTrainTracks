import maya.cmds as cmds

def makeRail(amtOfRails):
    
    # Create the rails
    railPart1 = cmds.polyCube(ch=True, o=True, w=(2.2*amtOfRails), h=0.3, d=0.6, cuv=4, name="Rail1Part")
    cmds.rotate(0, 90, 0)
    cmds.move(-3, 0, amtOfRails-1)
    tracks = cmds.group(railPart1, name="track")
  
    railPart2 = cmds.polyCube(ch=True, o=True, w=(2.2*amtOfRails), h=0.6, d=0.2, cuv=4, name="Rail1Part")
    cmds.rotate(0, 90, 0)
    cmds.move(-3, 0.45, amtOfRails-1)
    cmds.parent(railPart2, tracks)
   
    railPart3 = cmds.polyCube(ch=True, o=True, w=(2.2*amtOfRails), h=0.3, d=0.6, cuv=4, name="Rail1Part")
    cmds.rotate(0, 90, 0)
    cmds.move(-3, 0.9, amtOfRails-1)
    cmds.parent(railPart3, tracks)
    
    railPart4 = cmds.polyCube(ch=True, o=True, w=(2.2*amtOfRails), h=0.3, d=0.6, cuv=4, name="Rail2Part")
    cmds.rotate(0, 90, 0)
    cmds.move(3, 0, amtOfRails-1)
    cmds.parent(railPart4, tracks)
    
    railPart5 = cmds.polyCube(ch=True, o=True, w=(2.2*amtOfRails), h=0.6, d=0.2, cuv=4, name="Rail2Part")
    cmds.rotate(0, 90, 0)
    cmds.move(3, 0.45, amtOfRails-1)
    cmds.parent(railPart5, tracks)
    
    railPart6 = cmds.polyCube(ch=True, o=True, w=(2.2*amtOfRails), h=0.3, d=0.6, cuv=4, name="Rail2Part")
    cmds.rotate(0, 90, 0)
    cmds.move(3, 0.9, amtOfRails-1)
    cmds.parent(railPart6, tracks)
    
    # Create the slats and nails
    for i in range(amtOfRails):
        # Make Slat/Sleeper
        slat = cmds.polyCube(w=9, h=0.2, name="Slat")
        cmds.move(0, 0, (2*i))
        nails = cmds.group(slat, name = "nails")
        
        # Make the Nail Beds
        nailBed1 = cmds.polyCube(w=1.5, h=0.2, d=0.7, name="NailBed")
        cmds.move(3, 0.1, 2*i)
        cmds.parent(nailBed1, nails)
        
        nailBed2 = cmds.polyCube(w=1.5, h=0.2, d=0.7, name="NailBed")
        cmds.move(-3, 0.1, 2*i)
        cmds.parent(nailBed2, nails)
        
        nailBed3 = cmds.polyCube(w=0.7, h=0.2, d=0.65, name="NailBed")
        cmds.move(3, 0.2, 2*i)
        cmds.parent(nailBed3, nails)
        
        nailBed4 = cmds.polyCube(w=1, h=0.4, d=0.4, name="NailBed")
        cmds.move(3, 0.3, 2*i)
        cmds.parent(nailBed4, nails)
        
        nailBed5 = cmds.polyCube(w=0.7, h=0.2, d=0.65, name="NailBed")
        cmds.move(-3, 0.2, 2*i)
        cmds.parent(nailBed5, nails)
        
        nailBed6 = cmds.polyCube(w=1, h=0.4, d=0.4, name="NailBed")
        cmds.move(-3, 0.3, 2*i)
        cmds.parent(nailBed6, nails)
        
        # Make the Nails (Far right) x1 = 3.63, x2 = 3.3
        nail1 = cmds.polyCylinder(h=0.35, r=.06, sa=6, name="Nail")
        cmds.rotate(0, 90, 0)
        cmds.move(3.63, .2, (2*i)-0.2)
        cmds.parent(nail1, nails)
        
        nail2 = cmds.polyCylinder(h=0.35, r=.06, sa=6, name="Nail")
        cmds.rotate(0, 90, 0)
        cmds.move(3.63, .2, (2*i)+0.2)
        cmds.parent(nail2, nails)
        
        nail3 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(3.63, .05, (2*i)-0.2)
        cmds.parent(nail3, nails)
        
        nail4 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(3.63, .05, (2*i)+0.2)
        cmds.parent(nail4, nails)
        
        nail5 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(3.3, .33, (2*i))
        cmds.parent(nail5, nails)
        
        nail6 = cmds.polyCylinder(h=0.4, r=.06, sa=6, name="Nail")
        cmds.move(3.3, .4, (2*i))
        cmds.parent(nail6, nails)
        
        nail7 = cmds.polyCylinder(h=0.4, r=.04, name="Nail")
        cmds.move(3.3, .405, (2*i))
        cmds.parent(nail7, nails)
        
        # Make Nails (Center-Right
        nail8 = cmds.polyCylinder(h=0.35, r=.06, sa=6, name="Nail")
        cmds.rotate(0, 90, 0)
        cmds.move(2.37, .2, (2*i)-0.2)
        cmds.parent(nail8, nails)
        
        nail9 = cmds.polyCylinder(h=0.35, r=.06, sa=6, name="Nail")
        cmds.rotate(0, 90, 0)
        cmds.move(2.37, .2, (2*i)+0.2)
        cmds.parent(nail9, nails)
        
        nail10 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(2.37, .05, (2*i)-0.2)
        cmds.parent(nail10, nails)
        
        nail11 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(2.37, .05, (2*i)+0.2)
        cmds.parent(nail11, nails)
        
        nail12 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(2.7, .33, (2*i))
        cmds.parent(nail12, nails)
        
        nail13 = cmds.polyCylinder(h=0.4, r=.06, sa=6, name="Nail")
        cmds.move(2.7, .4, (2*i))
        cmds.parent(nail13, nails)
        
        nail14 = cmds.polyCylinder(h=0.4, r=.04, name="Nail")
        cmds.move(2.7, .405, (2*i))
        cmds.parent(nail14, nails)
        
        # Make the Nails (Far Left)
        nail15 = cmds.polyCylinder(h=0.35, r=.06, sa=6, name="Nail")
        cmds.rotate(0, 90, 0)
        cmds.move(-3.63, .2, (2*i)-0.2)
        cmds.parent(nail15, nails)
        
        nail16 = cmds.polyCylinder(h=0.35, r=.06, sa=6, name="Nail")
        cmds.rotate(0, 90, 0)
        cmds.move(-3.63, .2, (2*i)+0.2)
        cmds.parent(nail16, nails)
        
        nail17 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(-3.63, .05, (2*i)-0.2)
        cmds.parent(nail17, nails)
        
        nail18 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(-3.63, .05, (2*i)+0.2)
        cmds.parent(nail18, nails)
        
        nail19 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(-3.3, .33, (2*i))
        cmds.parent(nail19, nails)
        
        nail20 = cmds.polyCylinder(h=0.4, r=.06, sa=6, name="Nail")
        cmds.move(-3.3, .4, (2*i))
        cmds.parent(nail20, nails)
        
        nail21 = cmds.polyCylinder(h=0.4, r=.04, name="Nail")
        cmds.move(-3.3, .405, (2*i))
        cmds.parent(nail21, nails)
        
        # Make Nails (Center-Left
        nail22 = cmds.polyCylinder(h=0.35, r=.06, sa=6, name="Nail")
        cmds.rotate(0, 90, 0)
        cmds.move(-2.37, .2, (2*i)-0.2)
        cmds.parent(nail22, nails)
        
        nail23 = cmds.polyCylinder(h=0.35, r=.06, sa=6, name="Nail")
        cmds.rotate(0, 90, 0)
        cmds.move(-2.37, .2, (2*i)+0.2)
        cmds.parent(nail23, nails)
        
        nail24 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(-2.37, .05, (2*i)-0.2)
        cmds.parent(nail24, nails)
        
        nail25 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(-2.37, .05, (2*i)+0.2)
        cmds.parent(nail25, nails)
        
        nail26 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(-2.7, .33, (2*i))
        cmds.parent(nail26, nails)
        
        nail27 = cmds.polyCylinder(h=0.4, r=.06, sa=6, name="Nail")
        cmds.move(-2.7, .4, (2*i))
        cmds.parent(nail27, nails)
        
        nail28 = cmds.polyCylinder(h=0.4, r=.04, name="Nail")
        cmds.move(-2.7, .405, (2*i))
        cmds.parent(nail28, nails)
        cmds.parent(nails, tracks)
  

railInput = cmds.promptDialog(message="How many rails to make? >>> ", backgroundColor = [.175, .215, .237])
amtOfRails = int(cmds.promptDialog(query=True, text=True))
makeRail(amtOfRails)
railOffset += 10
