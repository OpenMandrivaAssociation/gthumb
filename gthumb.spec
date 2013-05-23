%define _disable_ld_no_undefined 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	An image viewer and browser for GNOME
Name:		gthumb
Version:	3.1.2
Release:	2
License:	GPLv2+
Group:		Graphics
Url:		http://gthumb.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gthumb/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	intltool
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(champlain-gtk-0.12)
BuildRequires:	pkgconfig(clutter-gtk-1.0)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(gconf-2.0) GConf2
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libbrasero-burn3)
BuildRequires:	pkgconfig(libopenraw-1.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libsoup-gnome-2.4)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(sm)

%description
gThumb lets you browse your hard disk, showing you thumbnails of image files. 
It also lets you view single files (including GIF animations), add comments to
images, organize images in catalogs, print images, view slideshows, set your
desktop background, and more. 

%package devel
Summary:	Header files for building %{name} extensions
Group:		Development/C

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

