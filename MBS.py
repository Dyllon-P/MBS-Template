"""
MBS Multistage Template
Dyllon Preston
"""


from rocketpy import Environment, Rocket, SolidMotor, Flight
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
year, month, day = str(date.today()).split('-')
# DATE = (int(year), int(month), int(day) + 5, 12)  # Adjust Hour in 6 hour increments

DATE = (2022, 1, 28, 12)
DIAM = 10

def magic(d1, d2, d3, d4, d5):
    x1, y1, z1 = d1
    x2, y2, z2 = d2
    x3, y3, z3 = d3
    x4, y4, z4 = d4
    x5, y5, z5 = d5
    ###
    maxZ = max(*z1, *z2, *z3, *z4, *z5)
    maxX = max(*x1, *x2, *x3, *x4, *x5)
    minX = min(*x1, *x2, *x3, *x4, *x5)
    minY = min(*y1, *y2, *y3, *y4, *y5)
    maxY = max(*y1, *y2, *y3, *y4, *y5)
    maxXY = max(maxX, maxY)
    minXY = min(minX, minY)
    ###
    fig1 = plt.figure(figsize=(9, 9))
    ax1 = plt.subplot(111, projection="3d")
    ax1.plot(x1, y1, z1 - 1400, linewidth='2')
    ax1.plot(x2, y2, z2 - 1400, linewidth='2')
    ax1.plot(x3, y3, z3 - 1400, linewidth='2')
    ax1.plot(x4, y4, z4 - 1400, linewidth='2')
    ax1.plot(x5, y5, z5 - 1400, linewidth='2')
    # ax1.plot(x3, y3, z3 - 1400, linewidth='2')
    ax1.scatter(0, 0, 0)
    ax1.set_xlabel("X - East (m)")
    ax1.set_ylabel("Y - North (m)")
    ax1.set_zlabel("Z - Altitude Above Ground Level (m)")
    ax1.set_title("Flight Trajectory")
    ax1.set_zlim3d([0, maxZ])
    ax1.set_ylim3d([minXY, maxXY])
    ax1.set_xlim3d([minXY, maxXY])
    ax1.view_init(15, 45)
    plt.show()

# Parameters for environment
Env = Environment(
    railLength=7.3152,
    latitude=32.990254,
    longitude=-106.974998,
    elevation=1400,
    date=DATE,  # Date in year, month, day, hour UTC format
    )

Env.setAtmosphericModel(type='Forecast', file='GFS')


motor1 = SolidMotor(
    thrustSource="./gtxr.eng",
    burnOut=7.75346560,
    grainNumber=5,
    grainSeparation=0.000127,
    grainDensity=1567.4113,
    grainOuterRadius=0.127/2,
    grainInitialInnerRadius=0.0591566/2,
    grainInitialHeight=0.28140406,
    nozzleRadius=0.113284/2,
    throatRadius=0.02026627,
    interpolationMethod='linear'
)
motor2 = SolidMotor(
    thrustSource="./gtxr.eng",
    burnOut=7.75346560,
    grainNumber=5,
    grainSeparation=0.000127,
    grainDensity=1567.4113,
    grainOuterRadius=0.127/2,
    grainInitialInnerRadius=0.0591566/2,
    grainInitialHeight=0.28140406,
    nozzleRadius=0.113284/2,
    throatRadius=0.02026627,
    interpolationMethod='linear'
)
motor_empty = SolidMotor( #Empty Motor
    thrustSource="./Empty.eng",
    burnOut=.1,
    grainNumber=5,
    grainSeparation=0.000127,
    grainDensity=0.907,
    grainOuterRadius=0.127,
    grainInitialInnerRadius=0.0591566/2,
    grainInitialHeight=0.28140406,
    nozzleRadius=0.113284/2,
    throatRadius=0.02026627, 
    interpolationMethod='linear'
)
Event1 = Rocket( #Booster
    motor=motor1,
    radius=.156718/2,
    mass=75.53846882558567,
    inertiaI=65.16150555935428,
    inertiaZ=8.642868198621159,
    distanceRocketNozzle=2.248412428983355,
    distanceRocketPropellant=1.4208688502810294,
    powerOffDrag="./CD/MBS_CDPowerOff_S+B.csv",
    powerOnDrag="./CD/MBS_CDPowerOn_S+B.csv"
)
Event2 = Rocket( #Sustainer
    motor=motor2,
    radius=.156718/2,
    mass=29.627244893255025,
    inertiaI=7.255057626156905,
    inertiaZ=4.342645507989871,
    distanceRocketNozzle=1.0533242864474788,
    distanceRocketPropellant=0.22578070774515324,
    powerOffDrag="./CD/MBS_CDPowerOff_S.csv",
    powerOnDrag="./CD/MBS_CDPowerOn_S.csv"
)
Event3 = Rocket( #Booster Recovery
    motor=motor_empty,
    radius=.156718/2,
    mass=23.024139893620283,
    inertiaI=6.821259532385813,
    inertiaZ=4.300222690631286,
    distanceRocketNozzle=0.7937596281448074,
    distanceRocketPropellant=0.03378395055751826,
    powerOffDrag="./CD/MBS_CDPowerOff_S.csv",
    powerOnDrag="./CD/MBS_CDPowerOn_S.csv"
)
Event4 = Rocket( #Sustainer Recovery Fins
    motor=motor_empty,
    radius=.156718/2,
    mass=21.069244839778772,
    inertiaI=4.4642384309459455,
    inertiaZ=4.26657314975943,
    distanceRocketNozzle=0.6703693510258891,
    distanceRocketPropellant=0.1571742276764364,
    powerOffDrag="./CD/MBS_CDPowerOff_S.csv",
    powerOnDrag="./CD/MBS_CDPowerOn_S.csv"
)
Event5 = Rocket( #Sustainer Recovery Nose
    motor=motor_empty,
    radius=.156718/2,
    mass=8.558000053476253,
    inertiaI=1,
    inertiaZ=0.07607235823044187,
    distanceRocketNozzle=0,
    distanceRocketPropellant=0,
    powerOffDrag="./CD/MBS_CDPowerOff_S.csv",
    powerOnDrag="./CD/MBS_CDPowerOn_S.csv"
)

Event1.setRailButtons([0.1, -0.2])
Event2.setRailButtons([0.1, -0.2])
Event3.setRailButtons([0.1, -0.2])
Event4.setRailButtons([0.1, -0.2])
Event5.setRailButtons([0.1, -0.2])

NoseCone = Event1.addNose(length=0.9144, kind="ogive", distanceToCM=1.6263591253766445)
#Booster
FinSet = Event1.addFins(4, span=0.1651, rootChord=0.381, tipChord=0.127, distanceToCM=-1.854712428983355)
#Booster
FinSet = Event1.addFins(4, span=0.1651, rootChord=0.381, tipChord=0.127, distanceToCM=0.060026579716645045)
#Booster Recovery

NoseCone = Event2.addNose(length=0.9144, kind="ogive", distanceToCM=0.8940082592125214)

FinSet = Event2.addFins(4, span=0.1651, rootChord=0.381, tipChord=0.127, distanceToCM=-0.6723242864474788)

FinSet = Event3.addFins(4, span=0.1651, rootChord=0.381, tipChord=0.127, distanceToCM=-0.40005962814480733)

FinSet = Event4.addFins(4, span=0.1651, rootChord=0.381, tipChord=0.127, distanceToCM=-0.2893693510258891)
NoseCone = Event5.addNose(length=0.9144, kind="ogive", distanceToCM=0.048802122486610755)


#Sustainer Recovery
# FinSet = Event2.addFins(4, span=0.1651, rootChord=0.381, tipChord=0.127, distanceToCM=-1.255239687)


def drogueTrigger(p, y):
    return True if y[5] < 0 else False

def mainTrigger(p, y):
    return True if y[5] < 0 else False

Event3Main = Event3.addParachute('Main',
                        CdS=.97*np.pi*(0.3048*6/2)**2,
                        trigger=mainTrigger,
                        samplingRate=105,
                        lag=1.5,
                        noise=(0, 8.3, 0.5))
Event4Main = Event4.addParachute('Main',
                        CdS=.97*np.pi*(0.3048*4/2)**2,
                        trigger=mainTrigger,
                        samplingRate=105,
                        lag=1.5,
                        noise=(0, 8.3, 0.5))
Event5Main = Event5.addParachute('Main',
                        CdS=.97*np.pi*(0.3048*6/2)**2,
                        trigger=mainTrigger,
                        samplingRate=105,
                        lag=1.5,
                        noise=(0, 8.3, 0.5))

tsecond_stage = motor1.burnOutTime + 20

booster = Flight(rocket=Event1, environment=Env, inclination=90, heading=0, timeOvershoot = True, maxTime=tsecond_stage)
booster.postProcess()


initial = [x for x in booster.solution if x[0] >= tsecond_stage][0]
initial = [0, *initial[1:]]

sustainer = Flight(rocket=Event2, environment=Env, initialSolution=initial, maxTime=2000, timeOvershoot = True, terminateOnApogee=True)
sustainer.postProcess()

boosterRecovery = Flight(rocket=Event3, environment=Env, initialSolution=initial, timeOvershoot = True)
boosterRecovery.postProcess()

initial = [x for x in sustainer.solution if x[6] > 0][-1]
initial = [0, *initial[1:]]

sustainerRecovery = Flight(rocket=Event4, environment=Env, initialSolution=initial, timeOvershoot = True, maxTime=4000)
sustainerRecovery.postProcess()

noseRecovery = Flight(rocket=Event5, environment=Env, initialSolution=initial, timeOvershoot = True, maxTime=4000)
noseRecovery.postProcess()

print("apogee: ", noseRecovery.apogee)


d1 = (booster.x[:,1], booster.y[:,1], booster.z[:,1])
d2 = (boosterRecovery.x[:,1], boosterRecovery.y[:,1], boosterRecovery.z[:,1])
d3 = (sustainer.x[:,1], sustainer.y[:,1], sustainer.z[:,1])
d4 = (sustainerRecovery.x[:,1], sustainerRecovery.y[:,1], sustainerRecovery.z[:,1])
d5 = (noseRecovery.x[:,1], noseRecovery.y[:,1], noseRecovery.z[:,1])

magic(d1, d2, d3, d4, d5)


