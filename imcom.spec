
%include	/usr/lib/rpm/macros.python

Summary:	Command-line Jabber client
Summary(pl):	Tekstowy klient Jabbera
Name:		imcom
Version:	0.95
Release:	1
License:	BSD
Group:		Applications/Communications
Source0:	http://imcom.floobin.cx/src/%{name}-%{version}.tar.gz
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
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{py_sitedir}/%{name}}
install *.py $RPM_BUILD_ROOT%{py_sitedir}/%{name}

echo %{name} > $RPM_BUILD_ROOT%{py_sitedir}/%{name}.pth

cat <<END > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh

exec python -O %{py_sitedir}/%{name}/CLI.pyo

END

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html CONTRIBUTORS README* LICENSE TODO WHATSNEW
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/%{name}
%{py_sitedir}/%{name}/*.py[co]
%{py_sitedir}/%{name}.pth
