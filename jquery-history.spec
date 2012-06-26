%define		plugin	history
Summary:	jQuery history plugin
Name:		jquery-%{plugin}
Version:	1.7.1
Release:	1
License:	New BSD License
Group:		Applications/WWW
Source0:	https://github.com/balupton/history.js/tarball/master/%{plugin}-%{version}.tgz
# Source0-md5:	8aee8aed522b72695cb80edb219e4576
URL:		https://github.com/balupton/History.js/
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
History.js gracefully supports the HTML5 History/State APIs
(pushState, replaceState, onPopState) in all browsers. Including
continued support for data, titles, replaceState. Supports jQuery,
MooTools and Prototype. For HTML5 browsers this means that you can
modify the URL directly, without needing to use hashes anymore. For
HTML4 browsers it will revert back to using the old onhashchange
functionality.

%prep
%setup -qc
mv *-history.js-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p scripts/compressed/history*.js $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc History.md README.md license.txt
%{_appdir}
