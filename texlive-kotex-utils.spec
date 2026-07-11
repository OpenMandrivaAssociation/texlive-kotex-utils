%global tl_name kotex-utils
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1.0
Release:	%{tl_revision}.1
Summary:	Utility scripts and support files for typesetting Korean
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/korean/kotex-utils
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-utils.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-utils.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(kotex-utf)
Requires:	texlive(kotex-utils.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides scripts and support files for index generation in
Korean language typesetting. The files belong to the ko.TeX bundle.

