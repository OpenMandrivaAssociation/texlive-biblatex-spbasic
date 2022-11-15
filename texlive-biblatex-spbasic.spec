Name:		texlive-biblatex-spbasic
Version:	61439
Release:	1
Summary:	A BibLaTeX style emulating Springer's old spbasic.bst
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-spbasic
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-spbasic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-spbasic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a bibliography and citation style for
BibLaTeX/biber for typesetting articles for Springer's
journals. It is the same as the old BibTeX style spbasic.bst.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-spbasic
%doc %{_texmfdistdir}/doc/latex/biblatex-spbasic

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
