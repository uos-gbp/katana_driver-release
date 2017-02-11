Name:           ros-indigo-katana-arm-gazebo
Version:        1.0.7
Release:        0%{?dist}
Summary:        ROS katana_arm_gazebo package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/katana_arm_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-controller-manager-msgs
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-joint-trajectory-controller
Requires:       ros-indigo-katana-description
Requires:       ros-indigo-katana-gazebo-plugins
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-urdf
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-controller-manager-msgs
BuildRequires:  ros-indigo-gazebo-ros
BuildRequires:  ros-indigo-joint-trajectory-controller
BuildRequires:  ros-indigo-katana-description
BuildRequires:  ros-indigo-katana-gazebo-plugins
BuildRequires:  ros-indigo-robot-state-publisher
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-urdf
BuildRequires:  ros-indigo-xacro

%description
This package starts a Neuronics Katana robot arm in the Gazebo simulation
environment. It is modeled after the pr2_arm_gazebo package by John Hsu.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Feb 11 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.7-0
- Autogenerated by Bloom

* Fri Jan 27 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.6-0
- Autogenerated by Bloom

* Tue Apr 12 2016 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.5-0
- Autogenerated by Bloom

* Mon Apr 11 2016 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.4-0
- Autogenerated by Bloom

* Mon Jun 29 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.3-0
- Autogenerated by Bloom

* Wed May 06 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.2-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.1-0
- Autogenerated by Bloom

* Mon Mar 16 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.0-0
- Autogenerated by Bloom

