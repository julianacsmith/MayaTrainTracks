import maya.cmds as cmds
import math

# Sets the shaders of all my objects
def setShader(r,g,b,object,metal=0.5):
    shader = cmds.shadingNode("standardSurface", asShader=True)
    cmds.select(object)
    cmds.setAttr((shader + ".baseColor"),r,g,b, type="double3")
    cmds.setAttr((shader + ".metalness"), metal)
    cmds.hyperShade(assign=shader)
    
# Sets kyeframes for animation
def setKeyFrame(object):
    startTime = cmds.playbackOptions(query=True, minTime=True)
    endTime = cmds.playbackOptions(query=True, maxTime=True)
    
    cmds.cutKey(object, time=(startTime, endTime), attribute="rotateX")
    cmds.setKeyframe(object, time=startTime, attribute="rotateX", value=0)
    cmds.setKeyframe(object, time=endTime, attribute="rotateX", value=720)
    
def setKeyFrameTracks(object):
    startTime = cmds.playbackOptions(query=True, minTime=True)
    endTime = cmds.playbackOptions(query=True, maxTime=True)
    
    cmds.cutKey(object, time=(startTime, endTime), attribute="translateZ")
    cmds.setKeyframe(object, time=startTime, attribute="translateZ", value=0)
    cmds.setKeyframe(object, time=endTime, attribute="translateZ", value=-100)

# Makes the roof of my train
def makeRoof():
    cmds.select( cl=True )
    conductor = cmds.polyCylinder( r=1, h=2, sx=20, sy=1, sz=1, ax=(0, 1, 0), cuv=1, ch=1, name='ConductorRoof' )
    cmds.scale(4.2, 4.2, 6)
    cmds.move(0,7.05,-10.7)
    cmds.polyCut( 'ConductorRoof.f[0:59]', cd='X', df=1, ch=1 )
    setShader(1,0,0,conductor,0)
    booth = cmds.group(conductor, n="Roof")
    
    roofPart = cmds.polyCylinder(h=8.4, n="RoofPart")
    cmds.move(0,7.05,-5.7)
    setShader(1,0,0,roofPart,0)
    cmds.parent(roofPart, booth)
    
    roofPart = cmds.polyCylinder(h=8.4, n="RoofPart")
    cmds.move(0,7.05,-7.7)
    setShader(1,0,0,roofPart,0)
    cmds.parent(roofPart, booth)
    
    roofPart = cmds.polyCylinder(h=8.4, n="RoofPart")
    cmds.move(0,7.05,-9.7)
    setShader(1,0,0,roofPart,0)
    cmds.parent(roofPart, booth)
    
    roofPart = cmds.polyCylinder(h=8.4, n="RoofPart")
    cmds.move(0,7.05,-11.7)
    setShader(1,0,0,roofPart,0)
    cmds.parent(roofPart, booth)
    
    roofPart = cmds.polyCylinder(h=8.4, n="RoofPart")
    cmds.move(0,7.05,-13.7)
    setShader(1,0,0,roofPart,0)
    cmds.parent(roofPart, booth)
    
    roofPart = cmds.polyCylinder(h=8.4, n="RoofPart")
    cmds.move(0,7.05,-15.7)
    setShader(1,0,0,roofPart,0)
    cmds.parent(roofPart, booth)
    
    cmds.select("Roof")
    cmds.rotate(0,-8,90)
    
    roofPart = cmds.polyCube(h=0.5, w=9, d=13, n="RoofPart")
    cmds.rotate(8,0,0)
    cmds.move(-0.1,15.5,4)
    setShader(10,10,0,roofPart)
    return booth
    
# Makes circular nails around 2 axes
def makeCircularNails_xy(amt, radius, x_offset, y_offset, z_offset):
    degree=0
    nails = cmds.group(em = True, name="Nails")
    for i in range(amt):
        nail = cmds.polyCylinder(h=1, r=0.2, name="TrainNail")
        cmds.move(math.cos(degree)*radius+x_offset,math.sin(degree)*radius+y_offset,z_offset)
        cmds.rotate(90,0,0)
        setShader(10,10,0,nail)
        cmds.parent(nail, nails)
        degree += (360/amt)*(math.pi/180)
    return nails
    
def makeCircularNails_yz(amt, radius, x_offset, y_offset, z_offset):
    degree=0
    nails = cmds.group(em = True, name="Nails")
    for i in range(amt):
        nail = cmds.polyCylinder(h=0.6, r=0.2, name="TrainNail")
        cmds.move(x_offset,math.sin(degree)*radius+y_offset,math.cos(degree)*radius+z_offset)
        cmds.rotate(0,0,90)
        setShader(10,10,0,nail)
        cmds.parent(nail, nails)
        degree += (360/amt)*(math.pi/180)
    return nails

# Makes each wheel
def makeWheel(wheelNum, radius, spokes, offset_x, offset_y, offset_z):
    wheelBase = cmds.polyCylinder(h=0.5, r=radius, name = "WheelBase")
    cmds.rotate(0,0,90)
    wheel = cmds.group(wheelBase, name="Wheel")
   
    wheelBaseDiff = cmds.polyCylinder(h=3, r = radius*0.8, name = "WheelBaseDiff")
    cmds.rotate(0,0,90)
    cmds.parent(wheelBaseDiff, wheel)
    
    wheelBase = cmds.polyBoolOp( 'WheelBase', 'WheelBaseDiff', op=2, n='WheelBase' )
    cmds.parent(wheelBase, wheel)
    cmds.delete(("WheelBase" + str(wheelNum)), constructionHistory = True)
    setShader(1,0,0,("WheelBase" + str(wheelNum)))
    
    angle = 0
    angleInc = 180//spokes
    for i in range(spokes):
        wheelSpoke = cmds.polyCylinder(h=radius*2-1, r=0.2, name = "WheelSpoke")
        cmds.rotate(angle,0,0)
        setShader(1,0,0,wheelSpoke)
        cmds.parent(wheelSpoke, wheel)
        angle += angleInc
        
    wheelCenter = cmds.polyCylinder(h=1, r=radius/4, name="WheelCenter")
    cmds.rotate(0,0,90)
    setShader(1,0,0,wheelCenter)
    cmds.parent(wheelCenter, wheel)
    
    wheelNails = makeCircularNails_yz(spokes, radius*0.9, offset_x, offset_y, offset_z)
    cmds.select(wheel)
    cmds.move(offset_x, offset_y, offset_z)
    cmds.parent(wheelNails, wheel)
    setKeyFrame(wheel)
    
    return wheel
    
# Makes each cart
def makeCart(wheelBaseNum):
    cart = cmds.group(em=True, name="Cart")
    
    roof = cmds.polyCylinder( r=1, h=2, sx=20, name='CartRoof' )
    cmds.scale(4.2, 5.5, 14.2)
    cmds.move(0,9.3,0)
    cmds.polyCut('CartRoof.f[0:59]', cd='X', df=1 )
    cmds.rotate(0,0,90)
    cmds.select("CartRoof.e[24:25]", "CartRoof.e[35:36]", "CartRoof.e[46:47]")
    cmds.polyCloseBorder()
    setShader(0,0,0.8,roof,0.3)
    cmds.parent(roof, cart)
    
    roofPart = cmds.polyCube(h=3, w=7, d=17, name = "CartRoofPart")
    cmds.move(0,13,0)
    setShader(0.5,0.5,0.5,roofPart)
    cmds.parent(roofPart, cart)
    
    roofPart1 = cmds.polyCylinder( r=1, h=2, sx=20, name='CartRoofPart1' )
    cmds.scale(3, 4, 10)
    cmds.move(0,14,0)
    cmds.polyCut('CartRoofPart1.f[0:59]', cd='X', df=1 )
    cmds.rotate(0,0,90)
    cmds.select("CartRoofPart1.e[24:25]", "CartRoofPart1.e[35:36]", "CartRoofPart1.e[46:47]")
    cmds.polyCloseBorder()
    setShader(0.8,0,0,roofPart1, 0.3)
    cmds.parent(roofPart1, cart)
    
    roofRim = cmds.polyCube(h=0.5, w=9, d=21, name = "RoofPartRim")
    cmds.move(0,14,0)
    setShader(10,0,0,roofRim)
    cmds.parent(roofRim, cart)

    roofRim = cmds.polyCube(h=0.5, w=12, d=30, name = "RoofPartRim")
    cmds.move(0,9,0)
    setShader(0,0,10,roofRim)
    cmds.parent(roofRim, cart)
        
    cartWheelBase = cmds.polyCube(h=3,w=7,d=29, name = "CartWheelBase")
    cmds.move(0,-11,0)
    setShader(1,0,0,cartWheelBase)
    cmds.parent(cartWheelBase, cart)
    
    cartWheelBaseConnector = cmds.polyCube(h=1,w=2,d=35, name = "CartWheelBaseConnector")
    cmds.move(0,-11,0)
    setShader(0.5,0.5,0.5,cartWheelBaseConnector)
    cmds.parent(cartWheelBaseConnector, cart)
    
    booth = cmds.polyCylinder(h=8, r=4, name = "Booth")
    cmds.rotate(0,0,90)
    cmds.scale(0.8, 1, 0.4)
    cmds.move(0,-5,-10.25)
    setShader(1,0,0,booth,0.1)
    cmds.parent(booth, cart)
    
    cmds.duplicate("Booth")
    cmds.move(0,-5,-4)
    
    cmds.duplicate("Booth1")
    cmds.move(0,-5, 2)
    
    booth = cmds.polyCylinder(h=8, r=4, name = "BoothSeat")
    cmds.rotate(0,90,90)
    cmds.scale(0.6, 1, 0.4)
    cmds.move(0,-8,-8)
    setShader(1,0,0,booth, 0.1)
    cmds.parent(booth, cart)
    
    cmds.duplicate("BoothSeat")
    cmds.move(0,-8,-1)
    
    cmds.duplicate("BoothSeat1")
    cmds.move(0,-8,5)
    
    flip = -1
    wheels = []
    for i in range(6):
        if flip == -1:
            wheel = makeWheel(wheelBaseNum, 4, 8, flip*5.5,-12,8.5-8.5*i)
            wheels.append(wheel)
            
            wheelRod = cmds.polyCylinder(h=10, name = "wheelRod")
            cmds.move(0,-12,8.5-8.5*i)
            cmds.rotate(0,0,90)
            setShader(1,0,0,wheelRod)
            cmds.parent(wheelRod, cart)
        else:
            wheel = makeWheel(wheelBaseNum, 4, 8, flip*5.5,-12,8.5-8.5*(i-3))
            wheels.append(wheel)
 
        if i == 2:
            flip = 1
        wheelBaseNum += 1
    cartWheels = cmds.group(wheels, name="CartWheels")
    cmds.parent(cartWheels, cart)
    
    cartBase = cmds.polyCube(h=20,w=10,d=25,name = "Base")
    base = cmds.group(cartBase, name = "Cart1Base")
    diff = cmds.group(em=True, name="Cart1Diff")
    
    for i in range(2):
        cartBaseTrim = cmds.polyCube(h=20, name = "CartBaseTrim")
        cmds.move(4.7,0,flip*12.2)
        setShader(0.6, 0, 0.2, cartBaseTrim)
        cmds.parent(cartBaseTrim, cart)
        
        cartBaseTrim = cmds.polyCube(h=20, name = "CartBaseTrim")
        cmds.move(-4.7,0,flip*12.2)
        setShader(0.6, 0, 0.2, cartBaseTrim)
        cmds.parent(cartBaseTrim, cart)
        flip = -1
    
    for i in range(4):
        cartWindow = cmds.polyCube(h=7, w=15, d=3, name = "CartWindow")
        windowCart = cmds.group(cartWindow, name= ("Window"+str(i)))
        cartWindowTop = cmds.polyCylinder(h=15, r=1.5, name = "CartWindowTop")
        cmds.rotate(0,0,90)
        cmds.move(0,3.5,0)
        cmds.parent(cartWindowTop, windowCart)
        
        cmds.select(("Window" + str(i)))
        cmds.scale(1,1.5,1.5)
        cmds.move(0,0,9-6*i)
        cmds.parent(windowCart, diff)
    
    frontWindow = cmds.polyCube(h=12, w=8, d=30, name = "FrontWindow")
    cmds.move(0,1,0)
    cmds.parent(frontWindow, diff)
    
    interiorHollow = cmds.polyCube(h=18, w=8, d=23, name = "InteriorHollow")
    cmds.parent(interiorHollow, diff)
    
    entranceHollow = cmds.polyCylinder(h=15, r=2.25, name = "EntranceHollow")
    cmds.rotate(0,0,90)
    cmds.move(0,-5.5,9)
    cmds.parent(entranceHollow, diff)
    
    cmds.polyCBoolOp("Cart1Base", "Cart1Diff", op=2, name="CartFrame")
    cmds.delete("CartFrame", constructionHistory = True)
    setShader(0.8,1,1,"CartFrame")
    cmds.parent("CartFrame", cart)
    
    return cart 
       
# Makes the locomative. Like the main train
def makeTrain():
    body = cmds.polyCylinder(h=12, r=3, name="TrainBody")
    cmds.rotate(90,0,0)
    cmds.move(0,1,0)
    setShader(0.1,0.1,0.1,body)
    Train = cmds.group(body, name="Train")
    
    light = cmds.polyCylinder(h=1, r=2, name="TrainLight")
    cmds.rotate(90,0,0)
    cmds.move(0,1,6)
    setShader(1.0,0.8,0,light,1)
    cmds.parent(light, Train)
    
    rim = cmds.polyCylinder(h=1, r=3.2,name="TrainRimMid")
    cmds.move(0,1,0)
    cmds.rotate(90,0,0)
    setShader(10,10,0,rim)
    cmds.parent(rim, Train)
    
    rim = cmds.polyCylinder(h=1, r=3.2,name="TrainRimFront")
    cmds.rotate(90,0,0)
    cmds.move(0,1,5)
    setShader(10,10,0,rim)
    cmds.parent(rim, Train)
    
    rim = cmds.polyCylinder(h=1, r=3.2,name="TrainRimBack")
    cmds.rotate(90,0,0)
    cmds.move(0,1,-5)
    setShader(10,10,0,rim)
    cmds.parent(rim, Train)
    
    rim = cmds.polyCube(h=0.7, w=6.3, d=10, n="TrainRimHalf")
    cmds.move(0,1,0)
    setShader(10,10,0,rim)
    cmds.parent(rim, Train)
    
    base = cmds.polyCube(h=2, w=6, d=20, name="TrainBase")
    cmds.move(0,-3,-3)
    setShader(1,0,0,base)
    cmds.parent(base, Train)
    
    trainBaseConnector = cmds.polyCube(h=0.5,w=1.6,d=15, name = "TrainBaseConnector")
    cmds.move(0,-3.8,-16)
    setShader(0.5,0.5,0.5,trainBaseConnector)
    cmds.parent(trainBaseConnector, Train)
    
    smokeStack = cmds.polyCylinder(h=6, name="SmokeStackPipe")
    cmds.move(0,4.5,2.5)
    setShader(1.0,0.8,0,smokeStack,1)
    cmds.parent(smokeStack, Train)
    
    smokeStack = cmds.polyCylinder(h=2, r=1.25, name="SmokeStackPipeBase")
    cmds.move(0,3.5,2.5)
    setShader(1.0,0.8,0,smokeStack,1)
    cmds.parent(smokeStack, Train)
    
    smokeStack = cmds.polyCone(h=4, r=2.5, sx=8, name ="SmokeStackFlare")
    cmds.rotate(180,0,0)
    cmds.move(0,7,2.5)
    setShader(1.0,0.8,0,smokeStack,1)
    cmds.parent(smokeStack, Train)
    
    smokeStack = cmds.polyCylinder(h=1.5, r=2.5, sx=8, name ="SmokeStackFlareTop")
    cmds.move(0, 9.75, 2.5)
    cmds.select("SmokeStackFlareTop.e[8:15]")
    cmds.scale(0.5,0,0.5)
    setShader(1.0,0.8,0,smokeStack,1)
    cmds.parent(smokeStack, Train)
    
    conductor = cmds.polyCube(h=8, w=7, d=9, name = "ConductorBooth")
    cmds.move(0,0,-10)
    setShader(0.1,0.1,0.1,conductor)
    cmds.parent(conductor, Train)
    
    conductor = cmds.polyCube(h=6, w=6.5, d=2.5, name = "ConductorWindow")
    cmds.move(0,5,-7)
    setShader(0.1,0.1,0.1,conductor)
    cmds.parent(conductor, Train)
    
    booth = makeRoof()
    cmds.select("Roof")
    cmds.move(-2.2,3,0)
    cmds.parent(booth, Train)
    
    conductor = cmds.polyCube(h=6, w=6, d=10, name = "ConductorBoothDifference")
    cmds.move(0,1,-13.5)
    cmds.parent(conductor, Train)
    
    conductor = cmds.polyBoolOp( 'ConductorBooth', 'ConductorBoothDifference', op=2, n='ConductorBooth' )
    cmds.parent(conductor, Train)
    cmds.delete("ConductorBooth1", constructionHistory = True)
    setShader(1,0,0,"ConductorBooth1")
    
    cowCatcher = cmds.polyCube(h=4, w=7, d=0.5, n= "CowCatcher")
    cmds.move(0,3.5,22)
    cmds.select("CowCatcher.e[0]","CowCatcher.e[1]")
    cmds.polySplitRing(stp=2, div=1, uem=True, sma=30, fq=True)
    cmds.select("CowCatcher.vtx[8]")
    cmds.move(0,0,5,r=True)
    
    diff = cmds.group(empty=True, n="CatcherDiff")
    
    for i in range(6):
        cowCatcherDiff = cmds.polyCube(h=3, w=0.5, d=10, n="CowDiff")
        cmds.move(3-i*1.2,3.65,23)
        cmds.parent(cowCatcherDiff, diff)
    
    newCatcher = cmds.polyCBoolOp("CowCatcher", "CatcherDiff", op=2, n="CowCatcher")
    cmds.delete("CowCatcher1", constructionHistory = True)
    cmds.move(0,-7,-15)
    setShader(1,0,0,"CowCatcher1")
    cmds.parent("CowCatcher1", Train)
    
    rimNails = makeCircularNails_xy(12, 2.5, 0, 1, 5.6)
    cmds.parent(rimNails, Train)
    
    cmds.select(Train)
    cmds.move(0,6,0)

# Makes th train tracks
def makeRail(offSet):
    trackPart = cmds.group(em=True, name="TrackSlat")
    
    # Make Slat/Sleeper
    slat = cmds.polyCube(w=9, h=0.2, name="Slat")
    setShader(0.42,0.31,0.18,slat,0.2)
    nails = cmds.group(slat, name = "nails")
       
    flip = -1
    i = 0
    
    for i in range(2):
        railPart1 = cmds.polyCube(ch=True, o=True, w=(2.2), h=0.3, d=0.6, cuv=4, name="Rail1Part")
        cmds.rotate(0, 90, 0)
        cmds.move(flip*3, 0, 0)
        cmds.parent(railPart1, trackPart)
      
        railPart2 = cmds.polyCube(ch=True, o=True, w=(2.2), h=0.6, d=0.2, cuv=4, name="Rail1Part")
        cmds.rotate(0, 90, 0)
        cmds.move(flip*3, 0.45, 0)
        cmds.parent(railPart2, trackPart)
       
        railPart3 = cmds.polyCube(ch=True, o=True, w=(2.2), h=0.3, d=0.6, cuv=4, name="Rail1Part")
        cmds.rotate(0, 90, 0)
        cmds.move(flip*3, 0.9, 0)
        cmds.parent(railPart3, trackPart)
        
        # Create Nail Beds
        nailBed1 = cmds.polyCube(w=1.5, h=0.2, d=0.7, name="NailBed")
        cmds.move(flip*3, 0.1, 0)
        cmds.parent(nailBed1, nails)
        
        nailBed3 = cmds.polyCube(w=0.7, h=0.2, d=0.65, name="NailBed")
        cmds.move(flip*3, 0.2, 0)
        cmds.parent(nailBed3, nails)
            
        nailBed4 = cmds.polyCube(w=1, h=0.4, d=0.4, name="NailBed")
        cmds.move(flip*3, 0.3, 0)
        cmds.parent(nailBed4, nails)
        
        # Make the Nails (Far right) x1 = 3.63, x2 = 3.3
        nail1 = cmds.polyCylinder(h=0.35, r=.06, sa=6, name="Nail")
        cmds.rotate(0, 90, 0)
        cmds.move(flip*3.63, .2, -0.2)
        cmds.parent(nail1, nails)
        
        nail2 = cmds.polyCylinder(h=0.35, r=.06, sa=6, name="Nail")
        cmds.rotate(0, 90, 0)
        cmds.move(flip*3.63, .2, 0.2)
        cmds.parent(nail2, nails)
        
        nail3 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(flip*3.63, .05, -0.2)
        cmds.parent(nail3, nails)
        
        nail4 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(flip*3.63, .05, 0.2)
        cmds.parent(nail4, nails)
        
        nail5 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(flip*3.3, .33, 0)
        cmds.parent(nail5, nails)
        
        nail6 = cmds.polyCylinder(h=0.4, r=.06, sa=6, name="Nail")
        cmds.move(flip*3.3, .4, 0)
        cmds.parent(nail6, nails)
        
        nail7 = cmds.polyCylinder(h=0.4, r=.04, name="Nail")
        cmds.move(flip*3.3, .405, 0)
        cmds.parent(nail7, nails)
        
        # Make Nails (Center-Right
        nail8 = cmds.polyCylinder(h=0.35, r=.06, sa=6, name="Nail")
        cmds.rotate(0, 90, 0)
        cmds.move(flip*2.37, .2, -0.2)
        cmds.parent(nail8, nails)
        
        nail9 = cmds.polyCylinder(h=0.35, r=.06, sa=6, name="Nail")
        cmds.rotate(0, 90, 0)
        cmds.move(flip*2.37, .2, 0.2)
        cmds.parent(nail9, nails)
        
        nail10 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(flip*2.37, .05, -0.2)
        cmds.parent(nail10, nails)
        
        nail11 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(flip*2.37, .05, 0.2)
        cmds.parent(nail11, nails)
        
        nail12 = cmds.polyCylinder(h=0.4, r=.1, name="Nail")
        cmds.move(flip*2.7, .33, 0)
        cmds.parent(nail12, nails)
        
        nail13 = cmds.polyCylinder(h=0.4, r=.06, sa=6, name="Nail")
        cmds.move(flip*2.7, .4, 0)
        cmds.parent(nail13, nails)
        
        nail14 = cmds.polyCylinder(h=0.4, r=.04, name="Nail")
        cmds.move(flip*2.7, .405, 0)
        cmds.parent(nail14, nails)
        
        flip = 1
    cmds.parent(nails, trackPart)
    cmds.select(trackPart)
    cmds.move(0,0,offSet)
    return trackPart
       
        

railInput = cmds.promptDialog(message="How many cars to make? >>> ", backgroundColor = [.175, .215, .237])
numCarts = int(cmds.promptDialog(query=True, text=True))

offSet = 0
Tracks = cmds.group(em=True, name="Tracks")
for i in range(200):
    tracks = makeRail(offSet)
    cmds.parent(tracks, Tracks)
    offSet += 2.2
    
makeTrain()

# Big Wheels

makeWheel(1, 5, 7, 4, 4.75, -10)
makeWheel(2, 5, 7, -4, 4.75, -10)

# Small Wheels

makeWheel(3, 2.5, 6, 4, 2.2, 2.5)
makeWheel(4, 2.5, 6, -4, 2.2, 2.5)

wheelRod = cmds.polyCylinder(h=8, r=0.5, name = "wheelRod")
cmds.move(0,2.2, 2.5)
cmds.rotate(0,0,90)
setShader(1,0,0,wheelRod)

makeWheel(5, 2.5, 6, 4, 2.2, -2.5)
makeWheel(6, 2.5, 6, -4, 2.2, -2.5)

wheelRod2 = cmds.polyCylinder(h=8, r=0.5, name = "wheelRod")
cmds.move(0,2.2, -2.5)
cmds.rotate(0,0,90)
setShader(1,0,0,wheelRod2)

MainTrain = cmds.group("Train", "Wheel", "Wheel1", "Wheel2", "Wheel3", "Wheel4", "Wheel5", wheelRod, wheelRod2, name="MainTrain")
cmds.move(0,1.3,15)

wheelBaseNum = 7
cartTest = makeCart(wheelBaseNum)
cmds.select(cartTest)
cmds.scale(0.8,0.5,0.5)
cmds.move(0,9,-12)

for i in range(1,numCarts):
    cartTest = cmds.duplicate(cartTest, ic=True)
    cmds.move(0,9,(-12-(16*i)))
    
cmds.select("Tracks")
cmds.scale(1.3,1,1)
setKeyFrameTracks("Tracks")
