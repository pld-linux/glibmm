Summary:	A C++ interface for glib library
Summary(pl):	Interfejs C++ dla biblioteki glib
Name:		glibmm
Version:	2.3.7
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	1b265f1c2c87dd835e598facd1b37371
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	glib2-devel >= 2.3.6
Buildrequires:	libsigc++-devel >= 1.9.15
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
Requires:	glib2-devel >= 2.3.6
Requires:	libsigc++-devel >= 1.9.15
Requires:	libstdc++-devel
Obsoletes:	gtkmm-glib-devel

%description devel
Header files for glibmm library.

%description devel -l pl
Pliki nag³ówkowe biblioteki glibmm.

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
%configure \
	--enable-fulldocs \
	--enable-static

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
%doc %{_gtkdocdir}/%{name}-2.4
%doc %{_examplesdir}/%{name}-%{version}
%{_libdir}/lib*.la
%dir %{_libdir}/%{name}-2.3
%{_libdir}/%{name}-2.3/include
%dir %{_libdir}/%{name}-2.3/proc
%{_libdir}/%{name}-2.3/proc/m4
%{_libdir}/%{name}-2.3/proc/pm
%attr(755,root,root) %{_libdir}/%{name}-2.3/proc/gmmproc
%attr(755,root,root) %{_libdir}/%{name}-2.3/proc/*.pl
%{_includedir}/%{name}-2.3
%{_pkgconfigdir}/*.pc
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
