# revision 32101
# category Package
# catalog-ctan /language/korean/kotex-utils
# catalog-date 2013-11-08 09:28:00 +0100
# catalog-license lppl
# catalog-version 2.0.1
Name:		texlive-kotex-utils
Version:	2.0.1
Release:	8
Summary:	Utility scripts and support files for typesetting Korean
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/korean/kotex-utils
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-utils.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-utils.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-kotex-utf
Provides:	texlive-kotex-utils.bin = %{EVRD}

%description
The bundle provides scripts and support files for index
generation in Korean language typesetting. The files belong to
the ko.TeX bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/jamo-normalize
%{_bindir}/komkindex
%{_bindir}/ttf2kotexfont
%{_texmfdistdir}/makeindex/kotex-utils/kotex.ist
%{_texmfdistdir}/makeindex/kotex-utils/memucs-manual.ist
%{_texmfdistdir}/scripts/kotex-utils/jamo-normalize.pl
%{_texmfdistdir}/scripts/kotex-utils/komkindex.pl
%{_texmfdistdir}/scripts/kotex-utils/ttf2kotexfont.pl
%doc %{_texmfdistdir}/doc/latex/kotex-utils/ChangeLog
%doc %{_texmfdistdir}/doc/latex/kotex-utils/README
%doc %{_texmfdistdir}/doc/latex/kotex-utils/utf8-lang.xdy
%doc %{_texmfdistdir}/doc/latex/kotex-utils/utf8.xdy

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf ../share/texmf-dist/scripts/kotex-utils/jamo-normalize.pl jamo-normalize
    ln -sf ../share/texmf-dist/scripts/kotex-utils/komkindex.pl komkindex
    ln -sf ../share/texmf-dist/scripts/kotex-utils/ttf2kotexfont.pl ttf2kotexfont
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
