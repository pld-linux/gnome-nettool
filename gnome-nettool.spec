Summary:	GNOME interface for networking tools
Summary(pl.UTF-8):	Interfejs dla narzędzi sieciowych dla GNOME
Name:		gnome-nettool
Version:	2.19.90
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-nettool/2.19/%{name}-%{version}.tar.bz2
# Source0-md5:	5f3a1c3f2ad639494dc4c98cfa1f1b1c
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.19.1
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	gnome-doc-utils >= 0.11.2
BuildRequires:	gtk+2-devel >= 2:2.10.14
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libglade2-devel >= 1:2.6.2
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
%lang(ca) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-ca.omf
%lang(es) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-es.omf
%lang(fr) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-fr.omf
%lang(pa) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-pa.omf
%lang(sv) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-sv.omf
%lang(uk) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-uk.omf
