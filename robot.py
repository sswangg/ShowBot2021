import wpilib


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        CONTROLLER_PORT = 0  # USB port the controller is connected to, usually 0
        SPARK_MAX_CHANNEL = 1  # The channel the motor controller is on
        
        self.spark_max = wpilib.Spark(SPARK_MAX_CHANNEL)
        self.controller = wpilib.XboxController(CONTROLLER_PORT)

        # Change these depending on the controller
        self.left_trigger_axis = 2 
        self.right_trigger_axis = 5

    def teleopPeriodic(self):
        """ Makes a motor spin using the SPARK MAX motor controller

        Holding down the right trigger makes the motor go forwards at full speed and holding down the left trigger makes
        the motor go backwards at 20% speed. The speed set by holding down one of the triggers can then be modified by
        holding a button down. Holding x reduces the speed to 80% of what was set by the trigger. Holding y reduces it
        to 60%, b reduces it to 40%, and a reduces it to 20%.
        """
        if self.controller.getRawAxis(self.right_trigger_axis) > 0.95:
            self.running = 1
        elif self.controller.getRawAxis(self.left_trigger_axis) > 0.95:
            self.running = -0.2
        else:
            self.running = 0 

        if self.controller.getAButton():
            self.shooter_mod = 0.2
        elif self.controller.getBButton():
            self.shooter_mod = 0.4
        elif self.controller.getYButton():
            self.shooter_mod = 0.6
        elif self.controller.getXButton():
            self.shooter_mod = 0.8
        else:
            self.shooter_mod = 1

        self.spark_max.set(self.running * self.shooter_mod)


if __name__ == "__main__":
    wpilib.run(MyRobot)
