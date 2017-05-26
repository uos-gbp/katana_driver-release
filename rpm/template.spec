Name:           ros-lunar-katana-description
Version:        1.1.1
Release:        0%{?dist}
Summary:        ROS katana_description package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/katana_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-transmission-interface
Requires:       ros-lunar-urdf
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-convex-decomposition
BuildRequires:  ros-lunar-ivcon
BuildRequires:  ros-lunar-transmission-interface
BuildRequires:  ros-lunar-urdf

%description
This package contains an URDF description of the Katana arm and all supporting
mesh files.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri May 26 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.1.1-0
- Autogenerated by Bloom

* Fri May 26 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.1.0-0
- Autogenerated by Bloom

* Wed May 24 2017 Martin Günther <mguenthe@uni-osnabrueck.de> - 1.0.7-0
- Autogenerated by Bloom

