# TODO
# - build from source
# - finish installation http://docs.mattermost.com/install/prod-rhel-7.html

Summary:	Mattermost is an open source, self-hosted Slack-alternative
Name:		mattermost
Version:	2.2.0
Release:	0.1
License:	MIT
Group:		Applications/Networking
Source0:	https://releases.mattermost.com/%{version}/%{name}-team-%{version}-linux-amd64.tar.gz
URL:		http://www.mattermost.org/
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	/opt/mattermost

%description
As an alternative to proprietary SaaS messaging, Mattermost brings all
your team communication into one place, making it searchable and
accessible anywhere.

%prep
%setup -qc
mv mattermost/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a api bin config i18n logs web $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md MIT-COMPILED-LICENSE.md NOTICE.txt
%attr(755,root,root) %{_appdir}/bin/platform
%dir %{_appdir}
%dir %{_appdir}/web
%{_appdir}/web/static
%{_appdir}/web/templates
%dir %{_appdir}/api
%{_appdir}/api/templates
%dir %{_appdir}/bin
%{_appdir}/config
%dir %{_appdir}/i18n
%{_appdir}/i18n/en.json
%lang(es) %{_appdir}/i18n/es.json
%lang(fr) %{_appdir}/i18n/fr.json
%lang(pt) %{_appdir}/i18n/pt.json
