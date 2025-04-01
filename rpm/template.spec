%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-nav2-system-tests
Version:        1.3.5
Release:        4%{?dist}%{?release_suffix}
Summary:        ROS nav2_system_tests package

License:        Apache-2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       lcov
Requires:       ros-jazzy-geometry-msgs
Requires:       ros-jazzy-launch-ros
Requires:       ros-jazzy-launch-testing
Requires:       ros-jazzy-nav-msgs
Requires:       ros-jazzy-nav2-amcl
Requires:       ros-jazzy-nav2-behavior-tree
Requires:       ros-jazzy-nav2-bringup
Requires:       ros-jazzy-nav2-lifecycle-manager
Requires:       ros-jazzy-nav2-map-server
Requires:       ros-jazzy-nav2-minimal-tb3-sim
Requires:       ros-jazzy-nav2-msgs
Requires:       ros-jazzy-nav2-navfn-planner
Requires:       ros-jazzy-nav2-planner
Requires:       ros-jazzy-nav2-util
Requires:       ros-jazzy-navigation2
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclpy
Requires:       ros-jazzy-robot-state-publisher
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-tf2-geometry-msgs
Requires:       ros-jazzy-visualization-msgs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-launch-ros
BuildRequires:  ros-jazzy-launch-testing
BuildRequires:  ros-jazzy-nav-msgs
BuildRequires:  ros-jazzy-nav2-amcl
BuildRequires:  ros-jazzy-nav2-behavior-tree
BuildRequires:  ros-jazzy-nav2-common
BuildRequires:  ros-jazzy-nav2-lifecycle-manager
BuildRequires:  ros-jazzy-nav2-map-server
BuildRequires:  ros-jazzy-nav2-minimal-tb3-sim
BuildRequires:  ros-jazzy-nav2-msgs
BuildRequires:  ros-jazzy-nav2-navfn-planner
BuildRequires:  ros-jazzy-nav2-planner
BuildRequires:  ros-jazzy-nav2-util
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclpy
BuildRequires:  ros-jazzy-std-msgs
BuildRequires:  ros-jazzy-tf2-geometry-msgs
BuildRequires:  ros-jazzy-visualization-msgs
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python3-zmq
BuildRequires:  ros-jazzy-ament-cmake-gtest
BuildRequires:  ros-jazzy-ament-cmake-pytest
BuildRequires:  ros-jazzy-ament-lint-auto
BuildRequires:  ros-jazzy-ament-lint-common
BuildRequires:  ros-jazzy-launch
%endif

%description
A sets of system-level tests for Nav2 usually involving full robot simulation

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Tue Apr 01 2025 Carlos Orduno <carlos.a.orduno@intel.com> - 1.3.5-4
- Autogenerated by Bloom

* Sun Mar 30 2025 Carlos Orduno <carlos.a.orduno@intel.com> - 1.3.5-3
- Autogenerated by Bloom

* Sat Mar 22 2025 Carlos Orduno <carlos.a.orduno@intel.com> - 1.3.5-2
- Autogenerated by Bloom

* Wed Mar 05 2025 Carlos Orduno <carlos.a.orduno@intel.com> - 1.3.5-1
- Autogenerated by Bloom

* Thu Dec 19 2024 Carlos Orduno <carlos.a.orduno@intel.com> - 1.3.4-1
- Autogenerated by Bloom

