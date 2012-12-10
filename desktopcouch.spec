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



%changelog
* Wed Aug 24 2011 Michael Scherer <misc@mandriva.org> 1.0.7-2mdv2012.0
+ Revision: 696513
- fix missing directory

* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 1.0.7-1
+ Revision: 672660
- new version 1.0.7
- new verrsion 0.6.9b

* Sun Nov 07 2010 Jani Välimaa <wally@mandriva.org> 0.6.6-4mdv2011.0
+ Revision: 594760
- rebuild for python 2.7

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Tue Aug 17 2010 Michael Scherer <misc@mandriva.org> 0.6.6-2mdv2011.0
+ Revision: 570936
- update the patch for python-couchdb 0.7 from a dedicated launchpad branch

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 0.6.6-1mdv2011.0
+ Revision: 561980
- New version 0.6.6

* Fri May 07 2010 Frederik Himpe <fhimpe@mandriva.org> 0.6.4-2mdv2010.1
+ Revision: 543395
- Fix compatibility with python-couchdb 9.7
  (https://bugs.launchpad.net/desktopcouch/+bug/566073)

* Fri Apr 16 2010 Frederik Himpe <fhimpe@mandriva.org> 0.6.4-1mdv2010.1
+ Revision: 535649
- update to new version 0.6.4

* Sat Mar 27 2010 Michael Scherer <misc@mandriva.org> 0.6.3-1mdv2010.1
+ Revision: 528255
- add requires on twisted-core
- split tools ( as they requires gtk2 )
- update to 0.6.3
- add url for source

* Sat Feb 13 2010 Frederik Himpe <fhimpe@mandriva.org> 0.6.1-3mdv2010.1
+ Revision: 505401
- Requires: python-oauth

* Sat Feb 13 2010 Frederik Himpe <fhimpe@mandriva.org> 0.6.1-2mdv2010.1
+ Revision: 505187
- Requires python-couchdb

* Thu Feb 11 2010 Michael Scherer <misc@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 504028
- use the new couchdb-bin package
- import desktopcouch

