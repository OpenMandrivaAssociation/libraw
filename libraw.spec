# No point in trying to build a debuginfo package since
# the package only has static libraries and find-debuginfo.sh
# does not grok them
%global debug_package %{nil}

Summary: Library for reading RAW files obtained from digital photo cameras
Name: libraw
Version: 0.12.2
Release: %mkrel 1
License: LGPLv2 or CDDL
Group: Development/C
URL: http://www.libraw.org
Source0: http://www.libraw.org/data/LibRaw-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgomp-devel
Buildrequires: lcms-devel

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

%build
%configure2_5x
make

%install
rm -fr %buildroot
%makeinstall_std

# The source tree has these with execute permissions for some reason
chmod 644 LICENSE.CDDL LICENSE.LGPL LICENSE.LibRaw.pdf

rm -fr %buildroot%_datadir/doc/*

%files devel
%defattr(-,root,root,-)
%doc LICENSE.CDDL LICENSE.LGPL COPYRIGHT Changelog.txt Changelog.rus
%doc doc/*
%dir %{_includedir}/libraw
%{_includedir}/libraw/*.h
%{_libdir}/libraw.a
%{_libdir}/libraw_r.a
%{_bindir}/*
%{_libdir}/pkgconfig/*.pc
