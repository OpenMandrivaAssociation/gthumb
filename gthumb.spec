%define name gthumb
%define version 2.11.6
%define libname %mklibname %name %version
%define api 2.0
%define api2 2.12

Summary:	An image viewer and browser for GNOME
Name:		%name
Version: %version
Release: %mkrel 1
License:	GPLv2+
URL:		http://gthumb.sourceforge.net/
Group:		Graphics
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:  scrollkeeper
BuildRequires:  gnome-doc-utils
BuildRequires:	gtk+2-devel
BuildRequires:	libGConf2-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	clutter-gtk-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	libexiv-devel
BuildRequires:	libsoup-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libopenraw-devel >= 0.0.8
BuildRequires:	tiff-devel
BuildRequires:	unique-devel >= 1.1.2
BuildRequires:	brasero-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:  intltool
BuildRequires:	gnome-common
Requires(post): scrollkeeper >= 0.3 desktop-file-utils
Requires(postun): scrollkeeper >= 0.3 desktop-file-utils

%description
gThumb lets you browse your hard disk, showing you thumbnails of image files. 
It also lets you view single files (including GIF animations), add comments to
images, organize images in catalogs, print images, view slideshows, set your
desktop background, and more. 

%package devel
Summary: Header files for building %name extensions
Group: Development/C

%description devel
gThumb lets you browse your hard disk, showing you thumbnails of image files. 
It also lets you view single files (including GIF animations), add comments to
images, organize images in catalogs, print images, view slideshows, set your
desktop background, and more. 


%prep
%setup -q

%build
%configure2_5x --disable-scrollkeeper --enable-libopenraw

%make

%install
rm -rf $RPM_BUILD_ROOT

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %{name}-%{api} --with-gnome --all-name
#for omf in %buildroot%_datadir/omf/%name/%name-??*.omf;do 
#echo "%lang($(basename $omf|sed -e s/%name-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name-%{api}.lang
#done

# remove unpackaged files 
rm -rf $RPM_BUILD_ROOT%{_libdir}/gthumb/*/*.{la,a}

%if %mdkversion < 200900
%post
%post_install_gconf_schemas %name
%update_scrollkeeper
%update_menus
%update_desktop_database
%update_icon_cache hicolor
%endif

%preun
%preun_uninstall_gconf_schemas %name

%if %mdkversion < 200900
%postun
%clean_scrollkeeper
%clean_menus
%clean_desktop_database
%clean_icon_cache hicolor
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{api}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README COPYING
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/gthumb
#%_datadir/%name-%{api}/
%_datadir/icons/hicolor/*/apps/gthumb.*
#%dir %{_datadir}/omf/%name
#%{_datadir}/omf/%name/*-C.omf
%dir %_libdir/%name/
%dir %_libdir/%name/extensions/
%_libdir/%name/extensions/*.extension
%_libdir/%name/extensions/*.so

%files devel
%defattr(-,root,root)
%doc ChangeLog
%_includedir/%name-%{api2}/
%_libdir/pkgconfig/gthumb-%{api2}.pc
