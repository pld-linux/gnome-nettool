# TODO:
#	- adapt src/ping.h to PLD ping
#
Summary:	GNOME interface for networking tools
Summary(pl.UTF-8):	Interfejs dla narzędzi sieciowych dla GNOME
Name:		gnome-nettool
Version:	2.22.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-nettool/2.22/%{name}-%{version}.tar.bz2
# Source0-md5:	afcaff8ebc76b5f352902ed424dc2856
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.19.1
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk+2
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

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name} --with-gnome

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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/%{name}/gnome-nettool-C.omf
%lang(ca) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-ca.omf
%lang(es) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-es.omf
%lang(fr) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-fr.omf
%lang(oc) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-oc.omf
%lang(pa) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-pa.omf
%lang(sv) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-sv.omf
%lang(uk) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-uk.omf
%lang(vi) %{_omf_dest_dir}/gnome-nettool/gnome-nettool-vi.omf
