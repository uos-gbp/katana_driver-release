Name:           ros-lunar-katana-moveit-ikfast-plugin
Version:        1.1.1
Release:        0%{?dist}
Summary:        ROS katana_moveit_ikfast_plugin package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/katana_moveit_ikfast_plugin
Source0:        %{name}-%{version}.tar.gz

Requires:       lapack-devel
Requires:       ros-lunar-moveit-core
Requires:       ros-lunar-pluginlib
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-tf-conversions
BuildRequires:  lapack-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-moveit-core
BuildRequires:  ros-lunar-pluginlib
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-tf-conversions

%description
The katana_moveit_ikfast_plugin package

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
* Fri May 26 2017 Martin Günther <mguenthe@uos.de> - 1.1.1-0
- Autogenerated by Bloom

* Fri May 26 2017 Martin Günther <mguenthe@uos.de> - 1.1.0-0
- Autogenerated by Bloom

* Wed May 24 2017 Martin Günther <mguenthe@uos.de> - 1.0.7-0
- Autogenerated by Bloom

