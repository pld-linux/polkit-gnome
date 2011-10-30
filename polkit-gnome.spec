Summary:	GNOME dialogs for PolicyKit
Summary(pl.UTF-8):	Okna dialogowe GNOME dla pakietu PolicyKit
Name:		polkit-gnome
Version:	0.105
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/polkit-gnome/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	50ecad37c8342fb4a52f590db7530621
URL:		http://hal.freedesktop.org/docs/PolicyKit-gnome/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	glibc-misc
BuildRequires:	gnome-common >= 2.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.99
Requires:	glib2 >= 1:2.30.0
Requires:	polkit >= 0.99
Obsoletes:	PolicyKit-gnome
Obsoletes:	polkit-gnome-devel < 0.103
Obsoletes:	polkit-gnome-libs < 0.103
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
polkit-gnome provides a D-BUS session bus service that is used to
bring up authentication dialogs used for obtaining privileges.

%description -l pl.UTF-8
Pakiet polkit-gnome udostępnia usługę magistrali sesji D-BUS służącą
do wyświetlania okien dialogowych uwierzytelniania w celu uzyskania
uprawnień.

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
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang polkit-gnome-1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f polkit-gnome-1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS TODO
%attr(755,root,root) %{_libexecdir}/polkit-gnome-authentication-agent-1
