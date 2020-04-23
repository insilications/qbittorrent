#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6E4A2D025B7CC9A2 (hammered999@gmail.com)
#
Name     : qbittorrent
Version  : 4.2.4
Release  : 12
URL      : https://sourceforge.net/projects/qbittorrent/files/qbittorrent/qbittorrent-4.2.4/qbittorrent-4.2.4.tar.xz
Source0  : https://sourceforge.net/projects/qbittorrent/files/qbittorrent/qbittorrent-4.2.4/qbittorrent-4.2.4.tar.xz
Source1  : https://sourceforge.net/projects/qbittorrent/files/qbittorrent/qbittorrent-4.2.4/qbittorrent-4.2.4.tar.xz.asc
Summary  : An advanced BitTorrent client programmed in C++, based on Qt toolkit and libtorrent-rasterbar.
Group    : Development/Tools
License  : GPL-2.0
Requires: qbittorrent-bin = %{version}-%{release}
Requires: qbittorrent-data = %{version}-%{release}
Requires: qbittorrent-license = %{version}-%{release}
Requires: qbittorrent-man = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : openssl-dev
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(libtorrent-rasterbar)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(zlib)
BuildRequires : qttools-dev
BuildRequires : sed

%description
TRANSLATORS:
1. Use an editor that has NSIS syntax highlighting(eg Notepad++/Geany). This will
make your life easier.
2. Open the relevant .nsi file that exists in the folder named
"installer-translations"
3. Lines starting with ";" are considered comments. These include the
english message to help you with the translation.
4. Edit only the part inside the quotation marks(""). Unless you know
what you are doing.
5. Save the files with utf8 encoding and BOM.
6. Submit your changes: 1) as a pull request to the official git repo or
2) open an issue to the bugtracker and attach them or 3) via email or
4)the same way you provide the translations for qbt itself

%package bin
Summary: bin components for the qbittorrent package.
Group: Binaries
Requires: qbittorrent-data = %{version}-%{release}
Requires: qbittorrent-license = %{version}-%{release}

%description bin
bin components for the qbittorrent package.


%package data
Summary: data components for the qbittorrent package.
Group: Data

%description data
data components for the qbittorrent package.


%package license
Summary: license components for the qbittorrent package.
Group: Default

%description license
license components for the qbittorrent package.


%package man
Summary: man components for the qbittorrent package.
Group: Default

%description man
man components for the qbittorrent package.


%prep
%setup -q -n qbittorrent-4.2.4
cd %{_builddir}/qbittorrent-4.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587603332
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1587603332
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qbittorrent
cp %{_builddir}/qbittorrent-4.2.4/COPYING %{buildroot}/usr/share/package-licenses/qbittorrent/949ae914f4f5d1a0ac5f5d99c36b463cce3c69ca
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/qbittorrent

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.qbittorrent.qBittorrent.desktop
/usr/share/icons/hicolor/128x128/apps/qbittorrent.png
/usr/share/icons/hicolor/128x128/status/qbittorrent-tray.png
/usr/share/icons/hicolor/16x16/apps/qbittorrent.png
/usr/share/icons/hicolor/16x16/status/qbittorrent-tray.png
/usr/share/icons/hicolor/192x192/apps/qbittorrent.png
/usr/share/icons/hicolor/192x192/status/qbittorrent-tray.png
/usr/share/icons/hicolor/22x22/apps/qbittorrent.png
/usr/share/icons/hicolor/22x22/status/qbittorrent-tray.png
/usr/share/icons/hicolor/24x24/apps/qbittorrent.png
/usr/share/icons/hicolor/24x24/status/qbittorrent-tray.png
/usr/share/icons/hicolor/32x32/apps/qbittorrent.png
/usr/share/icons/hicolor/32x32/status/qbittorrent-tray.png
/usr/share/icons/hicolor/36x36/apps/qbittorrent.png
/usr/share/icons/hicolor/36x36/status/qbittorrent-tray.png
/usr/share/icons/hicolor/48x48/apps/qbittorrent.png
/usr/share/icons/hicolor/48x48/status/qbittorrent-tray.png
/usr/share/icons/hicolor/64x64/apps/qbittorrent.png
/usr/share/icons/hicolor/64x64/status/qbittorrent-tray.png
/usr/share/icons/hicolor/72x72/apps/qbittorrent.png
/usr/share/icons/hicolor/72x72/status/qbittorrent-tray.png
/usr/share/icons/hicolor/96x96/apps/qbittorrent.png
/usr/share/icons/hicolor/96x96/status/qbittorrent-tray.png
/usr/share/icons/hicolor/scalable/status/qbittorrent-tray-dark.svg
/usr/share/icons/hicolor/scalable/status/qbittorrent-tray-light.svg
/usr/share/icons/hicolor/scalable/status/qbittorrent-tray.svg
/usr/share/metainfo/org.qbittorrent.qBittorrent.appdata.xml
/usr/share/pixmaps/qbittorrent.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qbittorrent/949ae914f4f5d1a0ac5f5d99c36b463cce3c69ca

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/qbittorrent.1
