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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a bibliography and citation style for
BibLaTeX/biber for typesetting articles for Springer's journals. It is
the same as the old BibTeX style spbasic.bst.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-spbasic
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-spbasic
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-spbasic/Changes
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-spbasic/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-spbasic/biblatex-spbasic.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-spbasic/biblatex-spbasic.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-spbasic/biblatex-spbasic.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-spbasic/biblatex-spbasic.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-spbasic/biblatex-spbasic.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-spbasic/biblatex-spbasic.lbx
