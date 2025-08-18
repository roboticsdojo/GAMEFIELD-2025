# Step by Step guide to launching your robot in this world
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

All libraries should be ready to use and the ign gazebo app ready to be executed.


## Uninstalling binary install
If you need to uninstall Ignition or switch to a source-based install once you have already installed the library from binaries, run the following command:
```bash
sudo apt remove ignition-fortress && sudo apt autoremove
```

### If you are using WSL2
Run the following command on Windows Powershell as an Administrator:

```bash
wsl --version
```
If not WSL 2, run the following command:
```bash
wsl --upgrade
```
To use OPENGL Rendering, enter this command in WSL2 terminal:
```bash
 export LIBGL_ALWAYS_SOFTWARE=1
 ```
 
More coming soon...