# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	A C++ interface for glib library
Summary(pl):	Interfejs C++ dla biblioteki glib
Name:		glibmm
Version:	2.9.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glibmm/2.9/%{name}-%{version}.tar.bz2
# Source0-md5:	1344e815a2cd20ff189563d510609c3d
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.6.3
BuildRequires:	libsigc++-devel >= 1:2.0.10
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
Obsoletes:	gtkmm-glib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C++ interface for glib library.

%description -l pl
Interfejs C++ dla biblioteki glib.

%package devel
Summary:	Header files for glibmm library
Summary(pl):	Pliki nag³ówkowe biblioteki glibmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.6.3
Requires:	libsigc++-devel >= 1:2.0.10
Requires:	libstdc++-devel
Obsoletes:	gtkmm-glib-devel

%description devel
Header files for glibmm library.

%description devel -l pl
Pliki nag³ówkowe biblioteki glibmm.

%package doc
Summary:	Reference documentation and examples for glibmm
Summary(pl):	Szczegó³owa dokumentacja i przyk³ady dla glibmm
Group:		Documentation

%description doc
Reference documentation and examples for glibmm.

%description doc -l pl
Szczegó³owa dokumentacja i przyk³ady dla glibmm.

%package static
Summary:	Static glibmm library
Summary(pl):	Statyczna biblioteka glibmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	gtkmm-glib-static

%description static
Static glibmm library.

%description static -l pl
Statyczna biblioteka glibmm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--enable-fulldocs \
	--enable-static \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gtkmm_docdir=%{_gtkdocdir}/%{name}-2.4 \
	glibmm_docdir=%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CHANGES NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_libdir}/%{name}-2.4
%{_libdir}/%{name}-2.4/include
%dir %{_libdir}/%{name}-2.4/proc
%{_libdir}/%{name}-2.4/proc/m4
%{_libdir}/%{name}-2.4/proc/pm
%attr(755,root,root) %{_libdir}/%{name}-2.4/proc/gmmproc
%attr(755,root,root) %{_libdir}/%{name}-2.4/proc/*.pl
%{_includedir}/%{name}-2.4
%{_pkgconfigdir}/*.pc
%{_aclocaldir}/*.m4

%files doc
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}-2.4
%{_examplesdir}/%{name}-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
