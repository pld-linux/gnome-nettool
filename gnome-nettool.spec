# TODO:
#	- adapt src/ping.h to PLD ping
#
Summary:	GNOME interface for networking tools
Summary(pl.UTF-8):	Interfejs dla narzędzi sieciowych dla GNOME
Name:		gnome-nettool
Version:	42.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-nettool/42/%{name}-%{version}.tar.xz
# Source0-md5:	ba99489e9e3a1af03e9f2719acac7beb
Patch0:		%{name}-desktop.patch
URL:		https://www.gnome.org/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	libgtop-devel >= 2.26.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig >= 1:0.16
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz >= 1:4.999.7
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.28.0
Requires:	hicolor-icon-theme
Suggests:	bind-utils
Suggests:	bsd-finger
Suggests:	net-tools
Suggests:	ping
Suggests:	traceroute
Suggests:	whois
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a GNOME GUI for the basic networking tools like ping, whois,
traceroute and dig.

%description -l pl.UTF-8
Graficzny interfejs użytkownika do podstawowych narzędzi sieciowych,
takich jak ping, whois, traceroute czy dig dla GNOME.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '/^po\/Makefile\.in/d' configure.ac

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
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

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-nettool
%{_datadir}/appdata/gnome-nettool.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-nettool.gschema.xml
%{_datadir}/%{name}
%{_desktopdir}/gnome-nettool.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-nettool.png
%{_iconsdir}/hicolor/scalable/apps/gnome-nettool*.svg
