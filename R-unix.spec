#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-unix
Version  : 1.5.5
Release  : 37
URL      : https://cran.r-project.org/src/contrib/unix_1.5.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/unix_1.5.5.tar.gz
Summary  : POSIX System Utilities
Group    : Development/Tools
License  : MIT
Requires: R-unix-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
POSIX functions which are not part of the Standard C Library.

%package lib
Summary: lib components for the R-unix package.
Group: Libraries

%description lib
lib components for the R-unix package.


%prep
%setup -q -n unix
cd %{_builddir}/unix

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666102566

%install
export SOURCE_DATE_EPOCH=1666102566
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/unix/DESCRIPTION
/usr/lib64/R/library/unix/INDEX
/usr/lib64/R/library/unix/LICENSE
/usr/lib64/R/library/unix/Meta/Rd.rds
/usr/lib64/R/library/unix/Meta/features.rds
/usr/lib64/R/library/unix/Meta/hsearch.rds
/usr/lib64/R/library/unix/Meta/links.rds
/usr/lib64/R/library/unix/Meta/nsInfo.rds
/usr/lib64/R/library/unix/Meta/package.rds
/usr/lib64/R/library/unix/NAMESPACE
/usr/lib64/R/library/unix/NEWS
/usr/lib64/R/library/unix/R/unix
/usr/lib64/R/library/unix/R/unix.rdb
/usr/lib64/R/library/unix/R/unix.rdx
/usr/lib64/R/library/unix/help/AnIndex
/usr/lib64/R/library/unix/help/aliases.rds
/usr/lib64/R/library/unix/help/paths.rds
/usr/lib64/R/library/unix/help/unix.rdb
/usr/lib64/R/library/unix/help/unix.rdx
/usr/lib64/R/library/unix/html/00Index.html
/usr/lib64/R/library/unix/html/R.css
/usr/lib64/R/library/unix/tests/testthat.R
/usr/lib64/R/library/unix/tests/testthat/test-forking.R
/usr/lib64/R/library/unix/tests/testthat/test-process.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/unix/libs/unix.so
/usr/lib64/R/library/unix/libs/unix.so.avx2
/usr/lib64/R/library/unix/libs/unix.so.avx512
