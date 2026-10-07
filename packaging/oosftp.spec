Name:           oosftp
Version:        0.1.0
Release:        1%{?dist}
Summary:        Interactive and scripted SFTP client with capability-isolated local sandbox.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosftp
Source0:        oosftp-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosftp is a sovereign, capability-bounded SFTP CLIENT written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosftp
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosftp-uninstall

%files
/usr/bin/oosftp
/usr/bin/oosftp-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
