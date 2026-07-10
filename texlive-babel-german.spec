%global tl_name babel-german
%global tl_revision 78737

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.3
Release:	%{tl_revision}.1
Summary:	Babel support for documents written in German
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/german
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-german.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-german.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-german.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle is an extension to the babel package for multilingual
typesetting. It provides all the necessary macros, definitions and
settings to typeset German documents. The bundle includes support for
the traditional and reformed German orthography as well as for the
Austrian and Swiss varieties of German.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-german
%dir %{_datadir}/texmf-dist/source/generic/babel-german
%dir %{_datadir}/texmf-dist/tex/generic/babel-german
%doc %{_datadir}/texmf-dist/doc/generic/babel-german/README
%doc %{_datadir}/texmf-dist/doc/generic/babel-german/babel-german.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-german/babel-german.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-german/babel-german.ins
%{_datadir}/texmf-dist/tex/generic/babel-german/austrian.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/babel-german.def
%{_datadir}/texmf-dist/tex/generic/babel-german/german-at-1901.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/german-at.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/german-austria-1901.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/german-austria.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/german-ch-1901.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/german-ch.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/german-de-1901.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/german-de.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/german-germany-1901.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/german-germany.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/german-switzerland-1901.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/german-switzerland.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/german.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/germanb.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/naustrian.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/ngerman.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/ngermanb.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/nswissgerman.ldf
%{_datadir}/texmf-dist/tex/generic/babel-german/swissgerman.ldf
