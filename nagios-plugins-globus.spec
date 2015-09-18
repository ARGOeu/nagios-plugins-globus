%define dir %{_libdir}/nagios/plugins/globus

Summary: Nagios plugins for Globus Toolkit services
Name: nagios-plugins-globus
Version: 0.1.0
Release: 1%{?dist}
License: ASL 2.0
Group: Network/Monitoring
Source0: %{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: perl-GridMon >= 1.0.28
Requires: voms-clients
Requires: globus-proxy-utils
Requires: myproxy
Requires: globus-gram-client-tools
Requires: uberftp
Requires: globus-gass-copy-progs

%description

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}%{dir}
install --mode 755 ./CertLifetime-probe  ${RPM_BUILD_ROOT}%{dir}
install --mode 755 ./GRAM-probe  ${RPM_BUILD_ROOT}%{dir}
install --mode 755 ./GridFTP-probe  ${RPM_BUILD_ROOT}%{dir}
install --mode 755 ./GridProxy-probe  ${RPM_BUILD_ROOT}%{dir}
install --mode 755 ./MyProxy-probe  ${RPM_BUILD_ROOT}%{dir}
install --mode 755 ./refresh_proxy ${RPM_BUILD_ROOT}%{dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{dir}/CertLifetime-probe
%{dir}/GRAM-probe
%{dir}/GridFTP-probe
%{dir}/GridProxy-probe
%{dir}/MyProxy-probe
%{dir}/refresh_proxy

%changelog
* Fri Sep 18 2015 Emir Imamagic <eimamagi@srce.hr> - 0.1.0-1%{?dist}
- Initial version of Globus probes for Nagios