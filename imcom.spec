
%define		beta beta10
%include	/usr/lib/rpm/macros.python
Summary:	Command-line Jabber client
Summary(pl):	Tekstowy klient Jabbera
Name:		imcom
Version:	1.30
Release:	1.%{beta}
License:	BSD
Group:		Applications/Communications
Source0:	http://nafai.dyndns.org/files/imcom-betas/%{name}-%{version}%{beta}.tar.gz
# Source0-md5:	f2ce69c87b5f75d741b135ec26523073
Patch0:		%{name}-ac_python_import_check.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://imcom.floobin.cx/
BuildRequires:	python >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IMCom is a command-line Jabber client.

%description -l pl
Tekstowy klient Jabbera.

%prep
%setup -qn %{name}-%{version}%{beta}
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure
%{__make}

rm -f docs/CHANGELOG

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

%{py_comp} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS README* LICENSE TODO WHATSNEW docs
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py[co]
%attr(755,root,root) %{_datadir}/%{name}/CLI.py
%attr(755,root,root) %{_datadir}/%{name}/AccountCreator.py
%{_mandir}/man1/%{name}*
