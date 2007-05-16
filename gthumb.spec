%define name gthumb
%define version 2.10.3
%define libname %mklibname %name %version

Summary:	An image viewer and browser for GNOME
Name:		%name
Version: %version
Release: %mkrel 1
License:	GPL
URL:		http://gthumb.sourceforge.net/
Group:		Graphics
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	libgnomeprintui-devel
BuildRequires:  libgnomeui2-devel
BuildRequires:  scrollkeeper
BuildRequires:  gnome-doc-utils
BuildRequires:  libexif-devel >= 0.5.12
BuildRequires:  png-devel
BuildRequires:  libglade2.0-devel
BuildRequires:	gphoto2-devel >= 2.1.3
BuildRequires:	libopenraw-devel
BuildRequires:	libiptcdata-devel
BuildRequires:	tiff-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	ImageMagick
BuildRequires:  intltool
BuildRequires:  perl-XML-Parser
BuildRequires:  desktop-file-utils
BuildRequires:  libxxf86vm-devel
Requires: jpeg-progs
Requires(post): scrollkeeper >= 0.3 desktop-file-utils
Requires(postun): scrollkeeper >= 0.3 desktop-file-utils

%description
gThumb lets you browse your hard disk, showing you thumbnails of image files. 
It also lets you view single files (including GIF animations), add comments to
images, organize images in catalogs, print images, view slideshows, set your
desktop background, and more. 

%package -n %libname
Group:System/Libraries
Summary: Shared library part of gThumb

%description -n %libname
gThumb lets you browse your hard disk, showing you thumbnails of image files. 
It also lets you view single files (including GIF animations), add comments to
images, organize images in catalogs, print images, view slideshows, set your
desktop background, and more. 

%prep
%setup -q

%build
%configure2_5x --disable-scrollkeeper

%make

%install
rm -rf $RPM_BUILD_ROOT

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %{name}-2.0 --with-gnome --all-name
for omf in %buildroot%_datadir/omf/%name/%name-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/%name-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name-2.0.lang
done



# icons
mkdir -p %{buildroot}/%{_iconsdir} %{buildroot}%{_miconsdir}
install -m 644 -D       data/gthumb.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 data/gthumb.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 data/gthumb.png %{buildroot}%{_miconsdir}/%{name}.png

install -d %buildroot/%_menudir
cat > %buildroot/%{_menudir}/%name << EOF
?package(%{name}): \
command="%{_bindir}/%{name}" \
icon="%name.png" \
needs="X11" \
section="Multimedia/Graphics" \
title="GThumb" \
longtitle="View and organize your images" \
startup_notify="true" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Graphics" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


# remove unpackaged files 
rm -rf $RPM_BUILD_ROOT%{_libdir}/gthumb/modules/*.{la,a} \
 $RPM_BUILD_ROOT%{_libdir}/gthumb/*.{la,a} \
 %buildroot%_libdir/*.{la,a} \
 $RPM_BUILD_ROOT%{_localstatedir}/scrollkeeper

%post
%post_install_gconf_schemas %name
%update_scrollkeeper
%update_menus
%update_desktop_database
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %name

%postun
%clean_scrollkeeper
%clean_menus
%clean_desktop_database
%clean_icon_cache hicolor

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-2.0.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_libdir}/gthumb
%{_datadir}/applications/*
%{_datadir}/gthumb
%_libdir/libgthumb.so
%dir %{_datadir}/omf/%name
%{_datadir}/omf/%name/*-C.omf
%{_datadir}/icons/hicolor/48x48/apps/gthumb.png
%{_datadir}/man/man1/*
%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


%changelog
* Tue Apr 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.1-1mdv2007.1
+ Revision: 150478
- fix buildrequires
- new version

* Tue Mar 20 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.10.0-1mdv2007.1
+ Revision: 146838
- new version
- update file list

* Tue Feb 27 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.9.3-2mdv2007.1
+ Revision: 126258
- build with RAW support

* Mon Feb 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.9.3-1mdv2007.1
+ Revision: 126110
- new version

* Mon Feb 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.9.2-1mdv2007.1
+ Revision: 122710
- new version
- drop patch
- update file list

* Wed Jan 03 2007 Pascal Terjan <pterjan@mandriva.org> 2.9.1-4mdv2007.1
+ Revision: 103698
- Add patch (based on svn) to fix behaviour after image deletion

* Sun Dec 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.9.1-3mdv2007.1
+ Revision: 102969
- enable libiptcdata support

* Sat Dec 30 2006 Pascal Terjan <pterjan@mandriva.org> 2.9.1-2mdv2007.1
+ Revision: 102840
- increase release
- BuildRequires libxxf86vm-devel

* Wed Dec 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.9.1-1mdv2007.1
+ Revision: 102164
- fix buildrequires
- new version
- update file list

* Sun Dec 10 2006 Pascal Terjan <pterjan@mandriva.org> 2.8.1-2mdv2007.1
+ Revision: 94483
- Rebuild for new libgphoto

* Fri Dec 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.1-1mdv2007.1
+ Revision: 92167
- new version

* Sun Nov 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.0-3mdv2007.1
+ Revision: 87344
- new version

* Thu Oct 12 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.7.9-3mdv2007.1
+ Revision: 63847
- rebuild
- rebuild
- Import gthumb



* Thu Oct 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.7.9-1mdv2007.0
- New version 2.7.9

* Mon Aug  7 2006 Götz Waschk <waschk@mandriva.org> 2.7.8-4mdv2007.0
- fix buildrequires

* Thu Aug 03 2006 Frederic Crozat <fcrozat@mandriva.com> 2.7.8-3mdv2007.0
- Rebuild with latest dbus

* Tue Jul 25 2006 Götz Waschk <waschk@mandriva.org> 2.7.8-2mdv2007.0
- update desktop database

* Tue Jul 25 2006 Götz Waschk <waschk@mandriva.org> 2.7.8-1mdv2007.0
- new macros
- xdg menu
- New release 2.7.8

* Thu May 18 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.7.7-1mdk
- New release 2.7.7

* Thu Apr 20 2006 Frederic Crozat <fcrozat@mandriva.com> 2.7.6-1mdk
- Release 2.7.6
- Remove patch0 (merged upstream)

* Fri Feb 17 2006 Götz Waschk <waschk@mandriva.org> 2.6.9-1mdk
- add library package
- New release 2.6.9
- use mkrel

* Wed Dec 28 2005 Frederic Crozat <fcrozat@mandriva.com> 2.6.8-2mdk
- Update patch0 to fix utf8 text for photo import

* Fri Oct 07 2005 Frederic Crozat <fcrozat@mandriva.com> 2.6.8-1mdk
- Release 2.6.8

* Tue Aug 30 2005 Götz Waschk <waschk@mandriva.org> 2.6.6-2mdk
- replace preqreq

* Mon Jun 27 2005 Götz Waschk <waschk@mandriva.org> 2.6.6-1mdk
- New release 2.6.6

* Wed May  4 2005 Götz Waschk <waschk@mandriva.org> 2.6.5-2mdk
- fix build on x86_64

* Sat Apr 23 2005 Götz Waschk <waschk@mandriva.org> 2.6.5-1mdk
- New release 2.6.5

* Tue Apr 19 2005 Frederic Crozat <fcrozat@mandriva.com> 2.6.4-1mdk 
- Release 2.6.4 (based on Götz Waschk package)
- regenerate patch0

* Fri Feb 18 2005 Götz Waschk <waschk@linux-mandrake.com> 2.6.3-2mdk
- fix rpmlint warnings

* Sat Jan 22 2005 Goetz Waschk <waschk@linux-mandrake.com> 2.6.3-1mdk
- New release 2.6.3

* Thu Jan 06 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.2-2mdk 
- Rebuild with latest howl

* Mon Dec  6 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- New release 2.6.2

* Sun Nov 21 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- New release 2.6.1

* Thu Oct 21 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.0.1-1mdk
- New release 2.6.0.1

* Mon Oct 18 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.0-1mdk
- rediff patch 0
- New release 2.6.0

* Tue Sep 14 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.4.2-2mdk
- Patch0: don't convert exif info in utf8, libexif9 already does it

* Wed Sep  1 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.4.2-1mdk
- New release 2.4.2

* Wed Aug  4 2004 Götz Waschk <waschk@linux-mandrake.com> 2.4.1-2mdk
- fix buildrequires

* Thu Jul  1 2004 Götz Waschk <waschk@linux-mandrake.com> 2.4.1-1mdk
- fix source URL
- New release 2.4.1

* Tue Jun 01 2004 Abel Cheung <deaddog@deaddog.org> 2.4.0-2mdk
- Use ImageMagick to convert icons
- Build against gphoto and libtiff as well
- yelp-pregenerate is no more

* Tue Jun  1 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.4.0-1mdk
- New release 2.4.0

* Mon Apr 26 2004 Götz Waschk <waschk@linux-mandrake.com> 2.3.3-1mdk
- fix source URL
- new version

* Wed Apr 21 2004 Götz Waschk <waschk@linux-mandrake.com> 2.3.2-2mdk
- fix buildrequires

* Wed Apr  7 2004 Götz Waschk <waschk@linux-mandrake.com> 2.3.2-1mdk
- new version

* Mon Feb 09 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.2.1-2mdk
- Fix menu

* Sat Jan 24 2004 Götz Waschk <waschk@linux-mandrake.com> 2.2.1-1mdk
- fix menu
- new version

* Fri Dec 19 2003 Götz Waschk <waschk@linux-mandrake.com> 2.2.0-1mdk
- new version

* Tue Nov 18 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.9-1mdk
- drop merged patch
- new version

* Mon Nov  3 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.8-2mdk
- remove one dummy rpmlint warning
- fix buildrequires

* Mon Nov  3 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.8-1mdk
- patch to move libgthumb to %_libdir/gthumb
- new version

* Tue Oct 14 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.7-1mdk
- new version

* Mon Sep  1 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.6-1mdk
- new version

* Tue Aug 19 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.5-1mdk
- new version

* Sun Aug 17 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.4-2mdk
- reenable parallel build
- rebuild with newer libexif

* Sun Aug 10 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.4-1mdk
- drop merged patch
- new version

* Wed Jul 16 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.3-4mdk
- fix postun script (thanks to Michael Reinsch) 

* Tue Jul 15 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.3-3mdk
- don't deinstall schemas on update

* Fri Jul 11 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 2.1.3-2mdk
- Patch0: fix schema

* Mon Jul  7 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.3-1mdk
- add schema uninstallation
- new version

* Wed May 07 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 2.1.2-1mdk
- Release 2.1.2

* Wed Mar 26 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.1.1-1mdk
- 2.1.1

* Wed Mar 12 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.0-3mdk
- fix buildrequires

* Tue Mar 11 2003 Götz Waschk <waschk@linux-mandrake.com> 2.1.0-2mdk
- fix buildrequires

* Mon Mar  3 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 2.1.0-1mdk
- Release 2.1.0 (GNOME 2.2 version)
- Remove patch 0 (merged upstream)

* Mon Jan 27 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.1-1mdk
- Release 2.0.1

* Tue Jan 21 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.0-1mdk
- Release 2.0.0

* Fri Jan 17 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 1.108-2mdk
- Recompiled against latest openssl
- Generate yelp cache

* Mon Jan  6 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 1.108-1mdk
- Release 1.108

* Mon Dec 23 2002 Götz Waschk <waschk@linux-mandrake.com> 1.107-1mdk
- fix the rpmlint warning about the menu title
- reenable parallel build
- rediff the patch
- new version

* Fri Nov 29 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.106-1mdk
- Release 1.106
- Patch0 : fix compilation with GNOME 2.1.x

* Thu Oct 31 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.104-2mdk
- Add missing views
- Put back translations
- Disable parallel compilation, it is broken
- Fix BuildRequires
- Add missing dependency on libjpeg-progs, needed for jpegtran
- Compiled with EXIF support

* Wed Oct  2 2002 Götz Waschk <waschk@linux-mandrake.com> 1.104-1mdk
- new version

* Mon Aug 12 2002 Götz Waschk <waschk@linux-mandrake.com> 1.103-1mdk
- new version

* Fri Aug  2 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.102-1mdk
- First Mandrake Version by Yves Duret (spec file courtesy copy from Paolo Bacchilega)
