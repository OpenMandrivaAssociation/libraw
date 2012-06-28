%define oname	LibRaw

%define major	5
%define libname	%mklibname raw %{major}
%define devname %mklibname raw -d

Summary:	Library for reading and processing of RAW digicam images
Name:		libraw
Version:	0.14.7
Release:	1
License:	GPLv3
Group:		Development/C
URL:		http://www.libraw.org
Source0:	http://www.libraw.org/data/%{oname}-%{version}.tar.gz
Source1:        http://www.libraw.org/data/%{oname}-demosaic-pack-GPL2-%{version}.tar.gz
Source2:        http://www.libraw.org/data/%{oname}-demosaic-pack-GPL3-%{version}.tar.gz
BuildRequires:	libgomp-devel
Buildrequires:	lcms-devel

%description
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc, virtually all RAW formats are
supported).

It pays special attention to correct retrieval of data required for subsequent
RAW conversion.

The library is intended for embedding in RAW converters, data analyzers, and
other programs using RAW files as the initial data.

Since LibRaw is linked against LibRaw-demosaic-pack-GPL2 and
LibRaw-demosaic-pack-GPL3 the global licence is GPLv3.

%package -n %{libname}
Summary:	Library for reading and processing of RAW digicam images
Group:		System/Libraries

%description -n %{libname}
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc, virtually all RAW formats are
supported).

It pays special attention to correct retrieval of data required for subsequent
RAW conversion.

The library is intended for embedding in RAW converters, data analyzers, and
other programs using RAW files as the initial data.

Since LibRaw is linked against LibRaw-demosaic-pack-GPL2 and
LibRaw-demosaic-pack-GPL3 the global licence is GPLv3.

%package -n %{devname}
Summary:	LibRaw development files and headers
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < 0.13.4

%description -n %{devname}
This package contains the development files and headers for %{oname}.

%package tools
Summary:	Command line tools from %{oname}
Group:		Graphics

%description tools
This packages provides tools to manipulate raw files.

%prep
%setup -qn %{oname}-%{version} -b1 -b2

%build
%configure2_5x --disable-openmp --disable-static
#parallel build tends to broke build
make -j2

%install
%makeinstall_std

# The source tree has these with execute permissions for some reason
chmod 644 LICENSE.CDDL LICENSE.LGPL LICENSE.LibRaw.pdf

# let files section handle docs
rm -rf %{buildroot}%{_datadir}/doc/*

# move docs to a better location
mv doc html

%files tools
%{_bindir}/*

%files -n %{libname}
%doc LICENSE* README README.demosaic-packs
%{_libdir}/libraw.so.%{major}*
%{_libdir}/libraw_r.so.%{major}*

%files -n %{devname}
%doc LICENSE* Changelog.* README README.demosaic-packs html/
%{_includedir}/libraw
%{_libdir}/libraw.so
%{_libdir}/libraw_r.so
%{_libdir}/pkgconfig/*.pc
