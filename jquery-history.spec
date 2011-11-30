%define		plugin	history
Summary:	jQuery history plugin
Name:		jquery-%{plugin}
Version:	0.1
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://github.com/tkyk/jquery-history-plugin/raw/master/jquery.history.js
# Source0-md5:	9c162509c5b432ebb2d9f7ea0852a26d
URL:		http://tkyk.github.com/jquery-history-plugin/
BuildRequires:	closure-compiler
BuildRequires:	js
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
jQuery history plugin helps you to support back/forward buttons and
bookmarks in your javascript applications. You can store the
application state into URL hash and restore the state from it.

%prep
%setup -qcT
cp -p %{SOURCE0} .

%build
install -d build

# compress .js
js=jquery.history.js
out=build/$js
%if 0%{!?debug:1}
closure-compiler --js $js --charset UTF-8 --js_output_file $out
js -C -f $out
%else
cp -p $js $out
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p build/jquery.history.js $RPM_BUILD_ROOT%{_appdir}/history.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
