# NOTE: don't use 2.5.34, it's too broken? is 2.5.35 ok? how to test?
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
Version:	2.5.35
Release:	0.1
License:	BSD-like
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/flex/%{name}-%{version}.tar.bz2
# Source0-md5:	10714e50cea54dc7a227e3eddcd44d57
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	fd79ee2834b290e74c626f0bbfc8942f
Patch0:		%{name}-info.patch
Patch2:		%{name}-locale.patch
# patch #869230 (second version of bug #720983 fix)
#Patch3:	%{name}-m4-quotes.diff
URL:		http://flex.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	bison
# m4-quotes* patches require rebuilding *.c from scan.l
BuildRequires:	flex
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	help2man
BuildRequires:	texinfo
BuildRequires:	util-linux
Requires:	m4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_amd64		-fPIC
%define		specflags_ia32e		-fPIC
%define		specflags_x86_64	-fPIC

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
%patch2 -p1
#%patch3 -p1

# force regeneration (just in case make didn't want to)
rm -f skel.c

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

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
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_mandir}/README.flex-non-english-man-pages

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

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

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
