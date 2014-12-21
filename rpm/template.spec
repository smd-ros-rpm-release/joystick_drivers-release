Name:           ros-indigo-spacenav-node
Version:        1.10.0
Release:        0%{?dist}
Summary:        ROS spacenav_node package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/spacenav_node
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       libX11-devel
Requires:       libspnav-devel
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       spacenavd
BuildRequires:  libX11-devel
BuildRequires:  libspnav-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
ROS interface to the 3Dconnexion SpaceNavigator 6DOF joystick.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Jonathan Bohren <jbo@jhu.edu> - 1.10.0-0
- Autogenerated by Bloom

