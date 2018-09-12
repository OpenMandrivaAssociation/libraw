%define oname LibRaw
%define major 19
%define libname %mklibname raw %{major}
%define libname_r %mklibname raw_r %{major}
%define devname %mklibname raw -d

Summary:	Library for reading and processing of RAW digicam images
Name:		libraw
Version:	0.19.0
Release:	1
License:	GPLv3+
Group:		Development/C
Url:		http://www.libraw.org
Source0:	http://www.libraw.org/data/%{oname}-%{version}.tar.gz
Source1:	http://www.libraw.org/data/%{oname}-demosaic-pack-GPL2-0.18.8.tar.gz
Source2:	http://www.libraw.org/data/%{oname}-demosaic-pack-GPL3-0.18.8.tar.gz
Patch0:		LibRaw-0.6.0-pkgconfig.patch
Patch1:		libraw-0.18.6-compile.patch
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(lcms2)

%description
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc, virtually all RAW formats are
supported).

It pays special attention to correct retrieval of data required for subsequent
RAW conversion.

The library is intended for embedding in RAW converters, data analyzers, and
other programs using RAW files as the initial data.

Since LibRaw is linked against LibRaw-demosaic-pack-GPL2 and
LibRaw-demosaic-pack-GPL3 the global license is GPLv3.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for reading and processing of RAW digicam images
Group:		System/Libraries

%description -n %{libname}
This package contains a shared library for %{name}.

%files -n %{libname}
%{_libdir}/libraw.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libname_r}
Summary:	Library for reading and processing of RAW digicam images
Group:		System/Libraries

%description -n %{libname_r}
This package contains a shared library for %{name}.

%files -n %{libname_r}
%{_libdir}/libraw_r.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	LibRaw development files and headers
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{libname_r} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the development files and headers for %{oname}.

%files -n %{devname}
%doc LICENSE* Changelog.* README README.demosaic-packs html/
%{_includedir}/libraw
%{_libdir}/libraw.so
%{_libdir}/libraw_r.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%package tools
Summary:	Command line tools from %{oname}
Group:		Graphics

%description tools
This packages provides tools to manipulate raw files.

%files tools
%{_bindir}/*

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version} -b1 -b2
%apply_patches

%build
%configure \
    --enable-openmp \
    --enable-jasper \
    --enable-jpeg \
    --enable-lcms \
    --enable-demosaic-pack-gpl2 \
    --enable-demosaic-pack-gpl3

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make

%install
%makeinstall_std

# The source tree has these with execute permissions for some reason
chmod 644 LICENSE.CDDL LICENSE.LGPL

# let files section handle docs
rm -rf %{buildroot}%{_datadir}/doc/*
rm -rf %{buildroot}%{_datadir}/%{name}

# move docs to a better location
mv doc html
