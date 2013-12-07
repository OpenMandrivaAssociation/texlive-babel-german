# revision 30271
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-babel-german
Version:	20131013
Release:	4
Summary:	TeXLive babel-german package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-german.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-german.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-german.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-german package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-german/germanb.ldf
%{_texmfdistdir}/tex/generic/babel-german/ngermanb.ldf
%doc %{_texmfdistdir}/doc/generic/babel-german/germanb.pdf
%doc %{_texmfdistdir}/doc/generic/babel-german/ngermanb.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-german/german.ins
%doc %{_texmfdistdir}/source/generic/babel-german/germanb.dtx
%doc %{_texmfdistdir}/source/generic/babel-german/ngermanb.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
