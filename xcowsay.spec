%define name	xcowsay
%define version	1.3
%define release	2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Displays a cute cow and message on your desktop
Group:		Toys
License:	GPL
URL:		http://www.doof.me.uk/xcowsay/
Source:     http://www.nickg.me.uk/files/%{name}-%{version}.tar.gz
Patch:      xcowsay-1.2-fix-xcowthink-args-parsing.patch
BuildRequires:  gtk+2-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
xcowsay displays a cute cow and message on your desktop.

xcowsay includes all these amazing features:
- Fully configurable!
- Calculates display time from amount of text
- Daemon mode! Send your cow messages over DBus!
- Three different sized cows provided
- fortune(6) wrapper program: xcowfortune — cow will deliver pearls of wisdom!
- Replace the naffness that is xmessage(1)
- Should work with any window manager
- Supports UTF-8 characters properly

%prep
%setup -q
%patch -p 1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/%{name}



%changelog
* Sat Nov 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-1mdv2011.0
+ Revision: 597258
- update to new version 1.3

* Sun Mar 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-2mdv2010.1
+ Revision: 528615
- fix xcowthink argument parsing (#58452)

* Tue Jan 05 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-1mdv2010.1
+ Revision: 486468
- new version

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.1-1mdv2010.1
+ Revision: 468635
- update to new version 1.1.1

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.1-2mdv2010.0
+ Revision: 435070
- rebuild

* Mon Sep 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2009.0
+ Revision: 278591
- update to new version 1.1

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 269767
- rebuild early 2009.0 package (before pixel changes)
- description is not history

* Tue May 27 2008 Thierry Vignaud <tv@mandriva.org> 1.0-2mdv2009.0
+ Revision: 211572
- fix description-line-too-long

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2009.0
+ Revision: 210902
- import xcowsay


* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2009.0
- first mdv package 
