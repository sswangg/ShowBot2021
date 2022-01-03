# SPARK MAX Tester
Python program to help you test that shiny new SPARK MAX motor controller.

## Setup
### Required parts
- SPARK MAX motor controller
- Xbox Controller or other game controller
- RoboRIO
- Motor
- Computer
- Wires

I'm not sure how the wiring and setup works, ask electrical. However, as long as the Xbox Controller is plugged into the
computer, simulations will work.

## Installing and Running
Clone the repository onto your machine.
```bash
git clone https://github.com/sswangg/spark-max-tester.git
```

### Installing requirements
If you have not already, install RobotPy following these 
[instructions](https://robotpy.readthedocs.io/en/stable/install/computer.html) in the RobotPy documentation.

Tip: Use a [venv](https://docs.python.org/3/library/venv.html), especially if you need a newer version of pip 
(for linux). Also note that python 3.10 is not supported by RobotPy.

### Running a simulation
Running a simulation is a good way to verify that the code all works as intended. Start a simulation on macOS and Linux
using:
```bash
python3 robot.py sim
```
Or if you're on Windows:
```bash
py -3 robot.py sim
```
Your simulation should look something like this. Note that the widgets have been rearranged for compactness and 
aesthetics.
![A bunch of grey rectangles with white text](https://i.imgur.com/bFPXAoz.png)
If needed, drag the gamepad you'd like to use from the System Joysticks widget to Joysticks[0] in the joysticks widget.
Then switch the robot state from disabled to teleoperated and use the drop-down list in the NetworkTables widget to find
the simulated SPARK MAX.
![A drop-down list with "Ungrouped" and "Spark[1]" opened](https://i.imgur.com/TTLZRGu.png)
That's it! You can now control your motor controller and change the number next to "Value"

### Deploying to the robot
Deploy the code and test using actual hardware on a computer connected to the roboRIO. If you're on macOS or Linux:
```bash
python3 robot.py deploy
```
Or if you're on Windows:
```bash
py -3 robot.py deploy
```

## Controls
Either the right trigger or the left trigger must be held down for the motor controller to output a non-zero value.

- Right trigger: 1 (full speed forwards)
- Left trigger: -0.2 (1/5 speed backwards)

The speed (but not the direction) can then be modified by pressing one of the ABXY buttons.

- X: 0.8 speed multiplier
- Y: 0.6 speed multiplier
- B: 0.4 speed multiplier
- A: 0.2 speed multiplier

Note: These controls can be configured. The right and left triggers can be any axis, and the ABXY buttons can be any 
buttons.

If multiple buttons/axis are pressed/held, then backwards takes precendence over forwards, and lower speed multipliers 
take precedence over higher ones.

## Config
You can configure what port your gamepad is on, which axis and buttons it uses, and what channel the SPARK MAX is on.
Just change the values in config.py! Just note that button numbers start from 1 and not 0.
