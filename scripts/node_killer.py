#!/usr/bin/env python3

import rospy
import subprocess

def main():
    rospy.init_node("node_killer", anonymous=True)
    
    node_to_kill = "/joy_teleop/joy_node"

    rospy.loginfo(f"Killing node: {node_to_kill}")
    subprocess.run(["rosnode", "kill", node_to_kill])

if __name__ == "__main__":
    main()
