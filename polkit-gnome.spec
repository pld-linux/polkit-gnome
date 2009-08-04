Summary:	GNOME dialogs for PolicyKit
Summary(pl.UTF-8):	Okna dialogowe GNOME dla pakietu PolicyKit
Name:		polkit-gnome
Version:	0.93
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	b30bd877f674e89a80848ed45257375d
URL:		http://people.freedesktop.org/~david/polkit-spec.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.93
Requires:	polkit >= 0.93
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
polkit-gnome provides a D-BUS session bus service that is used to
bring up authentication dialogs used for obtaining privileges.

%description -l pl.UTF-8
Pakiet polkit-gnome udostępnia usługę magistrali sesji D-BUS
służącą do wyświetlania okien dialogowych uwierzytelniania w celu
uzyskania uprawnień.

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
	--with-html-dir=%{_gtkdocdir}
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
%{_sysconfdir}/xdg/autostart/polkit-gnome-authentication-agent-1.desktop
