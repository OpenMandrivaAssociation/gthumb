%define _disable_ld_no_undefined 1

Summary:	An image viewer and browser for GNOME
Name:		gthumb
Version:	3.1.2
Release:	1
License:	GPLv2+
URL:		http://gthumb.sourceforge.net/
Group:		Graphics
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.1/%{name}-%{version}.tar.xz

BuildRequires: flex
BuildRequires: bison
BuildRequires: intltool
BuildRequires: jpeg-devel
BuildRequires: pkgconfig(champlain-gtk-0.12)
BuildRequires: pkgconfig(clutter-gtk-1.0)
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(gconf-2.0) GConf2
BuildRequires: pkgconfig(gl)
BuildRequires: gnome-doc-utils-devel
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gstreamer-0.10)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(libbrasero-burn3)
BuildRequires: pkgconfig(libopenraw-1.0)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libsoup-gnome-2.4)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(sm)

%description
gThumb lets you browse your hard disk, showing you thumbnails of image files. 
It also lets you view single files (including GIF animations), add comments to
images, organize images in catalogs, print images, view slideshows, set your
desktop background, and more. 

%package devel
Summary: Header files for building %{name} extensions
Group: Development/C

%description devel
gThumb lets you browse your hard disk, showing you thumbnails of image files. 
It also lets you view single files (including GIF animations), add comments to
images, organize images in catalogs, print images, view slideshows, set your
desktop background, and more. 

%prep
%setup -q

%build
%configure2_5x \
	--disable-scrollkeeper \
	--disable-static \
	--enable-libopenraw

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name

# remove unpackaged files 
find %{buildroot} -name '*.la' -delete

%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/GConf/gsettings/gthumb.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gthumb
%{_datadir}/icons/hicolor/*/apps/gthumb.*
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/extensions/
%{_libdir}/%{name}/extensions/*.extension
%{_libdir}/%{name}/extensions/*.so
%{_mandir}/man1/%{name}.1*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-*/
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/gthumb.m4


%changelog
* Tue Oct 16 2012 Arkady L. Shane <ashejn@rosalinux.ru> 3.1.2-1
- update to 3.1.2

* Thu May 17 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.0.1-1
+ Revision: 799342
- update to new version 3.0.1
- cleaned up spec before upgrading to 2.14.x
- converted BRs to pkgconfig provides

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against libtiff.so.5

* Sun Oct 16 2011 Götz Waschk <waschk@mandriva.org> 2.12.4-1
+ Revision: 704885
- new version
- xz tarball

  + Oden Eriksson <oeriksson@mandriva.com>
    - attempt to relink against libpng15.so.15

* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 2.12.3-2
+ Revision: 677080
- rebuild to add gconf2 as req
- BR sm
- new version 2.12.3

  + Götz Waschk <waschk@mandriva.org>
    - new version
    - drop patch 0

* Mon Dec 20 2010 Götz Waschk <waschk@mandriva.org> 2.12.1-4mdv2011.0
+ Revision: 623307
- rebuild for buildsystem problem

  + Funda Wang <fwang@mandriva.org>
    - add patch to build with latest libexiv

* Sun Dec 05 2010 Funda Wang <fwang@mandriva.org> 2.12.1-2mdv2011.0
+ Revision: 609615
- disable exiv support for now

* Mon Nov 15 2010 Götz Waschk <waschk@mandriva.org> 2.12.1-1mdv2011.0
+ Revision: 597831
- update to new version 2.12.1

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.12.0-1mdv2011.0
+ Revision: 581653
- new version
- add m4 file

* Tue Sep 14 2010 Götz Waschk <waschk@mandriva.org> 2.11.92-1mdv2011.0
+ Revision: 578360
- update to new version 2.11.92

* Mon Aug 30 2010 Götz Waschk <waschk@mandriva.org> 2.11.91-1mdv2011.0
+ Revision: 574545
- update to new version 2.11.91

* Sat Aug 21 2010 Funda Wang <fwang@mandriva.org> 2.11.90-2mdv2011.0
+ Revision: 571611
- rebuild for new brasero

* Mon Aug 16 2010 Götz Waschk <waschk@mandriva.org> 2.11.90-1mdv2011.0
+ Revision: 570633
- update to new version 2.11.90

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 2.11.6-2mdv2011.0
+ Revision: 565545
- rebuild for new exiv2

* Tue Aug 03 2010 Götz Waschk <waschk@mandriva.org> 2.11.6-1mdv2011.0
+ Revision: 565413
- update to new version 2.11.6

* Mon Jul 12 2010 Götz Waschk <waschk@mandriva.org> 2.11.5-1mdv2011.0
+ Revision: 551299
- update to new version 2.11.5

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 2.11.4-1mdv2011.0
+ Revision: 550654
- new version
- update file list

* Thu Apr 15 2010 Götz Waschk <waschk@mandriva.org> 2.11.3-2mdv2010.1
+ Revision: 535087
- build with CD burning support

* Thu Apr 15 2010 Götz Waschk <waschk@mandriva.org> 2.11.3-1mdv2010.1
+ Revision: 535038
- new version
- drop patch

* Tue Feb 23 2010 Götz Waschk <waschk@mandriva.org> 2.11.2.1-1mdv2010.1
+ Revision: 510037
- new version
- remove build workaround

* Tue Feb 23 2010 Götz Waschk <waschk@mandriva.org> 2.11.2-1mdv2010.1
+ Revision: 510003
- new version
- drop patch 1
- fix build
- update build deps
- update file list

* Tue Feb 02 2010 Funda Wang <fwang@mandriva.org> 2.11.1-4mdv2010.1
+ Revision: 499437
- BR gnome-common

  + Frederic Crozat <fcrozat@mandriva.com>
    - Patch1: fix plugin linking

* Sun Jan 24 2010 Funda Wang <fwang@mandriva.org> 2.11.1-3mdv2010.1
+ Revision: 495416
- build with latest gtk
- these packages do not exist

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.11.1-2mdv2010.1
+ Revision: 488761
- rebuilt against libjpeg v8

* Mon Jan 04 2010 Götz Waschk <waschk@mandriva.org> 2.11.1-1mdv2010.1
+ Revision: 486240
- reenable openraw
- new version
- drop patches
- drop import script
- update file list
- update build deps

* Tue Oct 06 2009 Frederic Crozat <fcrozat@mandriva.com> 2.10.11-3mdv2010.0
+ Revision: 454698
- Add sources 1, 2 : import tool for use with nautilus (Fedora)
- Patch1 (GIT): fix import default directory (GNOME bug #577042)

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 2.10.11-2mdv2010.0
+ Revision: 416659
- rebuilt against libjpeg v7

* Tue Feb 24 2009 Götz Waschk <waschk@mandriva.org> 2.10.11-1mdv2009.1
+ Revision: 344435
- new version
- fix format strings

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.10.10-1mdv2009.0
+ Revision: 286975
- new version
- drop patch

* Mon Aug 04 2008 Götz Waschk <waschk@mandriva.org> 2.10.9-1mdv2009.0
+ Revision: 263602
- new version
- rediff the patch
- update license
- fix linking

  + Funda Wang <fwang@mandriva.org>
    - drop libpackage

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jan 01 2008 Götz Waschk <waschk@mandriva.org> 2.10.8-1mdv2008.1
+ Revision: 140043
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 09 2007 Funda Wang <fwang@mandriva.org> 2.10.7-2mdv2008.1
+ Revision: 116724
- drop old menu

* Mon Oct 15 2007 Götz Waschk <waschk@mandriva.org> 2.10.7-1mdv2008.1
+ Revision: 98706
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill changelog left by repsys

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 2.10.6-1mdv2008.0
+ Revision: 72370
- new version
- update file list

  + Thierry Vignaud <tv@mandriva.org>
    - replace %%{_datadir}/man by %%{_mandir}!

* Tue Jun 26 2007 Götz Waschk <waschk@mandriva.org> 2.10.5-1mdv2008.0
+ Revision: 44349
- new version

* Tue Jun 19 2007 Götz Waschk <waschk@mandriva.org> 2.10.4-1mdv2008.0
+ Revision: 41332
- new version
- fix buildrequires

* Wed May 16 2007 Götz Waschk <waschk@mandriva.org> 2.10.3-1mdv2008.0
+ Revision: 27296
- new version

* Tue Apr 17 2007 Pascal Terjan <pterjan@mandriva.org> 2.10.2-1mdv2007.1
+ Revision: 13549
- 2.10.2


* Wed Apr 04 2007 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdv2007.1
+ Revision: 150478
- fix buildrequires
- new version

* Tue Mar 20 2007 Götz Waschk <waschk@mandriva.org> 2.10.0-1mdv2007.1
+ Revision: 146838
- new version
- update file list

* Tue Feb 27 2007 Götz Waschk <waschk@mandriva.org> 2.9.3-2mdv2007.1
+ Revision: 126258
- build with RAW support

* Mon Feb 26 2007 Götz Waschk <waschk@mandriva.org> 2.9.3-1mdv2007.1
+ Revision: 126110
- new version

* Mon Feb 19 2007 Götz Waschk <waschk@mandriva.org> 2.9.2-1mdv2007.1
+ Revision: 122710
- new version
- drop patch
- update file list

* Wed Jan 03 2007 Pascal Terjan <pterjan@mandriva.org> 2.9.1-4mdv2007.1
+ Revision: 103698
- Add patch (based on svn) to fix behaviour after image deletion

* Sun Dec 31 2006 Götz Waschk <waschk@mandriva.org> 2.9.1-3mdv2007.1
+ Revision: 102969
- enable libiptcdata support

* Sat Dec 30 2006 Pascal Terjan <pterjan@mandriva.org> 2.9.1-2mdv2007.1
+ Revision: 102840
- increase release
- BuildRequires libxxf86vm-devel

* Wed Dec 27 2006 Götz Waschk <waschk@mandriva.org> 2.9.1-1mdv2007.1
+ Revision: 102164
- fix buildrequires
- new version
- update file list

* Sun Dec 10 2006 Pascal Terjan <pterjan@mandriva.org> 2.8.1-2mdv2007.1
+ Revision: 94483
- Rebuild for new libgphoto

* Fri Dec 08 2006 Götz Waschk <waschk@mandriva.org> 2.8.1-1mdv2007.1
+ Revision: 92167
- new version

* Sun Nov 26 2006 Götz Waschk <waschk@mandriva.org> 2.8.0-3mdv2007.1
+ Revision: 87344
- new version

* Fri Oct 13 2006 Götz Waschk <waschk@mandriva.org> 2.7.9-3mdv2007.1
+ Revision: 63847
- rebuild
- rebuild
- Import gthumb

* Fri Oct 06 2006 Götz Waschk <waschk@mandriva.org> 2.7.9-1mdv2007.0
- New version 2.7.9

* Tue Aug 08 2006 G�tz Waschk <waschk@mandriva.org> 2.7.8-4mdv2007.0
- fix buildrequires

* Fri Aug 04 2006 Frederic Crozat <fcrozat@mandriva.com> 2.7.8-3mdv2007.0
- Rebuild with latest dbus

* Wed Jul 26 2006 G�tz Waschk <waschk@mandriva.org> 2.7.8-2mdv2007.0
- update desktop database

* Wed Jul 26 2006 G�tz Waschk <waschk@mandriva.org> 2.7.8-1mdv2007.0
- new macros
- xdg menu
- New release 2.7.8

* Fri May 19 2006 Götz Waschk <waschk@mandriva.org> 2.7.7-1mdk
- New release 2.7.7

* Fri Apr 21 2006 Frederic Crozat <fcrozat@mandriva.com> 2.7.6-1mdk
- Release 2.7.6
- Remove patch0 (merged upstream)

* Fri Feb 17 2006 G�tz Waschk <waschk@mandriva.org> 2.6.9-1mdk
- add library package
- New release 2.6.9
- use mkrel

* Wed Dec 28 2005 Frederic Crozat <fcrozat@mandriva.com> 2.6.8-2mdk
- Update patch0 to fix utf8 text for photo import

* Sat Oct 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.6.8-1mdk
- Release 2.6.8

* Wed Aug 31 2005 G�tz Waschk <waschk@mandriva.org> 2.6.6-2mdk
- replace preqreq

* Tue Jun 28 2005 G�tz Waschk <waschk@mandriva.org> 2.6.6-1mdk
- New release 2.6.6

* Thu May 05 2005 G�tz Waschk <waschk@mandriva.org> 2.6.5-2mdk
- fix build on x86_64

* Sun Apr 24 2005 G�tz Waschk <waschk@mandriva.org> 2.6.5-1mdk
- New release 2.6.5

* Wed Apr 20 2005 Frederic Crozat <fcrozat@mandriva.com> 2.6.4-1mdk 
- Release 2.6.4 (based on G�tz Waschk package)
- regenerate patch0

* Fri Feb 18 2005 G�tz Waschk <waschk@linux-mandrake.com> 2.6.3-2mdk
- fix rpmlint warnings

* Sat Jan 22 2005 Goetz Waschk <waschk@linux-mandrake.com> 2.6.3-1mdk
- New release 2.6.3

* Thu Jan 06 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.2-2mdk 
- Rebuild with latest howl

* Mon Dec 06 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- New release 2.6.2

* Sun Nov 21 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- New release 2.6.1

* Fri Oct 22 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.0.1-1mdk
- New release 2.6.0.1

* Tue Oct 19 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.6.0-1mdk
- rediff patch 0
- New release 2.6.0

* Wed Sep 15 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.4.2-2mdk
- Patch0: don't convert exif info in utf8, libexif9 already does it

* Thu Sep 02 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.4.2-1mdk
- New release 2.4.2

* Thu Aug 05 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.4.1-2mdk
- fix buildrequires

* Fri Jul 02 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.4.1-1mdk
- fix source URL
- New release 2.4.1

* Wed Jun 02 2004 Abel Cheung <deaddog@deaddog.org> 2.4.0-2mdk
- Use ImageMagick to convert icons
- Build against gphoto and libtiff as well
- yelp-pregenerate is no more

* Wed Jun 02 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.4.0-1mdk
- New release 2.4.0

* Tue Apr 27 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.3.3-1mdk
- fix source URL
- new version

* Thu Apr 22 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.3.2-2mdk
- fix buildrequires

* Thu Apr 08 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.3.2-1mdk
- new version

