Name:           ros-kinetic-katana-driver
Version:        1.0.6
Release:        0%{?dist}
Summary:        ROS katana_driver package

Group:          Development/Libraries
License:        BSD, GPL
URL:            http://ros.org/wiki/katana_driver
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-katana
Requires:       ros-kinetic-katana-arm-gazebo
Requires:       ros-kinetic-katana-description
Requires:       ros-kinetic-katana-gazebo-plugins
Requires:       ros-kinetic-katana-moveit-ikfast-plugin
Requires:       ros-kinetic-katana-msgs
Requires:       ros-kinetic-katana-teleop
Requires:       ros-kinetic-katana-tutorials
Requires:       ros-kinetic-kni
BuildRequires:  ros-kinetic-catkin

%description
This stack contains all descriptions, drivers and bringup facilities for
Neuronics Katana 450 arm.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Jan 28 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.6-0
- Autogenerated by Bloom

