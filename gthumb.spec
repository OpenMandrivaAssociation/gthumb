%define name gthumb
%define version 2.10.7
%define libname %mklibname %name %version

Summary:	An image viewer and browser for GNOME
Name:		%name
Version: %version
Release: %mkrel 2
License:	GPL
URL:		http://gthumb.sourceforge.net/
Group:		Graphics
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
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
BuildRequires:  libxxf86vm-devel
BuildRequires:  libxtst-devel
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
%_libdir/bonobo/servers/GNOME_GThumb.server
%dir %{_datadir}/omf/%name
%{_datadir}/omf/%name/*-C.omf
%{_datadir}/icons/hicolor/48x48/apps/gthumb.png
%{_mandir}/man1/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
