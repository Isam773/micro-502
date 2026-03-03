import numpy as np

# Create a rotation matrix from the world frame to the body frame using euler angles
def euler2rotmat(euler_angles):

    R = np.eye(3)

    # Here you need to implement the rotation matrix
    # First calculate the rotation matrix for each angle (roll, pitch, yaw)
    # Then multiply the matrices together to get the total rotation matrix
    # Inputs:
    #           euler_angles: A list of 3 Euler angles [roll, pitch, yaw] in radians
    # Outputs:
    #           R: A 3x3 numpy array that represents the rotation matrix of the euler angles

    # --- YOUR CODE HERE ---

    R_roll = np.array([
        [1, 0, 0],
        [0, np.cos(euler_angles[0]), -np.sin(euler_angles[0])],
        [0, np.sin(euler_angles[0]), np.cos(euler_angles[0])]
    ])
    R_pitch = np.array([
        [np.cos(euler_angles[1]), 0, np.sin(euler_angles[0])],
        [0, 1, 0],
        [-np.sin(euler_angles[0]), 0, np.cos(euler_angles[1])]
    ])
    R_yaw = np.array([
        [np.cos(euler_angles[2]), -np.sin(euler_angles[0]), 0],
        [-np.sin(euler_angles[0]), np.cos(euler_angles[1]), 0],
        [0, 0, 1]
    ])

    R = R_yaw @ R_pitch @ R_roll
    return R


# Rotate the control commands from the inertial reference frame to the body reference frame
def rot_inertial2body(control_commands, euler_angles, quaternion):

    # Here you need to rotate the control commands from the inertial reference frame to the body reference frame
    # You should use the euler2rotmat function to get the rotation matrix
    # Keep in mind that you only want to rotate the velocity commands, which are the first two elements of the control_commands array
    # Think carefully about which direction you need to perform the rotation

    # Inputs:
    #           control_commands: A list of 4 control commands [vel_x, vel_y, altitude, yaw_rate] in the inertial reference frame
    #           euler_angles: A list of 3 Euler angles [roll, pitch, yaw] in radians
    #           quaternion: A list of 4 elements [x, y, z, w] representing the quaternion of the drone
    # Outputs:
    #           control_commands: A list of 4 control commands [vel_x, vel_y, altitude, yaw_rate] in the body reference frame

    # --- YOUR CODE HERE ---
    vel_inertial = np.zeros(3)
    vel_inertial[0:2] = control_commands[0:2]
    R = euler2rotmat(euler_angles)
    vel_body = R.T @ vel_inertial
    #print("before", control_commands)
    control_commands[0:2] = vel_body[0:2]
    #print("after", control_commands)

    return control_commands