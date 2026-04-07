%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define debug_package %{nil}
%define __noautoreq /usr/bin/gjs
%global __requires_exclude ^GLib$
%define _disable_rebuild_configure 1

Name:		gnome-weather
Version:	50.0
Release:	1
Summary:	A weather application for GNOME
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://wiki.gnome.org/Apps/Weather
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:	intltool
BuildRequires:	gjs
BuildRequires:  meson
BuildRequires:  typescript
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gjs-1.0)
BuildRequires:	pkgconfig(gweather4)
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(libadwaita-1)
Requires:	gjs

%description
%{name} is a weather application for GNOME.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name "*.la" -delete

%find_lang org.gnome.Weather

%files -f org.gnome.Weather.lang
%doc NEWS data/CREDITS
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.Weather.metainfo.xml
%{_datadir}/org.gnome.Weather
%{_datadir}/gnome-shell/search-providers/org.gnome.Weather.search-provider.ini
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/*
%{_iconsdir}/*/*/*/*
%{_datadir}/dbus-1/services/*.service
