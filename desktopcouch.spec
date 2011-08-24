Summary:    Integration of CouchDB storage into desktop applications	
Name:       desktopcouch
Version:    1.0.7
Release:    %mkrel 2
License:    LGPLv3
Group:      Databases
URL:        https://launchpad.net/desktopcouch	
Source0:    http://launchpad.net/desktopcouch/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires: python python-setuptools
BuildRequires: python-distutils-extra
BuildRequires: intltool 
Requires:      couchdb-bin
Requires:      python-couchdb
Requires:      python-oauth
Requires:      python-twisted-core
BuildArch:     noarch

%description
Integration of CouchDB storage into desktop applications, for automatic 
replication and synchronization of data between computers.

%package tools
Requires:   pygtk2.0
Group:      Databases
Summary: Desktopcouch tools 
%description tools
This package contains graphical tools for desktopcouch, to pair two computers.

%prep
%setup -q

%build
python setup.py build

%install
rm -Rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT

rm -Rf $RPM_BUILD_ROOT/%{_docdir}/
%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/xdg/desktop-couch/compulsory-auth.ini
%dir %{_sysconfdir}/xdg/desktop-couch
%{_datadir}/dbus-1/services/org.desktopcouch.CouchDB.service
%{py_puresitedir}/%{name}/
%{py_puresitedir}/*.egg-info
%{_prefix}/lib/%{name}/
%{_datadir}/%{name}/

%files tools
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop

