Summary:	GNU fast lexical analyzer generator
Summary(de):	GNU - schneller lexikalischer Analysegenerator
Summary(es):	Generador rАpido de analizadores lИxicos de la GNU
Summary(fr):	GИnИrateur rapide d'analyseur lexical de GNU
Summary(pl):	Szybki generator analizatora skЁadni GNU (flex)
Summary(pt_BR):	Gerador rАpido de analisadores lИxicos da GNU
Summary(ru):	Быстрый генератор лексических анализаторов GNU
Summary(tr):	GNU sЖzdizim ГЖzЭmleyici
Summary(uk):	Швидкий генератор лексичних анал╕затор╕в GNU
Name:		flex
Version:	2.5.4a
Release:	27
License:	BSD-like
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/non-gnu/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	bd8753d0b22e1f4ec87a553a73021adf
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	fd79ee2834b290e74c626f0bbfc8942f
Patch0:		%{name}-info.patch
Patch1:		%{name}-skel.patch
Patch2:		%{name}-glibc22.patch
Patch3:		%{name}-%{version}_bufer_overflow.patch
Patch4:		%{name}-gcc3.patch
Patch5:		%{name}-gcc31.patch
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
Beschreibung (regulДre Ausdrucksbasis) der Eingabe. Ausgelegt zum
Arbeiten mit yacc und bison, wird er von vielen Programmen als Teil
des Build-Vorgangs verwendet.

%description -l es
Este es el creador GNU de anАlisis lИxica rАpida. Crea cСdigos lИxicos
tokenizados basados en una descripciСn lИxica (basado en expresiones
regulares) de la entrada. EstА designado a trabajar tanto con yacc
como con bison, y se utiliza en varios programas como parte del su
proceso de programaciСn.

%description -l fr
GИnИrateur rapide d'analyseur lexical de GNU. Il gИnХre du code
lexical sous forme de tokens basИ sur une description lexicale (basИ
sur les expressions rationnelles) de son entrИe. Il est conГu pour
fonctionner avec yacc et bison, et est utilisИ par de nombreux
programmes comme faisant partie de leur phase de construction.

%description -l pl
GNU flex sЁu©y do tworzenia programu analizy leksykalnej na podstawie
wyra©eЯ regularnych i dyrektyw C zawartych w jednym lub wiЙcej plikach
wej╤ciowych. Przeznaczony do wspСЁpracy z parserami yacc i bison, jest
u©ywany przez wiele programСw w procesie kompilacji.

%description -l pt_BR
Este И o gerador GNU de anАlise lИxica rАpida. Ele gera cСdigos
lИxicos tokenizados baseados em uma descriГЦo lИxica (baseado em
expressУes regulares) da entrada. Ele И designado para trabalhar tanto
com yacc como com bison, e И utilizado em vАrios programas como parte
do seu processo de programaГЦo.

%description -l ru
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

%description -l tr
Bu paket, giriЧ olarak okuduПu bilgiyi kendisine dЭzgЭn deyimler
olarak belirtilen kurallar ГerГevesinde birimlere bЖler. yacc ve bison
paketleri ile birlikte ГalЩЧacak Чekilde tasarlanmЩЧtЩr. Pek Гok
programЩn derlenme aЧamasЩnda kullanЩlЩr.

%description -l uk
Програма flex генеру╓ сканери. Сканери - це програми, як╕ можуть
розп╕знавати лексичн╕ шаблони в текст╕. flex прийма╓ на вход╕ пару
регулярних вираз╕в та C код та генеру╓ вих╕дн╕ файли на мов╕ C.
Вих╕дний файл комп╕лю╓ться та зв'язу╓ться з б╕бл╕отекою для створення
виконуваного файлу, що проглядатиме св╕й вх╕дний пот╕к даних в пошуку
регулярних вираз╕в. При знаходженн╕ виконуватиметься заданий C код.
flex був розроблений для роботи як з системою Yacc, так ╕ Bison, та
використову╓ться багатьма програмами в процес╕ ╖х побудови з вих╕дних
текст╕в.

Вам сл╕д встановити flex, якщо ви збира╓тесь використовувати свою
систему для розробки програм.

%prep
%setup -q -n %{name}-2.5.4
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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
%doc NEWS README COPYING
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/flex*
%{_libdir}/*.a
%{_includedir}/*.h
