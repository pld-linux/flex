Summary:	GNU fast lexical analyzer generator
Summary(de):	GNU - schneller lexikalischer Analysegenerator 
Summary(fr):	Générateur rapide d'analyseur lexical de GNU
Summary(pl):	GNU szybki generator analizatora sk³adni (flex)
Summary(tr):	GNU sözdizim çözümleyici
Name:		flex
Version:	2.5.4a
Release:	8
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		flex-info.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is the GNU fast lexical analyzer generator. It generates lexical
tokenizing code based on a lexical (regular expression based) description
of the input. It is designed to work with both yacc and bison, and is
used by many programs as part of their build process.

%description -l de
GNU, der schnelle lexikalische Analysengenerator. Er erzeugt lexikalischen 
Token-Code, basierend auf einer lexikalischen Beschreibung (reguläre 
Ausdrucksbasis) der Eingabe. Ausgelegt zum Arbeiten mit yacc und bison, 
wird er von vielen Programmen als Teil des Build-Vorgangs verwendet. 

%description -l fr
Générateur rapide d'analyseur lexical de GNU. Il génère du code lexical
sous forme de tokens basé sur une description lexicale (basé sur les
expressions rationnelles) de son entrée. Il est conçu pour fonctionner
avec yacc et bison, et est utilisé par de nombreux programmes comme
faisant partie de leur phase de construction.

%description -l pl
GNU flex s³u¿y do tworzenia programu analizy leksykalnej na podstawie
wyra¿eñ regularnych i dyrektyw C zawartych w jednym lub wiêcej plikach
wej¶ciowych.  Przeznaczony do wspó³pracy z parserami yacc i bison, jest
u¿ywany przez wiele programów w procesie kompilacji.

%description -l tr
Bu paket, giriþ olarak okuduðu bilgiyi kendisine düzgün deyimler olarak
belirtilen kurallar çerçevesinde birimlere böler. yacc ve bison paketleri
ile birlikte çalýþacak þekilde tasarlanmýþtýr. Pek çok programýn derlenme
aþamasýnda kullanýlýr.

%prep
%setup -q -n %{name}-2.5.4
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr
make

makeinfo MISC/texinfo/flex.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,info,include,man/man1}

install flex.info* $RPM_BUILD_ROOT%{_infodir}

make prefix=$RPM_BUILD_ROOT/usr install
cd $RPM_BUILD_ROOT%{_bindir}
ln -sf flex lex

gzip -9nf $RPM_BUILD_ROOT/usr/{info/*,man/man1/*}

%post
/sbin/install-info %{_infodir}/flex.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/flex.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/flex*
%{_libdir}/*.a
%{_includedir}/*.h

%changelog
* Tue Dec 29 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.5.4a-7]
- added flex info pages and %post, %postun and
  {un}registering info pages.

* Mon Dec 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.5.4a-6]
- added gzipping man pages,
- LDFLAGS="-s" moved to make parameters.

* Fri Sep 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.5.4a-5]
- removed COPYING from %doc (copyright statment is in Copyright field),

* Sun Jun 14 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.5.4a-5]
- added buildroot support,
- build from non root's account,
- minor modifications of spec file,
- added pl translation (made by Piotr Dembiñski <hektor@kki.net.pl>).

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 2.5.4 to 2.5.4a

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 20 1997 Michael Fulbright <msf@redhat.com>
 Updated to v. 2.5.4
