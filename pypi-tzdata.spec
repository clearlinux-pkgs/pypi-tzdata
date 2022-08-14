#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-tzdata
Version  : 2022.2
Release  : 12
URL      : https://files.pythonhosted.org/packages/3e/eb/a00286433c739bb1a0d83a069b2dc379a5d14b0b9c927e3cb00cb434d740/tzdata-2022.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/3e/eb/a00286433c739bb1a0d83a069b2dc379a5d14b0b9c927e3cb00cb434d740/tzdata-2022.2.tar.gz
Summary  : Provider of IANA time zone data
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-tzdata-license = %{version}-%{release}
Requires: pypi-tzdata-python = %{version}-%{release}
Requires: pypi-tzdata-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
tzdata: Python package providing IANA time zone data
====================================================

%package license
Summary: license components for the pypi-tzdata package.
Group: Default

%description license
license components for the pypi-tzdata package.


%package python
Summary: python components for the pypi-tzdata package.
Group: Default
Requires: pypi-tzdata-python3 = %{version}-%{release}

%description python
python components for the pypi-tzdata package.


%package python3
Summary: python3 components for the pypi-tzdata package.
Group: Default
Requires: python3-core
Provides: pypi(tzdata)

%description python3
python3 components for the pypi-tzdata package.


%prep
%setup -q -n tzdata-2022.2
cd %{_builddir}/tzdata-2022.2
pushd ..
cp -a tzdata-2022.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660335829
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tzdata
cp %{_builddir}/tzdata-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tzdata/a17821d024ce62859b8750020c3b7cbb2e6a57af
cp %{_builddir}/tzdata-%{version}/licenses/LICENSE_APACHE %{buildroot}/usr/share/package-licenses/pypi-tzdata/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tzdata/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/pypi-tzdata/a17821d024ce62859b8750020c3b7cbb2e6a57af

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
