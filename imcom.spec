Summary:	Command-Line Jabber client
Summary(pl):	Tekstowy klient Jabbera
Name:		imcom
Version:	0.85
Release:	1
License:	distributable
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://imcom.floobin.cx/src/%{name}-%{version}.tar.gz
Patch0:		%{name}-FHS.patch
Requires:	python
URL:		http://imcom.floobin.cx/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is User Directory module for Jabber. 

%description -l pl
Modu³ ten umo¿liwia rejestrowanie i przeszukiwanie danych o u¿ytkownikach
systemu Jabber.

%prep
%setup -qn %{name}
%patch0 -p1

%build
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
%{__make} install DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf CONTRIBUTORS README* LICENSE TODO WHATSNEW

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz *.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
