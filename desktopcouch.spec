Summary:    Integration of CouchDB storage into desktop applications	
Name:       desktopcouch
Version:    0.6.1
Release:    %mkrel 1
License:    LGPLv3
Group:      Databases
URL:        https://launchpad.net/desktopcouch	
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-root
BuildRequires: python
Requires:      couchdb-bin
BuildArch:     noarch

%description
Integration of CouchDB storage into desktop applications, for automatic 
replication and synchronization of data between computers.

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
%{_datadir}/dbus-1/services/org.desktopcouch.CouchDB.service
%{_datadir}/applications/*.desktop
%{py_puresitedir}/%{name}/
%{py_puresitedir}/*.egg-info
%{_bindir}/*
%{_prefix}/lib/%{name}/
%{_mandir}/man1/*
%{_datadir}/%{name}/
