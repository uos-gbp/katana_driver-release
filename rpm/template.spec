Name:           ros-hydro-katana
Version:        1.0.2
Release:        0%{?dist}
Summary:        ROS katana package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/katana
Source0:        %{name}-%{version}.tar.gz

Requires:       armadillo-devel
Requires:       ros-hydro-actionlib
Requires:       ros-hydro-control-msgs
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-katana-msgs
Requires:       ros-hydro-kni
Requires:       ros-hydro-moveit-msgs
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-roslib
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-srvs
Requires:       ros-hydro-tf
Requires:       ros-hydro-trajectory-msgs
Requires:       ros-hydro-urdf
BuildRequires:  armadillo-devel
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-control-msgs
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-katana-msgs
BuildRequires:  ros-hydro-kni
BuildRequires:  ros-hydro-moveit-msgs
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-srvs
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-trajectory-msgs
BuildRequires:  ros-hydro-urdf

%description
This package provides ROS interfaces to the Neuronics Katana 450 arm. It wraps
the KNI library for low-level communication with the Katana arm.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed May 06 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.2-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.1-0
- Autogenerated by Bloom

* Mon Mar 16 2015 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.0-0
- Autogenerated by Bloom

