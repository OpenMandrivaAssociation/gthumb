%define _disable_ld_no_undefined 1
%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	An image viewer and browser for GNOME
Name:		gthumb
Version:	3.12.6
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		https://gthumb.sourceforge.net/
Source0:	https://download.gnome.org/sources/gthumb/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	flex
BuildRequires:	bison
BuildRequires:  meson
BuildRequires:	pkgconfig(champlain-0.12) >= 0.12.0
BuildRequires:	pkgconfig(champlain-gtk-0.12) >= 0.12.0
BuildRequires:	pkgconfig(clutter-1.0) >= 1.0.0
BuildRequires:	pkgconfig(clutter-gtk-1.0) >= 1.0.0
BuildRequires:	pkgconfig(exiv2) >= 0.21
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1) >= 3.2.0
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gstreamer-1.0) >= 1.0.0
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0) >= 1.0.0
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libraw) >= 0.14
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.34.0
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.36
BuildRequires:	pkgconfig(libsoup-gnome-2.4) >= 2.36
BuildRequires:  pkgconfig(libssh)
BuildRequires:	pkgconfig(libwebp) >= 0.2.0
BuildRequires:	pkgconfig(sm) >= 1.0.0
BuildRequires:	pkgconfig(webkit2gtk-4.0) >= 1.10.0
BuildRequires:	pkgconfig(zlib)
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	itstool
BuildRequires:	intltool >= 0.35.0

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
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS NEWS README.md COPYING
%{_bindir}/*
%{_libexecdir}/gthumb/video-thumbnailer
#{_datadir}/metainfo/org.gnome.gThumb.appdata.xml
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gthumb
%{_iconsdir}/hicolor/*/apps/*
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/extensions/
%{_libdir}/%{name}/extensions/*.extension
%{_libdir}/%{name}/extensions/*.so
%{_mandir}/man1/%{name}.1*

%files devel
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/gthumb.m4
