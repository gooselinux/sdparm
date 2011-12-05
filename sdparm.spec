Summary:   List or change SCSI/SATA disk parameters
Name:      sdparm
Version:   1.04
Release:   1.1%{?dist}
License:   BSD
Group:     Applications/System
URL:       http://sg.danny.cz/sg/sdparm.html
Source0:   http://sg.danny.cz/sg/p/sdparm-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description 
SCSI disk parameters are held in mode pages. This utility lists or
changes those parameters. Other SCSI devices (or devices that use the
SCSI command set e.g. some SATA devices) such as CD/DVD and tape
drives may also find parts of sdparm useful. Requires the linux kernel
2.4 series or later. In the 2.6 series any device node the understands
a SCSI command set may be used (e.g. /dev/sda). In the 2.4 series SCSI
device node may be used.

Fetches Vital Product Data pages. Can send commands to start or stop
the media and load or unload removable media.

Warning: It is possible (but unlikely) to change SCSI disk settings
such that the disk stops operating or is slowed down. Use with care.

%prep
%setup -q

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__make} install DESTDIR=%{buildroot} INSTALL="%{__install} -p"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc ChangeLog README CREDITS AUTHORS COPYING notes.txt
%{_bindir}/%{name}
%{_mandir}/man8/%{name}*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.04-1.1
- Rebuilt for RHEL 6

* Wed Oct 14 2009 Dan Horák <dan[at]danny.cz> - 1.04-1
- 1.04

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  8 2009 Terje Rosten <terje.rosten@ntnu.no> - 1.03-2
- Website has moved

* Tue Aug 12 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.03-1
- 1.03

* Sat Feb  9 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.02-2
- Rebuild

* Mon Nov  5 2007 Terje Rosten <terje.rosten@ntnu.no> - 1.02-1
- 1.02

* Tue Aug 28 2007 Terje Rosten <terje.rosten@ntnu.no> - 1.01-3
- Rebuild

* Mon May 21 2007 Terje Rosten <terje.rosten@ntnu.no> - 1.01-2
- Tag problem

* Mon May 21 2007 Terje Rosten <terje.rosten@ntnu.no> - 1.01-1
- New upstream release: 1.01

* Mon Nov 20 2006 Terje Rosten <terje.rosten@ntnu.no> - 1.00-4
- Fix changelog
- Don't install INSTALL

* Mon Nov 20 2006 Terje Rosten <terje.rosten@ntnu.no> - 1.00-3
- Maybe we should build in %%build :-)
- Remove check in %%clean/%%install

* Mon Nov 20 2006 Terje Rosten <terje.rosten@ntnu.no> - 1.00-2
- fix license, buildroot and group
- remove hardcoded packager tag
- use %%configure macro
- dist tag
- make install on single line
- fix files section
- remove strange use of macros (name, version and release)
- untabify

* Mon Oct 16 2006 Douglas Gilbert <dgilbert at interlog dot com> - 1.00
- update Background control mode subpage, vendor specific mode pages
- sdparm-1.00

* Sat Jul 08 2006 Douglas Gilbert <dgilbert at interlog dot com> - 0.99
- add old power condition page for disks
- sdparm-0.99

* Thu May 18 2006 Douglas Gilbert <dgilbert at interlog dot com> - 0.98
- add medium configuration mode page
- sdparm-0.98

* Wed Jan 25 2006 Douglas Gilbert <dgilbert at interlog dot com> - 0.97 
- add SAT pATA control and medium partition mode (sub)pages
- sdparm-0.97

* Fri Nov 18 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.96
- add capacity, ready and sync commands
- sdparm-0.96

* Tue Sep 20 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.95
- add debian build directory, decode more VPD pages
- sdparm-0.95

* Thu Jul 28 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.94
- add '--command=<cmd>' option
- sdparm-0.94

* Thu Jun 02 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.93
- add '--transport=' and '--dbd' options
- sdparm-0.93

* Fri May 20 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.92
- add some tape, cd/dvd, disk, ses and rbc mode pages
- sdparm-0.92

* Fri May 06 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.91
- if lk 2.4 detected, map non-sg SCSI device node to sg equivalent
- sdparm-0.91

* Mon Apr 18 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.90
- initial version
- sdparm-0.90
