# Robotics

AI/ML with robotics

## Bill of Materials
TBD

## Stuff Used
- Cortano
- CortanoNanoBridge
- OpenCV
- etc.

## Session #1 (Structure, Motion, Communication)
- Chassis
- Motors
- Gears
- Power
- Joints
- End Effectors
- Communication (Python)

## Session #2 Neural Networks, Object Recognition, Depth Processing
- Neural Network Purpose
- Neural Network 'Learning'
- Neural Network Data Constraints
- Camera Input
- Object Recognition (ML)
- Depth Extraction

## Session #3 Motion Control, Joint Control
- ICP 
- Motion Tracking
- Depth Projections
- Gridmap Construction
  
## Session #4 Positioning, Object Tracking, Collision Mapping
- Objective-oriented Thinking
- Breadth First Search
- A*
- Utility (State-Action)
- Decision Graph Construction
- MDPs
- Q-Learning (ML)

## Submodules
Cortano & CortanoNanoBridge by Timothy Young

## Guide

### PyRealSense
> Install PyRealSense
>> - Install [PyRealSense2](https://drive.google.com/file/d/1Fw8zVV-cP5c9xpp-JplMKnJGe5nVNNaY/view?usp=drive_link) onto the Jetson Nano `./PyRealSense` (Jetson Nano Python3.6 cu10.2)
>> - Attach the RealSense camera to the Jetson Nano and try running the RealSense Viewer to ensure it works in USB 3.2 mode.

```
chmod +x install.sh
sudo ./install.sh
cd /usr/local/bin
sudo chmod +x ./realsense-viewer
./realsense-viewer
```

### RobotC (Vex MicroController)
> Install RobotC
>> - Download RobotC from [VexRobotics](https://www.vexrobotics.com/robotc-vexedr-vexiq.html)
>> - Set the board to Vex 2.0 Cortext (Robot -> Platform Type -> -> Vex 2.0 Cortex)
>> - Change the Vex Cortext Communication Mode to USB Only

### CortexNanoBridge (/CortexNanoBridge)
> Setup CortexNanoBridge on Jetson Nano
>> - Navigate to Jetson Nano Folder `cd ../CortextNanoBridge/jetson_nano`
>> - Make the install file executable `chmod +x install.sh`
>> - Install CortextNanoBridge onto the Jetson Nano `./install.sh`
>> - Reboot the Jetson Nano `sudo reboot`

### Cortano (/Cortano)
> Setup Cortano on Computer Controller
>> - Navigate to ./Cortano and run `python3 -m pip install .` to install the API
>> - Note the IP Address of the Jetson Nano
>> - Use robot.py, `python3 robot.py` but ensure that the IP Address specified is Jetson's IP Address `ifconfig`

## Contact
Chun Wu - [TheChunWu](https://twitter.com/TheChunWu)