import math
import time


def getLocationOfTurtle_m(horizontalPositionOfTurtle,verticalPositionOfTurtle,heightOfTurtle):
    positionOfTurtle_m = [20, 30] # Placeholder
    return positionOfTurtle_m

def getLocationOfVehicle_m(horizontalPositionOfTurtle,verticalPositionOfTurtle,heightOfTurtle):
    positionOfVehicle_m = [0, 10] # Placehoolder
    return positionOfVehicle_m

def getAngleOfVehicleWithRespectToHorizon(TBD):
    pointingAngleOfVehicle_deg = 135 # Placeholder
    return pointingAngleOfVehicle_deg

def moveTowardTurtleLocation(requiredRotationOfVehicle, x_m, y_m):
    while abs(x_m) > 10 or abs(y_m) > 10: # Since there will be a 10m range of accuracy
        # Give power to motors to move forward
        # Determine if within range of an obstacle
        # Go around obstacle if present
        break # currently infinite loop remove when ready
    return 0

def pathfind():
    start_time = time.time()

    x_m = getLocationOfTurtle_m(0,0,0)[0] - getLocationOfVehicle_m(0,0,0)[0]
    y_m = getLocationOfTurtle_m(0,0,0)[1] - getLocationOfVehicle_m(0,0,0)[1]
    angleFromVehicleToTurtle_deg = math.degrees(math.atan(x_m/y_m))

    if x_m < 0: # Happens when turtle is left of vehicle
        angleFromVehicleToTurtle_deg += 180
    if y_m < 0 and x_m > 0: # Happens when turtle is located below and right of vehicle
        angleFromVehicleToTurtle_deg += 360
    requiredRotationOfVehicle = getAngleOfVehicleWithRespectToHorizon(0) - angleFromVehicleToTurtle_deg

    while requiredRotationOfVehicle < 0:
        requiredRotationOfVehicle += 360

    if requiredRotationOfVehicle > 180:
        print('Rotating Counter Clockwise', 360 - requiredRotationOfVehicle, 'degrees')
    else:
        print('Rotating Clockwise', requiredRotationOfVehicle, 'degrees')

    # Insert Rotation here

    print("Time taken to pathfind and rotate %s seconds" % (time.time() - start_time))

    moveTowardTurtleLocation(requiredRotationOfVehicle, x_m, y_m)

    return 0

pathfind()