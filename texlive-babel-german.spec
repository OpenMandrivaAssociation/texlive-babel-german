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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle is an extension to the babel package for multilingual
typesetting. It provides all the necessary macros, definitions and
settings to typeset German documents. The bundle includes support for
the traditional and reformed German orthography as well as for the
Austrian and Swiss varieties of German.

