%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define debug_package %{nil}
%define __noautoreq /usr/bin/gjs
%define _disable_rebuild_configure 1

Name:		gnome-weather
Version:	3.18.1
Release:	1
Summary:	A weather application for GNOME
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://wiki.gnome.org/Apps/Weather
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	gjs
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gjs-1.0)
BuildRequires:	pkgconfig(gweather-3.0)
Requires:	gjs

%description
%{name} is a weather application for GNOME.

%prep
%setup -q

%build
%configure --disable-schemas-compile
%make

%install
%makeinstall_std

find %{buildroot} -name "*.la" -delete

%find_lang org.gnome.Weather

%files -f org.gnome.Weather.lang
%doc NEWS data/CREDITS
%{_bindir}/%{name}
%{_datadir}/appdata/org.gnome.Weather.Application.appdata.xml
%{_datadir}/org.gnome.Weather
%{_datadir}/gnome-shell/search-providers/org.gnome.Weather.Application.search-provider.ini
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/*
%{_iconsdir}/*/*/*/*
%{_datadir}/dbus-1/services/*.service


%changelog
* Sun Oct 19 2014 wally <wally> 3.14.1-3.mga5
+ Revision: 791734
- rebuild after latest rpm-mageia-setup
- drop requires which are now auto-generated

* Wed Oct 15 2014 umeabot <umeabot> 3.14.1-2.mga5
+ Revision: 745832
- Second Mageia 5 Mass Rebuild

* Mon Oct 13 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 738326
- new version 3.14.1

* Sun Sep 28 2014 tv <tv> 3.14.0-3.mga5
+ Revision: 731148
- rebuild so that it picks typelib() requires
- rebuild for bogus file deps

  + ovitters <ovitters>
    - new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 679794
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 677617
- new version 3.13.92

* Mon Sep 01 2014 ovitters <ovitters> 3.13.91-1.mga5
+ Revision: 670760
- new version 3.13.91

* Sat Aug 23 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 666722
- new version 3.13.90

* Wed Jul 23 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 656034
- new version 3.13.4

* Tue Jun 24 2014 ovitters <ovitters> 3.13.3-2.mga5
+ Revision: 639449
- update url

* Tue Jun 24 2014 ovitters <ovitters> 3.13.3-1.mga5
+ Revision: 639443
- new version 3.13.3

* Thu May 29 2014 ovitters <ovitters> 3.13.2-1.mga5
+ Revision: 627426
- new version 3.13.2

* Mon May 12 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 622331
- new version 3.12.1

* Tue Mar 25 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 608573
- new version 3.12.0

* Tue Mar 18 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 605011
- new version 3.11.92

* Tue Mar 04 2014 ovitters <ovitters> 3.11.91-1.mga5
+ Revision: 599236
- new version 3.11.91

* Mon Feb 17 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 594022
- new version 3.11.90

* Wed Feb 05 2014 ovitters <ovitters> 3.11.5-1.mga5
+ Revision: 583239
- new version 3.11.5

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1-2.mga4
+ Revision: 545233
- Mageia 4 Mass Rebuild

* Tue Oct 15 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 500936
- new version 3.10.1

* Tue Sep 24 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 485252
- new version 3.10.0

* Mon Sep 16 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480359
- new version 3.9.92

* Tue Sep 03 2013 fwang <fwang> 3.9.91-1.mga4
+ Revision: 474557
- update file list

  + ovitters <ovitters>
    - new version 3.9.91

* Tue Aug 20 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468038
- update file list

  + ovitters <ovitters>
    - new version 3.9.90

* Thu Aug 01 2013 dams <dams> 3.9.5-3.mga4
+ Revision: 462291
- fix not working apps by adding a require

  + ovitters <ovitters>
    - clean spec

* Tue Jul 30 2013 ovitters <ovitters> 3.9.5-2.mga4
+ Revision: 461208
- br gjs

* Tue Jul 30 2013 ovitters <ovitters> 3.9.5-1.mga4
+ Revision: 461106
- new version 3.9.5

* Tue Jul 02 2013 dams <dams> 3.9.3-6.mga4
+ Revision: 449570
- fix %%configure

* Mon Jul 01 2013 dams <dams> 3.9.3-5.mga4
+ Revision: 449493
- update %%configure arg

* Mon Jul 01 2013 dams <dams> 3.9.3-4.mga4
+ Revision: 449489
- update %%configure arg

* Mon Jul 01 2013 dams <dams> 3.9.3-3.mga4
+ Revision: 449485
- add back 'require'

* Mon Jul 01 2013 dams <dams> 3.9.3-2.mga4
+ Revision: 449476
- update %%configure option
- clean specfile

* Mon Jul 01 2013 fwang <fwang> 3.9.3-1.mga4
+ Revision: 448733
- update file list

  + ovitters <ovitters>
    - new version 3.9.3

* Thu May 30 2013 dams <dams> 3.8.2-2.mga4
+ Revision: 433080
- add 'libgweather-gir3.0' as require

* Sun May 26 2013 ovitters <ovitters> 3.8.2-1.mga4
+ Revision: 428145
- imported package gnome-weather

