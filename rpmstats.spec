Summary:	Gather statistics from installed packages
Summary(pl.UTF-8):	Zbieranie statystyk z zainstalowanych pakietów
Name:		rpmstats
Version:	0.7
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	825473cbff6a7b503c566f440fac7990
URL:		https://svn.mandriva.com/viewvc/soft/rpm/rpmstats/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpm-devel >= 4.4.1
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a program generating statistics about installed packages, and
to work the user needs to install it.

This tool lists, for all the packages installed, the number of days
since one file of the packages have not been accessed. To gather these
data, another tool exists: drakstats, which sends to bugzilla the
output of rpmstats.

%description -l pl.UTF-8
rpmstats zbiera statystyki ostatniego użycia z zainstalowanych
pakietów.

%prep
%setup -q

%build
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
