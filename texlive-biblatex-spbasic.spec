%global tl_name biblatex-spbasic
%global tl_revision 61439

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.04
Release:	%{tl_revision}.1
Summary:	A BibLaTeX style emulating Springers old spbasic.bst
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-spbasic
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-spbasic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-spbasic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a bibliography and citation style for
BibLaTeX/biber for typesetting articles for Springer's journals. It is
the same as the old BibTeX style spbasic.bst.

