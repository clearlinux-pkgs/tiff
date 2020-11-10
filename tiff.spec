#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tiff
Version  : v4.0.10
Release  : 51
URL      : https://gitlab.com/libtiff/libtiff/-/archive/v4.0.10/libtiff-v4.0.10.tar.gz
Source0  : https://gitlab.com/libtiff/libtiff/-/archive/v4.0.10/libtiff-v4.0.10.tar.gz
Summary  : Tag Image File Format (TIFF) library.
Group    : Development/Tools
License  : libtiff
Requires: tiff-bin = %{version}-%{release}
Requires: tiff-lib = %{version}-%{release}
Requires: tiff-license = %{version}-%{release}
Requires: tiff-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-scons
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libjpeg-turbo-dev
BuildRequires : libwebp-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(zlib)
BuildRequires : xz-dev
BuildRequires : zlib-dev
BuildRequires : zstd-dev
Patch1: CVE-2018-12900.patch
Patch2: CVE-2018-19210.patch
Patch3: CVE-2019-6128.patch
Patch4: CVE-2019-7663.patch
Patch5: CVE-2019-14973.patch
Patch6: CVE-2019-17546.patch

%description
This directory contains various contributions from libtiff users.

%package bin
Summary: bin components for the tiff package.
Group: Binaries
Requires: tiff-license = %{version}-%{release}

%description bin
bin components for the tiff package.


%package dev
Summary: dev components for the tiff package.
Group: Development
Requires: tiff-lib = %{version}-%{release}
Requires: tiff-bin = %{version}-%{release}
Provides: tiff-devel = %{version}-%{release}
Requires: tiff = %{version}-%{release}

%description dev
dev components for the tiff package.


%package dev32
Summary: dev32 components for the tiff package.
Group: Default
Requires: tiff-lib32 = %{version}-%{release}
Requires: tiff-bin = %{version}-%{release}
Requires: tiff-dev = %{version}-%{release}

%description dev32
dev32 components for the tiff package.


%package doc
Summary: doc components for the tiff package.
Group: Documentation
Requires: tiff-man = %{version}-%{release}

%description doc
doc components for the tiff package.


%package lib
Summary: lib components for the tiff package.
Group: Libraries
Requires: tiff-license = %{version}-%{release}

%description lib
lib components for the tiff package.


%package lib32
Summary: lib32 components for the tiff package.
Group: Default
Requires: tiff-license = %{version}-%{release}

%description lib32
lib32 components for the tiff package.


%package license
Summary: license components for the tiff package.
Group: Default

%description license
license components for the tiff package.


%package man
Summary: man components for the tiff package.
Group: Default

%description man
man components for the tiff package.


%prep
%setup -q -n libtiff-v4.0.10
cd %{_builddir}/libtiff-v4.0.10
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
pushd ..
cp -a libtiff-v4.0.10 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605031532
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%reconfigure --disable-static
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1605031532
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tiff
cp %{_builddir}/libtiff-v4.0.10/COPYRIGHT %{buildroot}/usr/share/package-licenses/tiff/a2f64f2a85f5fd34bda8eb713c3aad008adbb589
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fax2ps
/usr/bin/fax2tiff
/usr/bin/pal2rgb
/usr/bin/ppm2tiff
/usr/bin/raw2tiff
/usr/bin/tiff2bw
/usr/bin/tiff2pdf
/usr/bin/tiff2ps
/usr/bin/tiff2rgba
/usr/bin/tiffcmp
/usr/bin/tiffcp
/usr/bin/tiffcrop
/usr/bin/tiffdither
/usr/bin/tiffdump
/usr/bin/tiffinfo
/usr/bin/tiffmedian
/usr/bin/tiffset
/usr/bin/tiffsplit

%files dev
%defattr(-,root,root,-)
/usr/include/tiff.h
/usr/include/tiffconf.h
/usr/include/tiffio.h
/usr/include/tiffio.hxx
/usr/include/tiffvers.h
/usr/lib64/libtiff.so
/usr/lib64/libtiffxx.so
/usr/lib64/pkgconfig/libtiff-4.pc
/usr/share/man/man3/TIFFClose.3tiff
/usr/share/man/man3/TIFFDataWidth.3tiff
/usr/share/man/man3/TIFFError.3tiff
/usr/share/man/man3/TIFFFieldDataType.3tiff
/usr/share/man/man3/TIFFFieldName.3tiff
/usr/share/man/man3/TIFFFieldPassCount.3tiff
/usr/share/man/man3/TIFFFieldReadCount.3tiff
/usr/share/man/man3/TIFFFieldTag.3tiff
/usr/share/man/man3/TIFFFieldWriteCount.3tiff
/usr/share/man/man3/TIFFFlush.3tiff
/usr/share/man/man3/TIFFGetField.3tiff
/usr/share/man/man3/TIFFOpen.3tiff
/usr/share/man/man3/TIFFPrintDirectory.3tiff
/usr/share/man/man3/TIFFRGBAImage.3tiff
/usr/share/man/man3/TIFFReadDirectory.3tiff
/usr/share/man/man3/TIFFReadEncodedStrip.3tiff
/usr/share/man/man3/TIFFReadEncodedTile.3tiff
/usr/share/man/man3/TIFFReadRGBAImage.3tiff
/usr/share/man/man3/TIFFReadRGBAStrip.3tiff
/usr/share/man/man3/TIFFReadRGBATile.3tiff
/usr/share/man/man3/TIFFReadRawStrip.3tiff
/usr/share/man/man3/TIFFReadRawTile.3tiff
/usr/share/man/man3/TIFFReadScanline.3tiff
/usr/share/man/man3/TIFFReadTile.3tiff
/usr/share/man/man3/TIFFSetDirectory.3tiff
/usr/share/man/man3/TIFFSetField.3tiff
/usr/share/man/man3/TIFFWarning.3tiff
/usr/share/man/man3/TIFFWriteDirectory.3tiff
/usr/share/man/man3/TIFFWriteEncodedStrip.3tiff
/usr/share/man/man3/TIFFWriteEncodedTile.3tiff
/usr/share/man/man3/TIFFWriteRawStrip.3tiff
/usr/share/man/man3/TIFFWriteRawTile.3tiff
/usr/share/man/man3/TIFFWriteScanline.3tiff
/usr/share/man/man3/TIFFWriteTile.3tiff
/usr/share/man/man3/TIFFbuffer.3tiff
/usr/share/man/man3/TIFFcodec.3tiff
/usr/share/man/man3/TIFFcolor.3tiff
/usr/share/man/man3/TIFFmemory.3tiff
/usr/share/man/man3/TIFFquery.3tiff
/usr/share/man/man3/TIFFsize.3tiff
/usr/share/man/man3/TIFFstrip.3tiff
/usr/share/man/man3/TIFFswab.3tiff
/usr/share/man/man3/TIFFtile.3tiff
/usr/share/man/man3/libtiff.3tiff

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libtiff.so
/usr/lib32/libtiffxx.so
/usr/lib32/pkgconfig/32libtiff-4.pc
/usr/lib32/pkgconfig/libtiff-4.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/tiff-4.0.10/COPYRIGHT
/usr/share/doc/tiff-4.0.10/ChangeLog
/usr/share/doc/tiff-4.0.10/README.md
/usr/share/doc/tiff-4.0.10/RELEASE-DATE
/usr/share/doc/tiff-4.0.10/TODO
/usr/share/doc/tiff-4.0.10/VERSION
/usr/share/doc/tiff-4.0.10/html/TIFFTechNote2.html
/usr/share/doc/tiff-4.0.10/html/addingtags.html
/usr/share/doc/tiff-4.0.10/html/bugs.html
/usr/share/doc/tiff-4.0.10/html/build.html
/usr/share/doc/tiff-4.0.10/html/contrib.html
/usr/share/doc/tiff-4.0.10/html/document.html
/usr/share/doc/tiff-4.0.10/html/images.html
/usr/share/doc/tiff-4.0.10/html/images/back.gif
/usr/share/doc/tiff-4.0.10/html/images/bali.jpg
/usr/share/doc/tiff-4.0.10/html/images/cat.gif
/usr/share/doc/tiff-4.0.10/html/images/cover.jpg
/usr/share/doc/tiff-4.0.10/html/images/cramps.gif
/usr/share/doc/tiff-4.0.10/html/images/dave.gif
/usr/share/doc/tiff-4.0.10/html/images/info.gif
/usr/share/doc/tiff-4.0.10/html/images/jello.jpg
/usr/share/doc/tiff-4.0.10/html/images/jim.gif
/usr/share/doc/tiff-4.0.10/html/images/note.gif
/usr/share/doc/tiff-4.0.10/html/images/oxford.gif
/usr/share/doc/tiff-4.0.10/html/images/quad.jpg
/usr/share/doc/tiff-4.0.10/html/images/ring.gif
/usr/share/doc/tiff-4.0.10/html/images/smallliz.jpg
/usr/share/doc/tiff-4.0.10/html/images/strike.gif
/usr/share/doc/tiff-4.0.10/html/images/warning.gif
/usr/share/doc/tiff-4.0.10/html/index.html
/usr/share/doc/tiff-4.0.10/html/internals.html
/usr/share/doc/tiff-4.0.10/html/intro.html
/usr/share/doc/tiff-4.0.10/html/libtiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFClose.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFDataWidth.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFError.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFFieldDataType.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFFieldName.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFFieldPassCount.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFFieldReadCount.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFFieldTag.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFFieldWriteCount.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFFlush.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFGetField.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFOpen.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFPrintDirectory.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFRGBAImage.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFReadDirectory.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFReadEncodedStrip.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFReadEncodedTile.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFReadRGBAImage.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFReadRGBAStrip.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFReadRGBATile.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFReadRawStrip.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFReadRawTile.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFReadScanline.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFReadTile.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFSetDirectory.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFSetField.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFWarning.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFWriteDirectory.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFWriteEncodedStrip.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFWriteEncodedTile.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFWriteRawStrip.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFWriteRawTile.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFWriteScanline.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFWriteTile.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFbuffer.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFcodec.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFcolor.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFmemory.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFquery.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFsize.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFstrip.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFswab.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/TIFFtile.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/fax2ps.1.html
/usr/share/doc/tiff-4.0.10/html/man/fax2tiff.1.html
/usr/share/doc/tiff-4.0.10/html/man/index.html
/usr/share/doc/tiff-4.0.10/html/man/libtiff.3tiff.html
/usr/share/doc/tiff-4.0.10/html/man/pal2rgb.1.html
/usr/share/doc/tiff-4.0.10/html/man/ppm2tiff.1.html
/usr/share/doc/tiff-4.0.10/html/man/raw2tiff.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiff2bw.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiff2pdf.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiff2ps.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiff2rgba.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiffcmp.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiffcp.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiffcrop.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiffdither.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiffdump.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiffgt.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiffinfo.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiffmedian.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiffset.1.html
/usr/share/doc/tiff-4.0.10/html/man/tiffsplit.1.html
/usr/share/doc/tiff-4.0.10/html/misc.html
/usr/share/doc/tiff-4.0.10/html/support.html
/usr/share/doc/tiff-4.0.10/html/tools.html
/usr/share/doc/tiff-4.0.10/html/v3.4beta007.html
/usr/share/doc/tiff-4.0.10/html/v3.4beta016.html
/usr/share/doc/tiff-4.0.10/html/v3.4beta018.html
/usr/share/doc/tiff-4.0.10/html/v3.4beta024.html
/usr/share/doc/tiff-4.0.10/html/v3.4beta028.html
/usr/share/doc/tiff-4.0.10/html/v3.4beta029.html
/usr/share/doc/tiff-4.0.10/html/v3.4beta031.html
/usr/share/doc/tiff-4.0.10/html/v3.4beta032.html
/usr/share/doc/tiff-4.0.10/html/v3.4beta033.html
/usr/share/doc/tiff-4.0.10/html/v3.4beta034.html
/usr/share/doc/tiff-4.0.10/html/v3.4beta035.html
/usr/share/doc/tiff-4.0.10/html/v3.4beta036.html
/usr/share/doc/tiff-4.0.10/html/v3.5.1.html
/usr/share/doc/tiff-4.0.10/html/v3.5.2.html
/usr/share/doc/tiff-4.0.10/html/v3.5.3.html
/usr/share/doc/tiff-4.0.10/html/v3.5.4.html
/usr/share/doc/tiff-4.0.10/html/v3.5.5.html
/usr/share/doc/tiff-4.0.10/html/v3.5.6-beta.html
/usr/share/doc/tiff-4.0.10/html/v3.5.7.html
/usr/share/doc/tiff-4.0.10/html/v3.6.0.html
/usr/share/doc/tiff-4.0.10/html/v3.6.1.html
/usr/share/doc/tiff-4.0.10/html/v3.7.0.html
/usr/share/doc/tiff-4.0.10/html/v3.7.0alpha.html
/usr/share/doc/tiff-4.0.10/html/v3.7.0beta.html
/usr/share/doc/tiff-4.0.10/html/v3.7.0beta2.html
/usr/share/doc/tiff-4.0.10/html/v3.7.1.html
/usr/share/doc/tiff-4.0.10/html/v3.7.2.html
/usr/share/doc/tiff-4.0.10/html/v3.7.3.html
/usr/share/doc/tiff-4.0.10/html/v3.7.4.html
/usr/share/doc/tiff-4.0.10/html/v3.8.0.html
/usr/share/doc/tiff-4.0.10/html/v3.8.1.html
/usr/share/doc/tiff-4.0.10/html/v3.8.2.html
/usr/share/doc/tiff-4.0.10/html/v3.9.0beta.html
/usr/share/doc/tiff-4.0.10/html/v3.9.1.html
/usr/share/doc/tiff-4.0.10/html/v3.9.2.html
/usr/share/doc/tiff-4.0.10/html/v4.0.0.html
/usr/share/doc/tiff-4.0.10/html/v4.0.1.html
/usr/share/doc/tiff-4.0.10/html/v4.0.10.html
/usr/share/doc/tiff-4.0.10/html/v4.0.2.html
/usr/share/doc/tiff-4.0.10/html/v4.0.3.html
/usr/share/doc/tiff-4.0.10/html/v4.0.4.html
/usr/share/doc/tiff-4.0.10/html/v4.0.4beta.html
/usr/share/doc/tiff-4.0.10/html/v4.0.5.html
/usr/share/doc/tiff-4.0.10/html/v4.0.6.html
/usr/share/doc/tiff-4.0.10/html/v4.0.7.html
/usr/share/doc/tiff-4.0.10/html/v4.0.8.html
/usr/share/doc/tiff-4.0.10/html/v4.0.9.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtiff.so.5
/usr/lib64/libtiff.so.5.4.0
/usr/lib64/libtiffxx.so.5
/usr/lib64/libtiffxx.so.5.4.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libtiff.so.5
/usr/lib32/libtiff.so.5.4.0
/usr/lib32/libtiffxx.so.5
/usr/lib32/libtiffxx.so.5.4.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tiff/a2f64f2a85f5fd34bda8eb713c3aad008adbb589

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fax2ps.1
/usr/share/man/man1/fax2tiff.1
/usr/share/man/man1/pal2rgb.1
/usr/share/man/man1/ppm2tiff.1
/usr/share/man/man1/raw2tiff.1
/usr/share/man/man1/tiff2bw.1
/usr/share/man/man1/tiff2pdf.1
/usr/share/man/man1/tiff2ps.1
/usr/share/man/man1/tiff2rgba.1
/usr/share/man/man1/tiffcmp.1
/usr/share/man/man1/tiffcp.1
/usr/share/man/man1/tiffcrop.1
/usr/share/man/man1/tiffdither.1
/usr/share/man/man1/tiffdump.1
/usr/share/man/man1/tiffgt.1
/usr/share/man/man1/tiffinfo.1
/usr/share/man/man1/tiffmedian.1
/usr/share/man/man1/tiffset.1
/usr/share/man/man1/tiffsplit.1
