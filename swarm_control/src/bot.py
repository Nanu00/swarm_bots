import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class Bot():
    def __init__(self, id):
        self.id = id

        self.odom = Odometry()
        self.vel = Twist()

        self.pub = rospy.Publisher('bot'+str(self.id)+'/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('bot'+str(self.id)+'/odom', Odometry, self.odom_update)
        self.sub = rospy.Subscriber('bot'+str(self.id)+'/cmd_vel', Twist, self.cmd_vel_update)

    def odom_update(self, odom):
        self.odom = odom

    def cmd_vel_update(self, vel):
        self.vel = vel
