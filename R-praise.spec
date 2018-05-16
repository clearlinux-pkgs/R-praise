#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-praise
Version  : 1.0.0
Release  : 40
URL      : https://cran.rstudio.com/src/contrib/praise_1.0.0.tar.gz
Source0  : https://cran.rstudio.com/src/contrib/praise_1.0.0.tar.gz
Summary  : Praise Users
Group    : Development/Tools
License  : MIT
BuildRequires : clr-R-helpers

%description
praise their users if they have done something
    good, or they just need it to feel better.

%prep
%setup -q -c -n praise

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502417250

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502417250
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library praise
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library praise
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library praise
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/praise/DESCRIPTION
/usr/lib64/R/library/praise/INDEX
/usr/lib64/R/library/praise/LICENSE
/usr/lib64/R/library/praise/Meta/Rd.rds
/usr/lib64/R/library/praise/Meta/features.rds
/usr/lib64/R/library/praise/Meta/hsearch.rds
/usr/lib64/R/library/praise/Meta/links.rds
/usr/lib64/R/library/praise/Meta/nsInfo.rds
/usr/lib64/R/library/praise/Meta/package.rds
/usr/lib64/R/library/praise/NAMESPACE
/usr/lib64/R/library/praise/NEWS.md
/usr/lib64/R/library/praise/R/praise
/usr/lib64/R/library/praise/R/praise.rdb
/usr/lib64/R/library/praise/R/praise.rdx
/usr/lib64/R/library/praise/README.Rmd
/usr/lib64/R/library/praise/README.md
/usr/lib64/R/library/praise/help/AnIndex
/usr/lib64/R/library/praise/help/aliases.rds
/usr/lib64/R/library/praise/help/paths.rds
/usr/lib64/R/library/praise/help/praise.rdb
/usr/lib64/R/library/praise/help/praise.rdx
/usr/lib64/R/library/praise/html/00Index.html
/usr/lib64/R/library/praise/html/R.css
