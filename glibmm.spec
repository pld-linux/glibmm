# TODO
# - make clean on -examples (remove .deps) -> & noarch subpackage
#
# Conditional build:
%bcond_without	static_libs	# don't build static library

%define 	glib_ver	1:2.62.0
%define		libsigc_ver	1:2.10.0
Summary:	A C++ interface for glib library
Summary(pl.UTF-8):	Interfejs C++ dla biblioteki glib
Name:		glibmm
Version:	2.62.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glibmm/2.62/%{name}-%{version}.tar.xz
# Source0-md5:	7da228e3f0c6a10024b9a7708c53691e
URL:		https://www.gtkmm.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= %{glib_ver}
BuildRequires:	libsigc++-devel >= %{libsigc_ver}
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2.0
BuildRequires:	m4
BuildRequires:	mm-common >= 0.9.10
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= %{glib_ver}
Requires:	libsigc++ >= %{libsigc_ver}
Obsoletes:	gtkmm-glib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C++ interface for glib library.

%description -l pl.UTF-8
Interfejs C++ dla biblioteki glib.

%package devel
Summary:	Header files for glibmm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki glibmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= %{glib_ver}
Requires:	libsigc++-devel >= %{libsigc_ver}
Requires:	libstdc++-devel >= 6:4.7
Obsoletes:	gtkmm-glib-devel

%description devel
Header files for glibmm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki glibmm.

%package static
Summary:	Static glibmm library
Summary(pl.UTF-8):	Statyczna biblioteka glibmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	gtkmm-glib-static

%description static
Static glibmm library.

%description static -l pl.UTF-8
Statyczna biblioteka glibmm.

%package apidocs
Summary:	Reference documentation for glibmm
Summary(pl.UTF-8):	Szczegółowa dokumentacja dla glibmm
Group:		Documentation
Requires:	gtk-doc-common
Provides:	glibmm-doc
Obsoletes:	glibmm-doc
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Reference documentation for glibmm.

%description apidocs -l pl.UTF-8
Szczegółowa dokumentacja dla glibmm.

%package examples
Summary:	Examples for glibmm
Summary(pl.UTF-8):	Przykłady dla glibmm
Group:		Development/Libraries

%description examples
Examples for glibmm.

%description examples -l pl.UTF-8
Przykłady dla glibmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdocdir=%{_gtkdocdir}/%{name}-2.4 \
	devhelpdir=%{_gtkdocdir}/%{name}-2.4

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__rm} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/Makefile* \
	$RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgiomm-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgiomm-2.4.so.1
%attr(755,root,root) %{_libdir}/libglibmm-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglibmm-2.4.so.1
%attr(755,root,root) %{_libdir}/libglibmm_generate_extra_defs-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglibmm_generate_extra_defs-2.4.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgiomm-2.4.so
%attr(755,root,root) %{_libdir}/libglibmm-2.4.so
%attr(755,root,root) %{_libdir}/libglibmm_generate_extra_defs-2.4.so
%dir %{_libdir}/giomm-2.4
%{_libdir}/giomm-2.4/include
%dir %{_libdir}/glibmm-2.4
%{_libdir}/glibmm-2.4/include
%dir %{_libdir}/glibmm-2.4/proc
%{_libdir}/glibmm-2.4/proc/m4
%{_libdir}/glibmm-2.4/proc/pm
%attr(755,root,root) %{_libdir}/glibmm-2.4/proc/generate_wrap_init.pl
%attr(755,root,root) %{_libdir}/glibmm-2.4/proc/gmmproc
%{_includedir}/giomm-2.4
%{_includedir}/glibmm-2.4
%{_pkgconfigdir}/giomm-2.4.pc
%{_pkgconfigdir}/glibmm-2.4.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgiomm-2.4.a
%{_libdir}/libglibmm-2.4.a
%{_libdir}/libglibmm_generate_extra_defs-2.4.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/glibmm-2.4

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
