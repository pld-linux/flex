Summary:	GNU fast lexical analyzer generator
Summary(de):	GNU - schneller lexikalischer Analysegenerator
Summary(es):	Generador r�pido de analizadores l�xicos de la GNU
Summary(fr):	G�n�rateur rapide d'analyseur lexical de GNU
Summary(pl):	Szybki generator analizatora sk�adni GNU (flex)
Summary(pt_BR):	Gerador r�pido de analisadores l�xicos da GNU
Summary(ru):	������� ��������� ����������� ������������ GNU
Summary(tr):	GNU s�zdizim ��z�mleyici
Summary(uk):	������� ��������� ��������� ���̦����Ҧ� GNU
Name:		flex
Version:	2.5.31
Release:	5
License:	BSD-like
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/lex/%{name}-%{version}.tar.bz2
# Source0-md5:	363dcc4afc917dc51306eb9d3de0152f
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	fd79ee2834b290e74c626f0bbfc8942f
Source2:	%{name}-pl.po
Patch0:		%{name}-info.patch
Patch1:		%{name}-glibc22.patch
Patch2:		%{name}-locale.patch
Patch3:		%{name}-yymore-fix.patch
Patch4:		%{name}-yytext_ptr-undefined.patch
URL:		http://lex.sf.net/
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	help2man
BuildRequires:	texinfo
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

%description -l es
Este es el creador GNU de an�lisis l�xica r�pida. Crea c�digos l�xicos
tokenizados basados en una descripci�n l�xica (basado en expresiones
regulares) de la entrada. Est� designado a trabajar tanto con yacc
como con bison, y se utiliza en varios programas como parte del su
proceso de programaci�n.

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

%description -l pt_BR
Este � o gerador GNU de an�lise l�xica r�pida. Ele gera c�digos
l�xicos tokenizados baseados em uma descri��o l�xica (baseado em
express�es regulares) da entrada. Ele � designado para trabalhar tanto
com yacc como com bison, e � utilizado em v�rios programas como parte
do seu processo de programa��o.

%description -l ru
��������� flex ���������� ��������. �������� - ��� ���������,
��������� ������������ ����������� ������� � ������. flex ��������� ��
����� ���� ���������� ��������� � C ��� � ���������� �������� ����� ��
����� C. �������� ���� ������������� � ����������� � ����������� ���
�������� ������������ �����, ������� ����� ������������� ���� �������
����� ������ � ������ ���������� ���������. ��� ���������� �����
����������� �������� C ���. flex ��� ���������� ��� ������ ��� �
�������� Yacc, ��� � Bison, � ������������ ������� ����������� ���
����� �������� �� ���������� �� �������� �������.

��� ������� ���������� flex, ���� �� ����������� ������������ ����
������� ��� ���������� ��������.

%description -l tr
Bu paket, giri� olarak okudu�u bilgiyi kendisine d�zg�n deyimler
olarak belirtilen kurallar �er�evesinde birimlere b�ler. yacc ve bison
paketleri ile birlikte �al��acak �ekilde tasarlanm��t�r. Pek �ok
program�n derlenme a�amas�nda kullan�l�r.

%description -l uk
�������� flex �����դ �������. ������� - �� ��������, �˦ ������
���Ц������� ������Φ ������� � ����Ԧ. flex ������� �� ���Ħ ����
���������� ����ڦ� �� C ��� �� �����դ ��Ȧ�Φ ����� �� ��צ C.
��Ȧ���� ���� ���Ц������� �� ��'��դ���� � ¦�̦������ ��� ���������
������������ �����, �� ������������ �צ� �Ȧ���� ��Ԧ� ����� � ������
���������� ����ڦ�. ��� ���������Φ ���������������� ������� C ���.
flex ��� ����������� ��� ������ �� � �������� Yacc, ��� � Bison, ��
����������դ���� �������� ���������� � �����Ӧ �� �������� � ��Ȧ����
����Ԧ�.

��� �̦� ���������� flex, ���� �� ���������� ��������������� ����
������� ��� �������� �������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

cp -f %{SOURCE2} po/pl.po
echo 'pl' >> po/LINGUAS

# force regeneration (just in case make didn't want to)
rm -f skel.c

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf flex $RPM_BUILD_ROOT%{_bindir}/lex

echo .so flex.1 > $RPM_BUILD_ROOT%{_mandir}/man1/flex++.1
echo .so flex.1 > $RPM_BUILD_ROOT%{_mandir}/man1/lex.1
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/flex*
%{_libdir}/*.a
%{_includedir}/*.h
