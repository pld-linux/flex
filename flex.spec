Summary:	GNU fast lexical analyzer generator
Summary(de):	GNU - schneller lexikalischer Analysegenerator
Summary(fr):	G�n�rateur rapide d'analyseur lexical de GNU
Summary(pl):	Szybki generator analizatora sk�adni GNU (flex)
Summary(tr):	GNU s�zdizim ��z�mleyici
Name:		flex
Version:	2.5.4a
Release:	17
License:	GPL
Group:		Development/Tools
Source0:	ftp://prep.ai.mit.edu/pub/non-gnu/flex/%{name}-%{version}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-skel.patch
Patch2:		%{name}-glibc22.patch
Patch3:		%{name}-%{version}_bufer_overflow.patch
BuildRequires:	autoconf
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GNU fast lexical analyzer generator. It generates lexical
tokenizing code based on a lexical (regular expression based)
description of the input. It is designed to work with both yacc and
bison, and is used by many programs as part of their build process.

%description -l de
GNU, der schnelle lexikalische Analysengenerator. Er erzeugt
lexikalischen Token-Code, basierend auf einer lexikalischen
Beschreibung (regul�re Ausdrucksbasis) der Eingabe. Ausgelegt zum
Arbeiten mit yacc und bison, wird er von vielen Programmen als Teil
des Build-Vorgangs verwendet.

%description -l fr
G�n�rateur rapide d'analyseur lexical de GNU. Il g�n�re du code
lexical sous forme de tokens bas� sur une description lexicale (bas�
sur les expressions rationnelles) de son entr�e. Il est con�u pour
fonctionner avec yacc et bison, et est utilis� par de nombreux
programmes comme faisant partie de leur phase de construction.

%description -l pl
GNU flex s�u�y do tworzenia programu analizy leksykalnej na podstawie
wyra�e� regularnych i dyrektyw C zawartych w jednym lub wi�cej plikach
wej�ciowych. Przeznaczony do wsp�pracy z parserami yacc i bison, jest
u�ywany przez wiele program�w w procesie kompilacji.

%description -l tr
Bu paket, giri� olarak okudu�u bilgiyi kendisine d�zg�n deyimler
olarak belirtilen kurallar �er�evesinde birimlere b�ler. yacc ve bison
paketleri ile birlikte �al��acak �ekilde tasarlanm��t�r. Pek �ok
program�n derlenme a�amas�nda kullan�l�r.

%prep
%setup -q -n %{name}-2.5.4
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__autoconf}
%configure
%{__make}

makeinfo MISC/texinfo/flex.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_includedir},%{_mandir}/man1}

install flex.info* $RPM_BUILD_ROOT%{_infodir}

%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT/%{_bindir} \
	mandir=$RPM_BUILD_ROOT/%{_mandir}/man1 \
	libdir=$RPM_BUILD_ROOT/%{_libdir} \
	includedir=$RPM_BUILD_ROOT/%{_includedir} \
	infodir=$RPM_BUILD_ROOT/%{_infodir}

ln -sf flex $RPM_BUILD_ROOT%{_bindir}/lex

gzip -9nf NEWS README

echo .so flex.1 > $RPM_BUILD_ROOT%{_mandir}/man1/flex++
echo .so flex.1 > $RPM_BUILD_ROOT%{_mandir}/man1/lex
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/flex*
%{_libdir}/*.a
%{_includedir}/*.h
