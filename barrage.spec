%define	name	barrage
%define	version	1.0.2
%define	release	%mkrel 7
%define	Summary	A rather violent action game

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://lgames.sourceforge.net/index.php?project=Barrage
Source0:	http://nchc.dl.sourceforge.net/sourceforge/lgames/%{name}-%{version}.tar.bz2
Patch0:		barrage-1.0.2-desktop-entry-fix.patch
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
License:	GPL
Group:		Games/Arcade
Summary:	%{Summary}
BuildRequires:	SDL_mixer-devel
Buildrequires:	SDL-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Barrage is a rather violent action game with the objective to kill
and destroy as many targets as possible within 3 minutes. The player
controls a gun that may either fire small or large grenades at
soldiers, jeeps and tanks. It is a very simple gameplay though it is
not that easy to get high scores.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x	--bindir=%{_gamesbindir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%defattr(755,root,root,755)
%{_gamesbindir}/*
