Summary:	Gather statistics from installed packages
Summary(pl):	Zbiera statystyki z zainstalowanych pakiet�w
Name:		rpmstats
Version:	0.4
Release:	1
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	87552e75254ea73ef569f22472d888a6
License:	GPL
Group:		Applications/System
BuildRequires:	rpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rpmstats retrieves statistics about installed packages.

%description -l pl
rpmstats zbiera statystyki ostatniego u�ycia z zainstalowanych pakiet�w.

%prep
%setup -q

%build
CPPFLAGS="%{rpmcflags} -DRPM_42"
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	libexecdir=$RPM_BUILD_ROOT%{_libdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/%{name}
%{_mandir}/man?/*