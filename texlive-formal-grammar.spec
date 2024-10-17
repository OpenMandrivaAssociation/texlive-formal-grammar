Name:		texlive-formal-grammar
Version:	61955
Release:	2
Summary:	Typeset formal grammars
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/formal-grammar
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formal-grammar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formal-grammar.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formal-grammar.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a new environment and associated commands
to typeset BNF grammars. It allows to easily write formal
grammars. Its original motivation was to typeset grammars for
beamer presentations, therefore, there are macros to emphasize
or downplay some parts of the grammar (which is the main
novelty compared to other BNF packages).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/formal-grammar
%{_texmfdistdir}/tex/latex/formal-grammar
%doc %{_texmfdistdir}/doc/latex/formal-grammar

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
