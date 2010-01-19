Summary:	GNOME dialogs for PolicyKit
Summary(pl.UTF-8):	Okna dialogowe GNOME dla pakietu PolicyKit
Name:		polkit-gnome
Version:	0.96
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	611cf39fba2945320fc7a9ec49087e69
URL:		http://people.freedesktop.org/~david/polkit-spec.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gir-repository-devel
BuildRequires:	glibc-misc
BuildRequires:	gnome-common >= 2.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel >= 0.6.2
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.96
Requires:	%{name}-libs = %{version}-%{release}
Requires:	polkit >= 0.96
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
polkit-gnome provides a D-BUS session bus service that is used to
bring up authentication dialogs used for obtaining privileges.

%description -l pl.UTF-8
Pakiet polkit-gnome udostępnia usługę magistrali sesji D-BUS
służącą do wyświetlania okien dialogowych uwierzytelniania w celu
uzyskania uprawnień.

%package libs
Summary:	PolicyKit GNOME libraries
Summary(pl.UTF-8):	Biblioteki PolicyKit dla GNOME
Group:		Libraries

%description libs
PolicyKit GNOME libraries.

%description libs -l pl.UTF-8
Biblioteki PolicyKit dla GNOME.

%package devel
Summary:	PolicyKit header files for GNOME
Summary(pl.UTF-8):	Pliki nagłówkowe PolicyKit dla GNOME
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
PolicyKit header files for GNOME.

%description devel -l pl.UTF-8
Pliki nagłówkowe PolicyKit dla GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang polkit-gnome-1

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f polkit-gnome-1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS TODO
%attr(755,root,root) %{_libexecdir}/polkit-gnome-authentication-agent-1
%{_sysconfdir}/xdg/autostart/polkit-gnome-authentication-agent-1.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-gtk-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolkit-gtk-1.so.0
%{_libdir}/girepository-1.0/PolkitGtk-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-gtk-1.so
%{_libdir}/libpolkit-gtk-1.la
%{_includedir}/polkit-gtk-1
%{_pkgconfigdir}/polkit-gtk-1.pc
%{_datadir}/gir-1.0/PolkitGtk-1.0.gir
