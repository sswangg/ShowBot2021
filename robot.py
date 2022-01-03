import wpilib
import config


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        CONTROLLER_PORT = config.gamepad_port
        SPARK_MAX_CHANNEL = config.motor_controller_channel

        self.LEFT_TRIGGER_AXIS = config.left_trigger_axis
        self.RIGHT_TRIGGER_AXIS = config.right_trigger_axis
        self.A_BUTTON_NUM = config.a_button_num
        self.B_BUTTON_NUM = config.b_button_num
        self.X_BUTTON_NUM = config.x_button_num
        self.Y_BUTTON_NUM = config.y_button_num
        
        self.spark_max = wpilib.Spark(SPARK_MAX_CHANNEL)
        self.controller = wpilib.XboxController(CONTROLLER_PORT)

    def teleopPeriodic(self):
        """ Makes a motor spin using the SPARK MAX motor controller

        Holding down the right trigger makes the motor go forwards at full speed and holding down the left trigger makes
        the motor go backwards at 20% speed. The speed set by holding down one of the triggers can then be modified by
        holding a button down. Holding x reduces the speed to 80% of what was set by the trigger. Holding y reduces it
        to 60%, b reduces it to 40%, and a reduces it to 20%.
        """
        if self.controller.getRawAxis(self.RIGHT_TRIGGER_AXIS) > 0.95:
            self.running = 1
        elif self.controller.getRawAxis(self.LEFT_TRIGGER_AXIS) > 0.95:
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
