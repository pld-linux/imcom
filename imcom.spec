
Summary:	Command-line Jabber client
Summary(pl):	Tekstowy klient Jabbera
Name:		imcom
Version:	1.33
Release:	4
License:	BSD
Group:		Applications/Communications
Source0:	http://nafai.dyndns.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	37258996233ba8a3a3bdcbab179adf70
Patch0:		%{name}-ac_python_import_check.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-presence.patch
URL:		http://imcom.floobin.cx/
BuildRequires:	autoconf
BuildRequires:	rpm-pythonprov >= 4.2-0.20030322.3
%pyrequires_eq	python-modules
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IMCom is a command-line Jabber client.

%description -l pl
Tekstowy klient Jabbera.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/docs
rm -f docs/CHANGELOG docs/imcom.1

%{py_comp} $RPM_BUILD_ROOT%{_datadir}/%{name}
%{py_ocomp} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS README* LICENSE TODO WHATSNEW docs
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/modules
%{_datadir}/%{name}/*.py[co]
%{_datadir}/%{name}/modules/*.py[co]
%attr(755,root,root) %{_datadir}/%{name}/CLI.py
%attr(755,root,root) %{_datadir}/%{name}/AccountCreator.py
%{_mandir}/man1/%{name}*
