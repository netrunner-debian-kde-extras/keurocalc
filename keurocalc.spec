# IMPORTANT NOTE:
# This version packages KEuroCalc and curconvd into one single binary package.
# curconvd is a D-Bus currency conversion service (no user interface).
# One could very well package two separate binary packages.
Name:   	keurocalc
Version: 	1.2.1
Release: 	1
Url:		http://opensource.bureau-cornavin.com/keurocalc/index.html
Source0: 	keurocalc-%{version}.tgz

License:  	GPL
Group: 		Graphical desktop/KDE
BuildRoot: 	/tmp/%name-%version-%release
Summary: 	KEuroCalc - A currency converter and calculator


%description
KEuroCalc is a universal currency converter and calculator. It can
convert from and to many currencies, either with a fixed conversion rate or a
variable conversion rate. It directly downloads the latest variable rates
through the Internet.


%prep
%setup -q -n%name-%version
mkdir build


%build
export KDEDIR=/opt/kde4
export QTDIR=/opt/qt4
export LD_LIBRARY_PATH=$QTDIR/lib:$KDEDIR/lib:$LD_LIBRARY_PATH
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH
cd build
cmake -DCMAKE_INSTALL_PREFIX=$KDEDIR ..
make


%install
export KDEDIR=/opt/kde4
export QTDIR=/opt/qt4
export LD_LIBRARY_PATH=$QTDIR/lib:$KDEDIR/lib:$LD_LIBRARY_PATH
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH
cd build
make install DESTDIR=%buildroot


%clean
rm -fr %buildroot


%files
%defattr(-,root,root)

/opt/kde4/bin/keurocalc

/opt/kde4/share/apps/keurocalc/currencies.xml
/opt/kde4/share/apps/keurocalc/splash.png
/opt/kde4/share/applications/kde4/keurocalc.desktop
/opt/kde4/share/icons/hicolor/16x16/apps/keurocalc.png
/opt/kde4/share/icons/hicolor/32x32/apps/keurocalc.png
/opt/kde4/share/icons/hicolor/48x48/apps/keurocalc.png

/opt/kde4/share/locale/bg/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/bs/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/ca/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/ca@valencia/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/cs/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/da/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/de/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/el/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/en_GB/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/es/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/et/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/fi/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/fr/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/ga/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/gl/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/hu/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/it/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/ja/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/ko/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/nb/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/nds/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/nl/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/pl/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/pt_BR/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/pt/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/ru/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/sk/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/sl/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/sr/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/sr@latin/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/sv/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/tr/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/ug/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/uk/LC_MESSAGES/keurocalc.mo
/opt/kde4/share/locale/zh_TW/LC_MESSAGES/keurocalc.mo

%dir /opt/kde4/share/doc/HTML/en/keurocalc/
%doc /opt/kde4/share/doc/HTML/en/keurocalc/common
%doc /opt/kde4/share/doc/HTML/en/keurocalc/index.cache.bz2
%doc /opt/kde4/share/doc/HTML/en/keurocalc/index.docbook
%doc /opt/kde4/share/doc/HTML/en/keurocalc/screenshot.png
%doc /opt/kde4/share/doc/HTML/en/keurocalc/settings.png

%dir /opt/kde4/share/doc/HTML/da/keurocalc/
%doc /opt/kde4/share/doc/HTML/da/keurocalc/common
%doc /opt/kde4/share/doc/HTML/da/keurocalc/index.cache.bz2
%doc /opt/kde4/share/doc/HTML/da/keurocalc/index.docbook
%doc /opt/kde4/share/doc/HTML/da/keurocalc/screenshot.png
%doc /opt/kde4/share/doc/HTML/da/keurocalc/settings.png

%dir /opt/kde4/share/doc/HTML/es/keurocalc/
%doc /opt/kde4/share/doc/HTML/es/keurocalc/common
%doc /opt/kde4/share/doc/HTML/es/keurocalc/index.cache.bz2
%doc /opt/kde4/share/doc/HTML/es/keurocalc/index.docbook
%doc /opt/kde4/share/doc/HTML/es/keurocalc/screenshot.png
%doc /opt/kde4/share/doc/HTML/es/keurocalc/settings.png

%dir /opt/kde4/share/doc/HTML/et/keurocalc/
%doc /opt/kde4/share/doc/HTML/et/keurocalc/common
%doc /opt/kde4/share/doc/HTML/et/keurocalc/index.cache.bz2
%doc /opt/kde4/share/doc/HTML/et/keurocalc/index.docbook
%doc /opt/kde4/share/doc/HTML/et/keurocalc/screenshot.png
%doc /opt/kde4/share/doc/HTML/et/keurocalc/settings.png

%dir /opt/kde4/share/doc/HTML/fr/keurocalc/
%doc /opt/kde4/share/doc/HTML/fr/keurocalc/common
%doc /opt/kde4/share/doc/HTML/fr/keurocalc/index.cache.bz2
%doc /opt/kde4/share/doc/HTML/fr/keurocalc/index.docbook
%doc /opt/kde4/share/doc/HTML/fr/keurocalc/screenshot.png
%doc /opt/kde4/share/doc/HTML/fr/keurocalc/settings.png

%dir /opt/kde4/share/doc/HTML/it/keurocalc/
%doc /opt/kde4/share/doc/HTML/it/keurocalc/common
%doc /opt/kde4/share/doc/HTML/it/keurocalc/index.cache.bz2
%doc /opt/kde4/share/doc/HTML/it/keurocalc/index.docbook
%doc /opt/kde4/share/doc/HTML/it/keurocalc/screenshot.png
%doc /opt/kde4/share/doc/HTML/it/keurocalc/settings.png

%dir /opt/kde4/share/doc/HTML/nb/keurocalc/
%doc /opt/kde4/share/doc/HTML/nb/keurocalc/common
%doc /opt/kde4/share/doc/HTML/nb/keurocalc/index.cache.bz2
%doc /opt/kde4/share/doc/HTML/nb/keurocalc/index.docbook
%doc /opt/kde4/share/doc/HTML/nb/keurocalc/screenshot.png
%doc /opt/kde4/share/doc/HTML/nb/keurocalc/settings.png

%dir /opt/kde4/share/doc/HTML/nl/keurocalc/
%doc /opt/kde4/share/doc/HTML/nl/keurocalc/common
%doc /opt/kde4/share/doc/HTML/nl/keurocalc/index.cache.bz2
%doc /opt/kde4/share/doc/HTML/nl/keurocalc/index.docbook
%doc /opt/kde4/share/doc/HTML/nl/keurocalc/screenshot.png
%doc /opt/kde4/share/doc/HTML/nl/keurocalc/settings.png

%dir /opt/kde4/share/doc/HTML/pt/keurocalc/
%doc /opt/kde4/share/doc/HTML/pt/keurocalc/common
%doc /opt/kde4/share/doc/HTML/pt/keurocalc/index.cache.bz2
%doc /opt/kde4/share/doc/HTML/pt/keurocalc/index.docbook
%doc /opt/kde4/share/doc/HTML/pt/keurocalc/screenshot.png
%doc /opt/kde4/share/doc/HTML/pt/keurocalc/settings.png

%dir /opt/kde4/share/doc/HTML/pt_BR/keurocalc/
%doc /opt/kde4/share/doc/HTML/pt_BR/keurocalc/common
%doc /opt/kde4/share/doc/HTML/pt_BR/keurocalc/index.cache.bz2
%doc /opt/kde4/share/doc/HTML/pt_BR/keurocalc/index.docbook
%doc /opt/kde4/share/doc/HTML/pt_BR/keurocalc/screenshot.png
%doc /opt/kde4/share/doc/HTML/pt_BR/keurocalc/settings.png

%dir /opt/kde4/share/doc/HTML/sv/keurocalc/
%doc /opt/kde4/share/doc/HTML/sv/keurocalc/common
%doc /opt/kde4/share/doc/HTML/sv/keurocalc/index.cache.bz2
%doc /opt/kde4/share/doc/HTML/sv/keurocalc/index.docbook
%doc /opt/kde4/share/doc/HTML/sv/keurocalc/screenshot.png
%doc /opt/kde4/share/doc/HTML/sv/keurocalc/settings.png

%dir /opt/kde4/share/doc/HTML/uk/keurocalc/
%doc /opt/kde4/share/doc/HTML/uk/keurocalc/common
%doc /opt/kde4/share/doc/HTML/uk/keurocalc/index.cache.bz2
%doc /opt/kde4/share/doc/HTML/uk/keurocalc/index.docbook
%doc /opt/kde4/share/doc/HTML/uk/keurocalc/screenshot.png
%doc /opt/kde4/share/doc/HTML/uk/keurocalc/settings.png

/opt/kde4/bin/curconvd

/opt/kde4/share/apps/curconvd/currencies.xml

/opt/kde4/share/locale/bs/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/ca/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/ca@valencia/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/cs/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/da/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/de/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/el/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/en_GB/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/es/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/et/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/fi/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/fr/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/ga/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/gl/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/hu/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/it/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/ko/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/nb/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/nds/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/nl/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/pl/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/pt_BR/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/pt/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/sk/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/sl/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/sr/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/sr@latin/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/sv/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/tr/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/uk/LC_MESSAGES/curconvd.mo
/opt/kde4/share/locale/zh_TW/LC_MESSAGES/curconvd.mo

