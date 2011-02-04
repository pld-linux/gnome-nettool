# TODO:
#	- adapt src/ping.h to PLD ping
#
Summary:	GNOME interface for networking tools
Summary(pl.UTF-8):	Interfejs dla narzędzi sieciowych dla GNOME
Name:		gnome-nettool
Version:	2.32.0
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-nettool/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	af5436deb30ccfb3f6a1f8ea5602c40d
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgtop-devel >= 2.26.0
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Suggests:	bind-utils
Suggests:	bsd-finger
Suggests:	net-tools
Suggests:	ping
Suggests:	traceroute
Suggests:	whois
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a GNOME GUI for the basic networking tools like ping, whois,
traceroute and dig.

%description -l pl.UTF-8
GUI dla podstawowych narzędzi sieciowych, takich jak ping, whois,
traceroute czy dig dla GNOME.

%prep
%setup -q
%patch0 -p1

sed -i -e 's/en@shaw//' po/LINGUAS
rm -f po/en@shaw.po

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-nettool
%{_datadir}/%{name}
%{_desktopdir}/gnome-nettool.desktop
%{_iconsdir}/hicolor/*/apps/*
