Summary:	i810switch - for switching the LCD and external VGA displays on and off
Summary(pl.UTF-8):	i810switch - program do przełączania wyświetlacza LCD i zewnętrznego VGA
Name:		i810switch
Version:	0.6.5
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www16.plala.or.jp/mano-a-mano/i810switch/%{name}-%{version}.tar.gz
# Source0-md5:	5ca07aee624589bdce5761c796e5f9a8
URL:		http://www16.plala.or.jp/mano-a-mano/i810switch.html	
Requires:	pciutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
i810switch is a utility (for intel graphic cards) for switching the LCD
and external VGA displays on and off under Linux.

%description -l pl.UTF-8
i810switch to narzędzie do kart graficznych Intela do włączania i
wyłączania wyświetlacza LCD oraz zewnętrznego VGA pod Linuksem.

%prep
%setup -q
# Remove binaries supplied with sources:
%{__make} clean

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/i810*
