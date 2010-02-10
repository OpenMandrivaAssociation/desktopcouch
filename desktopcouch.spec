Summary:    TODO	
Name:		desktopcouch
Version:	0.6.1
Release: 	%mkrel 1
License:	TODO
Group:		TODO
URL:	    https://launchpad.net/desktopcouch	
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root

%description
TODO
%prep

%setup -q
%build
python setup.py build

%install
rm -Rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

