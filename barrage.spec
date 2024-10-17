Name:		barrage
Version:	1.0.7
Release:	1
License:	GPLv2
Group:		Games/Arcade
Summary:	A rather violent action game
URL:		https://lgames.sourceforge.net/index.php?project=Barrage
Source0:	http://nchc.dl.sourceforge.net/sourceforge/lgames/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(SDL_mixer)
Buildrequires:	pkgconfig(sdl)

%description
Barrage is a rather violent action game with the objective to kill
and destroy as many targets as possible within 3 minutes. The player
controls a gun that may either fire small or large grenades at
soldiers, jeeps and tanks. It is a very simple gameplay though it is
not that easy to get high scores.

%prep
%setup -q
%autopatch -p1

%build
%configure --localstatedir=%{_localstatedir}/games \
                --bindir=%{_gamesbindir}
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mv %{buildroot}%{_datadir}/icons/barrage48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

sed -i 's/Icon=.*/Icon=barrage/' %buildroot/%{_datadir}/applications/%{name}.desktop


%files
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_gamesbindir}/*
%config(noreplace) %attr(664, games, games) %{_localstatedir}/games/%{name}.hscr

%changelog
* Wed Dec 14 2011 Andrey Bondrov <abondrov@mandriva.org> 1.0.4-1
+ Revision: 740890
- New version 1.0.4

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 1.0.2-8
+ Revision: 635003
- rebuild
- tighten BR

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-7mdv2011.0
+ Revision: 616709
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.0.2-6mdv2010.0
+ Revision: 424012
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-5mdv2009.0
+ Revision: 243163
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Oct 29 2007 Funda Wang <fwang@mandriva.org> 1.0.2-3mdv2008.1
+ Revision: 102920
- fix bug#27120, icon not shown in menu


* Thu Dec 14 2006 Per Ã˜yvind Karlsen <pkarlsen@mandriva.com> 1.0.2-2mdv2007.0
+ Revision: 96900
- fix buildrequires
- xdg menu
  %%mkrel
  cleanups
- Import barrage

* Wed Feb 16 2005 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.0.2-1mdk
- 1.0.2

* Sat May 22 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.1-2mdk
- change summary macro to avoid possible conflicts if we were to build debug package
- fix buildrequires
- don't bzip2 icons in src.rpm

