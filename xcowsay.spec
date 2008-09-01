%define name	xcowsay
%define version	1.1
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Displays a cute cow and message on your desktop
Group:		Toys
License:	GPL
URL:		http://www.doof.me.uk/xcowsay/
Source:     http://www.nickg.me.uk/files/%{name}-%{version}.tar.gz
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

