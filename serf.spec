Summary:	High-performance asynchronous HTTP client library
Name:		serf
Version:	1.3.1
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	http://serf.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	da5aca0cad19fd9c19129c3f8f7393dd
Patch0:		%{name}-scons.patch
URL:		http://code.google.com/p/serf/
BuildRequires:	apr-devel
BuildRequires:	apr-util-devel
BuildRequires:	openssl-devel
BuildRequires:	scons >= 2.3.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The serf library is a C-based HTTP client library built upon the
Apache Portable Runtime (APR) library. It multiplexes connections,
running the read/write communication asynchronously. Memory copies and
transformations are kept to a minimum to provide high performance
operation.

%package devel
Summary:	Header files for serf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	apr-devel
Requires:	apr-util-devel
Requires:	openssl-devel

%description devel
C header files for the serf library.

%prep
%setup -q
%patch0 -p1

%build
%scons
%scons check

%install
rm -rf $RPM_BUILD_ROOT

%scons install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	--install-sandbox=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES NOTICE README
%attr(755,root,root) %ghost %{_libdir}/libserf-1.so.3
%attr(755,root,root) %{_libdir}/libserf-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libserf-1.so
%{_includedir}/serf-1
%{_pkgconfigdir}/serf-1.pc

