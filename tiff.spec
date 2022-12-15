#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tiff
Version  : 4.5.0
Release  : 58
URL      : https://gitlab.com/libtiff/libtiff/-/archive/v4.5.0/libtiff-v4.5.0.tar.gz
Source0  : https://gitlab.com/libtiff/libtiff/-/archive/v4.5.0/libtiff-v4.5.0.tar.gz
Summary  : Tag Image File Format (TIFF) library.
Group    : Development/Tools
License  : libtiff
Requires: tiff-bin = %{version}-%{release}
Requires: tiff-lib = %{version}-%{release}
Requires: tiff-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libjpeg-turbo-dev
BuildRequires : libwebp-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : pypi-sphinx
BuildRequires : xz-dev
BuildRequires : zlib-dev
BuildRequires : zstd-dev

%description
This directory contains various contributions from libtiff users.

%package bin
Summary: bin components for the tiff package.
Group: Binaries

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

%description lib
lib components for the tiff package.


%package lib32
Summary: lib32 components for the tiff package.
Group: Default

%description lib32
lib32 components for the tiff package.


%package man
Summary: man components for the tiff package.
Group: Default

%description man
man components for the tiff package.


%prep
%setup -q -n libtiff-v4.5.0
cd %{_builddir}/libtiff-v4.5.0
pushd ..
cp -a libtiff-v4.5.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671134880
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition "
%reconfigure --disable-static --with-docdir=/usr/share/doc/tiff
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure --disable-static --with-docdir=/usr/share/doc/tiff  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
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
export SOURCE_DATE_EPOCH=1671134880
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
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
/usr/share/man/man3/TIFFAccessTagMethods.3tiff
/usr/share/man/man3/TIFFClientInfo.3tiff
/usr/share/man/man3/TIFFClose.3tiff
/usr/share/man/man3/TIFFCreateDirectory.3tiff
/usr/share/man/man3/TIFFCustomDirectory.3tiff
/usr/share/man/man3/TIFFCustomTagList.3tiff
/usr/share/man/man3/TIFFDataWidth.3tiff
/usr/share/man/man3/TIFFDeferStrileArrayWriting.3tiff
/usr/share/man/man3/TIFFError.3tiff
/usr/share/man/man3/TIFFFieldDataType.3tiff
/usr/share/man/man3/TIFFFieldName.3tiff
/usr/share/man/man3/TIFFFieldPassCount.3tiff
/usr/share/man/man3/TIFFFieldQuery.3tiff
/usr/share/man/man3/TIFFFieldReadCount.3tiff
/usr/share/man/man3/TIFFFieldTag.3tiff
/usr/share/man/man3/TIFFFieldWriteCount.3tiff
/usr/share/man/man3/TIFFFlush.3tiff
/usr/share/man/man3/TIFFGetField.3tiff
/usr/share/man/man3/TIFFMergeFieldInfo.3tiff
/usr/share/man/man3/TIFFOpen.3tiff
/usr/share/man/man3/TIFFPrintDirectory.3tiff
/usr/share/man/man3/TIFFProcFunctions.3tiff
/usr/share/man/man3/TIFFRGBAImage.3tiff
/usr/share/man/man3/TIFFReadDirectory.3tiff
/usr/share/man/man3/TIFFReadEncodedStrip.3tiff
/usr/share/man/man3/TIFFReadEncodedTile.3tiff
/usr/share/man/man3/TIFFReadFromUserBuffer.3tiff
/usr/share/man/man3/TIFFReadRGBAImage.3tiff
/usr/share/man/man3/TIFFReadRGBAStrip.3tiff
/usr/share/man/man3/TIFFReadRGBATile.3tiff
/usr/share/man/man3/TIFFReadRawStrip.3tiff
/usr/share/man/man3/TIFFReadRawTile.3tiff
/usr/share/man/man3/TIFFReadScanline.3tiff
/usr/share/man/man3/TIFFReadTile.3tiff
/usr/share/man/man3/TIFFSetDirectory.3tiff
/usr/share/man/man3/TIFFSetField.3tiff
/usr/share/man/man3/TIFFSetTagExtender.3tiff
/usr/share/man/man3/TIFFStrileQuery.3tiff
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
/usr/share/man/man3/_TIFFRewriteField.3tiff
/usr/share/man/man3/_TIFFauxiliary.3tiff
/usr/share/man/man3/libtiff.3tiff

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libtiff.so
/usr/lib32/libtiffxx.so
/usr/lib32/pkgconfig/32libtiff-4.pc
/usr/lib32/pkgconfig/libtiff-4.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/tiff/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtiff.so.6
/usr/lib64/libtiff.so.6.0.0
/usr/lib64/libtiffxx.so.6
/usr/lib64/libtiffxx.so.6.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libtiff.so.6
/usr/lib32/libtiff.so.6.0.0
/usr/lib32/libtiffxx.so.6
/usr/lib32/libtiffxx.so.6.0.0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fax2ps.1
/usr/share/man/man1/fax2tiff.1
/usr/share/man/man1/pal2rgb.1
/usr/share/man/man1/ppm2tiff.1
/usr/share/man/man1/raw2tiff.1
/usr/share/man/man1/rgb2ycbcr.1
/usr/share/man/man1/thumbnail.1
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
