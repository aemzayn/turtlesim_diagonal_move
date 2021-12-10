# Moving diagonally in turtlesim using ROSPY

The reason I created this repository is I had a really hard time figuring out how to move a turtlesim sideways without rotating the turtlesim. Unfortunately, there is not quite a lot of source to learn it.

## How to use
1. Clone or download this project to your catkin workspace src folder
    ```
    cd ~/catkin_ws/src
    git clone https://github.com/aemzayn/turtlesim_diagonal_move.git
    cd ~/catkin_ws && catkin_make
    ```
2. Run `roscore` in separate terminal
3. Run turtlesim in another terminal 
    ```
    rosrun turtlesim_diagonal_move move.py
    ```
4. Enter the `direction` and `angle`

