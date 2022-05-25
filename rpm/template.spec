%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-dwb-msgs
Version:        1.0.12
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS dwb_msgs package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-builtin-interfaces
Requires:       ros-galactic-geometry-msgs
Requires:       ros-galactic-nav-2d-msgs
Requires:       ros-galactic-nav-msgs
Requires:       ros-galactic-rosidl-default-runtime
Requires:       ros-galactic-std-msgs
Requires:       ros-galactic-ros-workspace
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-builtin-interfaces
BuildRequires:  ros-galactic-geometry-msgs
BuildRequires:  ros-galactic-nav-2d-msgs
BuildRequires:  ros-galactic-nav-msgs
BuildRequires:  ros-galactic-rosidl-default-runtime
BuildRequires:  ros-galactic-std-msgs
BuildRequires:  ros-galactic-ros-workspace
BuildRequires:  ros-galactic-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-galactic-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-galactic-rosidl-interface-packages(member)

%if 0%{?with_weak_deps}
Supplements:    ros-galactic-rosidl-interface-packages(all)
%endif

%description
Message/Service definitions specifically for the dwb_core

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
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
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Wed May 25 2022 David V. Lu!! <davidvlu@gmail.com> - 1.0.12-1
- Autogenerated by Bloom

* Thu May 12 2022 David V. Lu!! <davidvlu@gmail.com> - 1.0.11-1
- Autogenerated by Bloom

* Mon May 09 2022 David V. Lu!! <davidvlu@gmail.com> - 1.0.10-1
- Autogenerated by Bloom

* Fri May 06 2022 David V. Lu!! <davidvlu@gmail.com> - 1.0.9-1
- Autogenerated by Bloom

