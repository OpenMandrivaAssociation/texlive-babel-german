Epoch:		1
Name:		texlive-babel-german
Version:	69506
Release:	1
Summary:	Babel support for documents written in German
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/german
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-german.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-german.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-german.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines LaTeX support, within the Babel package, of
German (including its Austrian dialect), in both 'old' and
'new' orthographies.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-german/austrian.ldf
%{_texmfdistdir}/tex/generic/babel-german/german.ldf
%{_texmfdistdir}/tex/generic/babel-german/germanb.ldf
%{_texmfdistdir}/tex/generic/babel-german/naustrian.ldf
%{_texmfdistdir}/tex/generic/babel-german/ngerman.ldf
%{_texmfdistdir}/tex/generic/babel-german/ngermanb.ldf
%{_texmfdistdir}/tex/generic/babel-german/nswissgerman.ldf
%{_texmfdistdir}/tex/generic/babel-german/swissgerman.ldf
%doc %{_texmfdistdir}/doc/generic/babel-german/README
%doc %{_texmfdistdir}/doc/generic/babel-german/germanb.pdf
%doc %{_texmfdistdir}/doc/generic/babel-german/ngermanb.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-german/german.ins
%doc %{_texmfdistdir}/source/generic/babel-german/germanb.dtx
%doc %{_texmfdistdir}/source/generic/babel-german/ngermanb.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
