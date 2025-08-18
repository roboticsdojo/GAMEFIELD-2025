from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    package_name = 'gamefield'
    sdf_file = os.path.join(
        get_package_share_directory(package_name),
        'sdf',
        'gamefield.sdf'
    )

    return LaunchDescription([
        # Environment vars for Ignition rendering
        SetEnvironmentVariable('LIBGL_ALWAYS_SOFTWARE', '1'),
        SetEnvironmentVariable('MESA_GL_VERSION_OVERRIDE', '3.3'),
        SetEnvironmentVariable('MESA_GLSL_VERSION_OVERRIDE', '330'),
        SetEnvironmentVariable('IGN_RENDERING_ENGINE_PATH', '/usr/lib/x86_64-linux-gnu/ign-rendering-6/engine-plugins'),
        SetEnvironmentVariable('IGN_RENDERING_ENGINE', 'ogre2'),
        SetEnvironmentVariable('DISPLAY', ':0'),
        SetEnvironmentVariable('QT_X11_NO_MITSHM', '1'),

        # Launch Ignition Gazebo with your sdf file
        ExecuteProcess(
            cmd=['ign', 'gazebo', sdf_file],
            output='screen'
        )
    ])