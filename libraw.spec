# No point in trying to build a debuginfo package since
# the package only has static libraries and find-debuginfo.sh
# does not grok them
%global debug_package %{nil}

Summary: Library for reading RAW files obtained from digital photo cameras
Name: libraw
Version: 0.10.0
Release: %mkrel 1
License: LGPLv2 or CDDL
Group: Development/C
URL: http://www.libraw.org
Source0: http://www.libraw.org/data/LibRaw-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
# Configuration support. Patch sent upstream
Patch0: LibRaw-0.9.1-configure.patch
# Use optflags for build
Patch1: LibRaw-0.9.1-configure-optflags.patch
# Don't impose -O4 and -w
Patch2: LibRaw-0.9.1-configure-default-cflags.patch

%description
LibRaw is a library for reading RAW files obtained from digital photo
cameras (CRW/CR2, NEF, RAF, DNG, and others).

LibRaw is based on the source codes of the dcraw utility, where part of
drawbacks have already been eliminated and part will be fixed in future.

%package devel
Provides: %name-static-devel = %{version}-%{release}
Summary: LibRaw development libraries
Group: Development/C

%description devel
LibRaw development libraries

This package contains static libraries that applications can use to build
against LibRaw. LibRaw does not provide dynamic libraries.

%prep
%setup -qn LibRaw-%{version}
%patch0 -p1 -b .configure
%patch1 -p1 -b .configure-optflags
%patch2 -p1 -b .configure-default-cflags

%build
# This is not the autotools generated configure script
CFLAGS="%{optflags}" sh configure -P %{_prefix}
%make

%install
rm -fr %buildroot
cp -pr doc manual

# The source tree has these with execute permissions for some reason
chmod 644 LICENSE.CDDL LICENSE.LGPL LICENSE.LibRaw.pdf

# The Libraries
%makeinstall_std LIBDIR=%{_lib}

%files devel
%defattr(-,root,root,-)
%doc LICENSE.CDDL LICENSE.LGPL COPYRIGHT Changelog.txt Changelog.rus
%doc manual
%dir %{_includedir}/libraw
%{_includedir}/libraw/*.h
%{_libdir}/libraw.a
%{_libdir}/libraw_r.a
