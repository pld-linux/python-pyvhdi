# see m4/${libname}.m4 />= for required version of particular library
%define		libbfio_ver		20201125
%define		libcdata_ver		20220115
%define		libcerror_ver		20120425
%define		libcfile_ver		20160409
%define		libclocale_ver		20120425
%define		libcnotify_ver		20120425
%define		libcpath_ver		20180716
%define		libcsplit_ver		20120701
%define		libcthreads_ver		20160404
%define		libfcache_ver		20191109
%define		libfdata_ver		20201129
%define		libfguid_ver		20120426
%define		libuna_ver		20210801
Summary:	Python 2 bindings for libvhdi library
Summary(pl.UTF-8):	Wiązania Pythona 2 do biblioteki libvhdi
Name:		python-pyvhdi
Version:	20221124
Release:	2
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://github.com/libyal/libvhdi/releases
Source0:	https://github.com/libyal/libvhdi/releases/download/%{version}/libvhdi-alpha-%{version}.tar.gz
# Source0-md5:	1d45d0b78dcf2244758e05d694990d45
URL:		https://github.com/libyal/libvhdi/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libbfio-devel >= %{libbfio_ver}
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libfcache-devel >= %{libfcache_ver}
BuildRequires:	libfdata-devel >= %{libfdata_ver}
BuildRequires:	libfguid-devel >= %{libfguid_ver}
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	python-devel >= 1:2.5
Requires:	libbfio >= %{libbfio_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libfguid >= %{libfguid_ver}
Requires:	libvhdi >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for libvhdi library.

%description -l pl.UTF-8
Wiązania Pythona 2 do biblioteki libvhdi.

%prep
%setup -q -n libvhdi-%{version}

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-python2 \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# keep only python2 module
%{__rm} $RPM_BUILD_ROOT%{_bindir}/vhdi*
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/libvhdi*
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvhdi.*
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/libvhdi.pc
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/man[13]

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pyvhdi.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{py_sitedir}/pyvhdi.so
