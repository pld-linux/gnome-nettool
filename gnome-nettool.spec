Summary:	GNOME interface for networking tools
Summary(pl.UTF-8):	Interfejs dla narzędzi sieciowych dla GNOME
Name:		gnome-nettool
Version:	2.18.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-nettool/2.18/%{name}-%{version}.tar.bz2
# Source0-md5:	596616cf631b5bc9ec0c873208ccfce9
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.18.0.1
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.10
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
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

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner %{name} -e << EOF
For full functionality, you need to install various networking command-line
tools, like ping, netstat, ifconfig, whois, traceroute, finger.
EOF
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/%{name}/gnome-nettool-C.omf
%lang(fr) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-fr.omf
%lang(pa) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-pa.omf
%lang(sv) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-sv.omf
