import rospy
from geometry_msgs.msg import Twist
from math import sin, cos
PI = 3.1415926535897

class Turtle:
    def __init__(self):
        rospy.init_node('sliding_turtle', anonymous=True)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self._rate = rospy.Rate(10)
        self._speed = 15

    def degrees2radians(self, angle):
        return angle * PI / 180

    def move(self):
        tw = Twist()

        distance = float(input('Enter distance: '))
        angle = float(input('Enter angle in degree: '))

        tw.linear.x = abs(self._speed) * cos(self.degrees2radians(angle))
        tw.linear.y = abs(self._speed) * sin(self.degrees2radians(angle))

        if not rospy.is_shutdown():
            t0 = float(rospy.Time.now().to_sec())
            current_distance = 0.0

            while current_distance < distance:
                self.pub.publish(tw)
                t1 = float(rospy.Time.now().to_sec())
                current_distance = float(self._speed * (t1 - t0))
            # Reset linear velocity to 0 after reach the distance
            tw.linear.x = 0
            tw.linear.y = 0
            self.pub.publish(tw)

if __name__ == '__main__':
    try:
        turtle = Turtle()
        turtle.move()
    except rospy.ROSInterruptException:
        pass

