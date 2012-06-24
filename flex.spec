Summary:     GNU fast lexical analyzer generator
Summary(de): GNU - schneller lexikalischer Analysegenerator 
Summary(fr): G�n�rateur rapide d'analyseur lexical de GNU
Summary(pl): GNU szybki generator analizatora sk�adni (flex)
Summary(tr): GNU s�zdizim ��z�mleyici
Name:        flex
Version:     2.5.4
Release:     5
Copyright:   GPL
Group:       Development/Tools
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}a.tar.gz
Buildroot:   /tmp/%{name}-%{version}-root

%description
This is the GNU fast lexical analyzer generator. It generates lexical
tokenizing code based on a lexical (regular expression based) description
of the input. It is designed to work with both yacc and bison, and is
used by many programs as part of their build process.

%description -l de
GNU, der schnelle lexikalische Analysengenerator. Er erzeugt lexikalischen 
Token-Code, basierend auf einer lexikalischen Beschreibung (regul�re 
Ausdrucksbasis) der Eingabe. Ausgelegt zum Arbeiten mit yacc und bison, 
wird er von vielen Programmen als Teil des Build-Vorgangs verwendet. 

%description -l fr
G�n�rateur rapide d'analyseur lexical de GNU. Il g�n�re du code lexical
sous forme de tokens bas� sur une description lexicale (bas� sur les
expressions rationnelles) de son entr�e. Il est con�u pour fonctionner
avec yacc et bison, et est utilis� par de nombreux programmes comme
faisant partie de leur phase de construction.

%description -l pl
GNU flex s�u�y do tworzenia programu analizy leksykalnej na podstawie
wyra�e� regularnych i dyrektyw C zawartych w jednym lub wi�cej plikach
wej�ciowych.  Przeznaczony do wsp�pracy z parserami yacc i bison, jest
u�ywany przez wiele program�w w procesie kompilacji.

%description -l tr
Bu paket, giri� olarak okudu�u bilgiyi kendisine d�zg�n deyimler olarak
belirtilen kurallar �er�evesinde birimlere b�ler. yacc ve bison paketleri
ile birlikte �al��acak �ekilde tasarlanm��t�r. Pek �ok program�n derlenme
a�amas�nda kullan�l�r.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" ./configure --prefix=/usr
make

%install
install -d $RPM_BUILD_ROOT/usr/{bin,include,man/man1}}

make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/* || :
cd $RPM_BUILD_ROOT/usr/bin
ln -sf flex lex

%files
%defattr(644, root, root, 755)
%doc NEWS README
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
/usr/lib/*.a
/usr/include/*.h

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Sep 18 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.5.4-5]
- removed COPYING from %doc (copyright statment is in Copyright field),

* Sun Jun 14 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.5.4-5]
- added buildroot support,
- build from non root's account,
- minor modifications of spec file,
- added pl translation (made by Piotr Dembi�ski <hektor@kki.net.pl>).

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr


* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 2.5.4 to 2.5.4a

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 20 1997 Michael Fulbright <msf@redhat.com>
 Updated to v. 2.5.4
