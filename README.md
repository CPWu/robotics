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

### CortextNanoBridge (/CortextNanoBridge)
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