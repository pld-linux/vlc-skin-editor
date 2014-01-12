Summary:	VLC Skin Editor
Summary(pl.UTF-8):	Edytor skórek dla VLC
Name:		vlc-skin-editor
Version:	0.8.5
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://download.videolan.org/videolan/skin-editor/%{version}/VLCSkinEditor_unix.tar.gz
# Source0-md5:	62ea5993ddcd2b926b89fa3ea31b8d53
URL:		http://www.videolan.org/vlc/skinedhlp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VLC Skin Editor.

%description -l pl.UTF-8
Edytor skórek dla VLC.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

cp -pr VLCSkinEditor.jar skin.dtd lang $RPM_BUILD_ROOT%{_datadir}/%{name}
cat >$RPM_BUILD_ROOT%{_bindir}/VLCSkinEditor <<EOF
#!/bin/sh

# lang directory must be in $PWD
cd %{_datadir}/%{name}

java -jar VLCSkinEditor.jar
EOF
chmod 755 $RPM_BUILD_ROOT%{_bindir}/VLCSkinEditor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.TXT
%attr(755,root,root) %{_bindir}/VLCSkinEditor
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/VLCSkinEditor.jar
%{_datadir}/%{name}/skin.dtd
%dir %{_datadir}/%{name}/lang
%{_datadir}/%{name}/lang/languages.txt
%lang(ca) %{_datadir}/%{name}/lang/ca.txt
%lang(de) %{_datadir}/%{name}/lang/de.txt
%{_datadir}/%{name}/lang/en.txt
%lang(fr) %{_datadir}/%{name}/lang/fr.txt
%lang(ko) %{_datadir}/%{name}/lang/ko.txt
%lang(nl) %{_datadir}/%{name}/lang/nl.txt
%lang(pt_BR) %{_datadir}/%{name}/lang/pt-br.txt
%lang(ru) %{_datadir}/%{name}/lang/ru.txt
%lang(sk) %{_datadir}/%{name}/lang/sk.txt
%lang(sv) %{_datadir}/%{name}/lang/sv.txt