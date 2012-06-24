Summary:	GNU fast lexical analyzer generator
Summary(de):	GNU - schneller lexikalischer Analysegenerator 
Summary(fr):	G�n�rateur rapide d'analyseur lexical de GNU
Summary(pl):	GNU szybki generator analizatora sk�adni (flex)
Summary(tr):	GNU s�zdizim ��z�mleyici
Name:		flex
Version:	2.5.4a
Release:	9
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narz�dzia
Source:		ftp://prep.ai.mit.edu/pub/gnu/flex/%{name}-%{version}.tar.gz
Patch0:		flex-info.patch
Buildroot:	/tmp/%{name}-%{version}-root

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
%setup -q -n %{name}-2.5.4
%patch0 -p1

%build
autoconf
%configure
make

makeinfo MISC/texinfo/flex.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_includedir},%{_mandir}/man1}

install flex.info* $RPM_BUILD_ROOT%{_infodir}

make install prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT/%{_bindir} \
	mandir=$RPM_BUILD_ROOT/%{_mandir}/man1 \
	libdir=$RPM_BUILD_ROOT/%{_libdir} \
	includedir=$RPM_BUILD_ROOT/%{_includedir} \
	infodir=$RPM_BUILD_ROOT/%{_infodir}

ln -sf flex $RPM_BUILD_ROOT%{_bindir}/lex

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*,%{_mandir}/man1/*}

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
* Mon Jun 21 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.5.4a-9]
- based on RH spec,
- spec rewrited by PLD team,
- pl translation by Wojtek �lusarczyk <wojtek@shadow.eu.org>.
