# NOTE: 2.5.35+ can't deal with "[[" "]]" strings in sources, needs workarounds like space separation
#	(or non-trivial update of m4-quotes patch)
# NOTE on shared libfl:
#	It exports two functions, yywrap() and main();
#	- because of the latter, unnecessary linking with shared -lfl would harm,
#	  so it would require large cleanup of other projects;
#	- when some code wants yywrap(), but no main(), using shared libfl is NOT POSSIBLE.
#	Thus, shared libfl would be of little use.
Summary:	GNU fast lexical analyzer generator
Summary(de.UTF-8):	GNU - schneller lexikalischer Analysegenerator
Summary(es.UTF-8):	Generador rápido de analizadores léxicos de la GNU
Summary(fr.UTF-8):	Générateur rapide d'analyseur lexical de GNU
Summary(pl.UTF-8):	Szybki generator analizatora składni GNU (flex)
Summary(pt_BR.UTF-8):	Gerador rápido de analisadores léxicos da GNU
Summary(ru.UTF-8):	Быстрый генератор лексических анализаторов GNU
Summary(tr.UTF-8):	GNU sözdizim çözümleyici
Summary(uk.UTF-8):	Швидкий генератор лексичних аналізаторів GNU
Name:		flex
Version:	2.5.39
Release:	1
License:	BSD-like
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/flex/%{name}-%{version}.tar.xz
# Source0-md5:	477679c37ff8b28248a9b05f1da29a82
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	fd79ee2834b290e74c626f0bbfc8942f
Patch0:		%{name}-info.patch
Patch1:		%{name}-pic.patch
# patch #869230 (second version of bug #720983 fix - from flex BTS)
# outdated as for 2.5.34+, but contains testcase
Patch2:		%{name}-m4-quotes.diff
URL:		http://flex.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.10
BuildRequires:	bison
# to rebuild scan.c from scan.l (m4-quotes patch)
#BuildRequires:	flex
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	help2man
BuildRequires:	libtool >= 2:2
# to rebuild skel.c from patched flex.skl
BuildRequires:	m4
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	texinfo-texi2dvi
BuildRequires:	texlive-fonts-cmsuper
BuildRequires:	texlive-pdftex
BuildRequires:	util-linux
BuildRequires:	xz
Requires:	m4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GNU fast lexical analyzer generator. It generates lexical
tokenizing code based on a lexical (regular expression based)
description of the input. It is designed to work with both yacc and
bison, and is used by many programs as part of their build process.

%description -l de.UTF-8
GNU, der schnelle lexikalische Analysengenerator. Er erzeugt
lexikalischen Token-Code, basierend auf einer lexikalischen
Beschreibung (reguläre Ausdrucksbasis) der Eingabe. Ausgelegt zum
Arbeiten mit yacc und bison, wird er von vielen Programmen als Teil
des Build-Vorgangs verwendet.

%description -l es.UTF-8
Este es el creador GNU de análisis léxica rápida. Crea códigos léxicos
tokenizados basados en una descripción léxica (basado en expresiones
regulares) de la entrada. Está designado a trabajar tanto con yacc
como con bison, y se utiliza en varios programas como parte del su
proceso de programación.

%description -l fr.UTF-8
Générateur rapide d'analyseur lexical de GNU. Il génère du code
lexical sous forme de tokens basé sur une description lexicale (basé
sur les expressions rationnelles) de son entrée. Il est conçu pour
fonctionner avec yacc et bison, et est utilisé par de nombreux
programmes comme faisant partie de leur phase de construction.

%description -l pl.UTF-8
GNU flex służy do tworzenia programu analizy leksykalnej na podstawie
wyrażeń regularnych i dyrektyw C zawartych w jednym lub więcej plikach
wejściowych. Przeznaczony do współpracy z parserami yacc i bison, jest
używany przez wiele programów w procesie kompilacji.

%description -l pt_BR.UTF-8
Este é o gerador GNU de análise léxica rápida. Ele gera códigos
léxicos tokenizados baseados em uma descrição léxica (baseado em
expressões regulares) da entrada. Ele é designado para trabalhar tanto
com yacc como com bison, e é utilizado em vários programas como parte
do seu processo de programação.

%description -l ru.UTF-8
Программа flex генерирует сканнеры. Сканнеры - это программы,
способные распознавать лексические шаблоны в тексте. flex принимает на
входе пару регулярных выражений и C код и генерирует исходные файлы на
языке C. Исходный файл компилируется и связывается с библиотекой для
создания исполняемого файла, который будет просматривать свой входной
поток данных в поиске регулярных выражений. При нахождении будет
исполняться заданный C код. flex был разработан для работы как с
системой Yacc, так и Bison, и используется многими программами как
часть процесса их построения из исходных текстов.

Вам следует установить flex, если вы собираетесь использовать свою
систему для разработки программ.

%description -l tr.UTF-8
Bu paket, giriş olarak okuduğu bilgiyi kendisine düzgün deyimler
olarak belirtilen kurallar çerçevesinde birimlere böler. yacc ve bison
paketleri ile birlikte çalışacak şekilde tasarlanmıştır. Pek çok
programın derlenme aşamasında kullanılır.

%description -l uk.UTF-8
Програма flex генерує сканери. Сканери - це програми, які можуть
розпізнавати лексичні шаблони в тексті. flex приймає на вході пару
регулярних виразів та C код та генерує вихідні файли на мові C.
Вихідний файл компілюється та зв'язується з бібліотекою для створення
виконуваного файлу, що проглядатиме свій вхідний потік даних в пошуку
регулярних виразів. При знаходженні виконуватиметься заданий C код.
flex був розроблений для роботи як з системою Yacc, так і Bison, та
використовується багатьма програмами в процесі їх побудови з вихідних
текстів.

Вам слід встановити flex, якщо ви збираєтесь використовувати свою
систему для розробки програм.

%package examples
Summary:	Flex examples
Summary(pl.UTF-8):	Przykłady dla fleksa
Group:		Development/Tools

%description examples
Flex examples.

%description examples -l pl.UTF-8
Przykłady dla fleksa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1

# force regeneration (just in case make didn't want to)
%{__rm} skel.c

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf flex $RPM_BUILD_ROOT%{_bindir}/lex
ln -sf flex $RPM_BUILD_ROOT%{_bindir}/flex++

echo .so flex.1 > $RPM_BUILD_ROOT%{_mandir}/man1/flex++.1
echo .so flex.1 > $RPM_BUILD_ROOT%{_mandir}/man1/lex.1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.flex-non-english-man-pages

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO doc/flex.pdf
%attr(755,root,root) %{_bindir}/flex
%attr(755,root,root) %{_bindir}/flex++
%attr(755,root,root) %{_bindir}/lex
%{_mandir}/man1/flex.1*
%{_mandir}/man1/flex++.1*
%{_mandir}/man1/lex.1*
%lang(es) %{_mandir}/es/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/flex.info*
%{_libdir}/libfl.a
%{_libdir}/libfl_pic.a
%{_includedir}/FlexLexer.h

%if 0
%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfl.so.2
%attr(755,root,root) %{_libdir}/libfl_pic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfl_pic.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfl.so
%attr(755,root,root) %{_libdir}/libfl_pic.so
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
