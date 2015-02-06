Summary:	Drive and jump with some kind of car across the moon
Name:		moon-buggy
Version:	1.0.51
Release:	3
License:	GPLv2
Group:		Games/Arcade
URL:		http://seehuhn.de/pages/%{name}
Source0:	http://seehuhn.de/media/programs/%{name}-%{version}.tar.gz
Source1:	http://seehuhn.de/media/programs/%{name}-sound-%{version}.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}-sound.desktop
Patch0:		moon-buggy-1.0.51-pause.patch
Patch1:		moon-buggy-1.0.51-sound.patch
BuildRequires:	ncurses-devel
BuildRequires:	esound-devel
BuildRequires:	desktop-file-utils
BuildRequires:	autoconf
BuildRequires:	automake

%description
Moon-buggy is a simple character graphics game where you drive some kind
of car across the moon's surface. Unfortunately there are dangerous craters
there. Fortunately your car can jump over them!

The game has some resemblance of the classic arcade game moon-patrol which
was released in 1982. A clone of this game was relased for the Commodore
C64 in 1983. The present, ASCII art version of moon-buggy was written many
years later by Jochen Voss.

%prep
%setup -q -a 1
%patch0 -p1 -b .pause
%patch1 -p1 -b .sound
mv -f %{name}-%{version}/* .

%build
autoreconf -f
%configure2_5x --sharedstatedir=%{_localstatedir}/games
%make

%install
%makeinstall_std

# Create zero-sized highscore file
touch %{buildroot}%{_localstatedir}/games/%{name}/mbscore

# Install working *.desktop files and an icon
desktop-file-install --vendor "" --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
desktop-file-install --vendor "" --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
install -D -p -m 644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Some file cleanups
rm -f %{buildroot}%{_infodir}/dir

# Convert everything to UTF-8
iconv -f iso-8859-1 -t utf-8 -o ChangeLog.utf8 ChangeLog
sed -i 's|\r$||g' ChangeLog.utf8
touch -c -r ChangeLog ChangeLog.utf8
mv -f ChangeLog.utf8 ChangeLog

iconv -f iso-8859-1 -t utf-8 -o TODO.utf8 TODO
sed -i 's|\r$||g' TODO.utf8
touch -c -r TODO TODO.utf8
mv -f TODO.utf8 TODO

%files
%doc ANNOUNCE AUTHORS ChangeLog COPYING README THANKS README.sound
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-sound.desktop
%attr(2755,root,games) %{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_infodir}/%{name}.info.*
%dir %attr(0775,root,games) %{_localstatedir}/games/%{name}
%config(noreplace) %attr(664,root,games) %{_localstatedir}/games/%{name}/mbscore



%changelog
* Fri Jun 01 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0.51-2
+ Revision: 801732
- Spec cleanup

* Tue Dec 06 2011 Andrey Bondrov <abondrov@mandriva.org> 1.0.51-1
+ Revision: 738362
- imported package moon-buggy

