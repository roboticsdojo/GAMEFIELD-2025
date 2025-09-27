# Step by Step Guide to Launching Your Robot in This World

First make sure you've installed Ignition Gazebo Fortress:

## Installing Ignition Gazebo Fortress

First install some necessary tools:

```bash
sudo apt-get update
sudo apt-get install lsb-release gnupg
```

Then install Ignition Fortress:

```bash
sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
sudo apt-get update
sudo apt-get install ignition-fortress
```

All libraries should be ready to use and the Ignition Gazebo app ready to be executed.

## Uninstalling Binary Install

If you need to uninstall Ignition or switch to a source-based install once you have already installed the library from binaries, run the following command:

```bash
sudo apt remove ignition-fortress && sudo apt autoremove
```

### If You Are Using WSL2

Run the following command on Windows PowerShell as an Administrator:

```bash
wsl --version
```

If not WSL 2, run the following command:

```bash
wsl --upgrade
```

To use **OpenGL Rendering**, enter this command in the WSL2 terminal:

```bash
export LIBGL_ALWAYS_SOFTWARE=1
```

---

More coming soon...

More details on how to spawn your robot with this world.

### To View the World Alone

Run the following command:

```bash
ros2 launch gamefield launch_ign.launch.py
```

### To Spawn the Robot in the Game Field at the Start Position

1. Copy the folder:

   ```
   ./gamefield/sdf
   ```

   into your robot's workspace in the folder:

   ```
   ./src/<your_package>/worlds
   ```

2. Ensure that in the `gamefield.sdf` file (in `./src/<your_package>/worlds`) this line:

   ```xml
   <uri>model://gamefield/sdf/My_GF.dae</uri>
   ```

   and all of its instances change to the relative path of your `My_GF.dae`, i.e.:

   ```xml
   <uri>model://src/<your_package>/worlds/My_GF.dae</uri>
   ```

3. In your `launch_sim.launch.py`, assuming it is Gazebo Ignition Fortress compatible, change the name of the world to `gamefield.sdf`, i.e.:

   ```python
   default_world = os.path.join(get_package_share_directory(package_name), 'worlds', 'gamefield.sdf')
   world = LaunchConfiguration('world')
   world_arg = DeclareLaunchArgument(
       'world', default_value=default_world, description='Path to the world SDF to load'
   )
   ```

4. Build your workspace:

   ```bash
   colcon build --symlink-install
   ```

5. Source your workspace:

   ```bash
   source install/setup.bash
   ```

6. Then to launch the gamefield with the world in it, run:

   ```bash
   ros2 launch <your_package> launch_sim.launch.py
   ```

---

**Heads up:** Ensure that your Gazebo clock is always running when trying to spawn the robot by clicking the play/pause button. A certain order is followed such that Gazebo should start with the world, then the robot spawns, then `joint_broad` starts, followed by `diff_cont`. Implement appropriate timer delays for this sequence to be followed rigidly.

**Note:** These instructions assume that the migration from Gazebo Classic to Ignition Fortress was done, making the robot's URDF compatible or spawnable.
