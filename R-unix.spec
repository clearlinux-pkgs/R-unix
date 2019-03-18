#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-unix
Version  : 1.5
Release  : 8
URL      : https://cran.r-project.org/src/contrib/unix_1.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/unix_1.5.tar.gz
Summary  : POSIX System Utilities
Group    : Development/Tools
License  : MIT
Requires: R-unix-lib = %{version}-%{release}
BuildRequires : R-assertthat
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
POSIX functions which are not part of the Standard C Library.

%package lib
Summary: lib components for the R-unix package.
Group: Libraries

%description lib
lib components for the R-unix package.


%prep
%setup -q -c -n unix

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552923935

%install
export SOURCE_DATE_EPOCH=1552923935
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library unix
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library unix
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library unix
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  unix || :


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
