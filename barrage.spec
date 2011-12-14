Name:		barrage
Version:	1.0.4
Release:	%mkrel 1
License:	GPLv2
Group:		Games/Arcade
Summary:	A rather violent action game
URL:		http://lgames.sourceforge.net/index.php?project=Barrage
Source0:	http://nchc.dl.sourceforge.net/sourceforge/lgames/%{name}-%{version}.tar.gz
Patch0:		barrage-1.0.4-desktop-entry-fix.patch
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
%patch0 -p1

%build
%configure2_5x	--bindir=%{_gamesbindir}
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_gamesdatadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%attr(755,root,root) %{_gamesbindir}/*
