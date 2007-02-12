Summary:	Applies heuristic checks to BibTeX files
Summary(pl.UTF-8):   Heurystyczne sprawdzanie plików BibTeXa
Name:		bibcheck
Version:	0.10
Release:	1
License:	GPL v2
Group:		Applications
Source0:	ftp://ftp.math.utah.edu/pub/tex/bib/%{name}-%{version}.tar.bz2
# Source0-md5:	9797b2f862902b6f24ef74cc9d4d6d2a
URL:		http://www.ecst.csuchico.edu/~jacobsd/bib/tools/bibtex.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Applies heuristic checks to BibTeX files.

%description -l pl.UTF-8
Heurystyczne sprawdzanie plików BibTeXa.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/etc/env.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README *.txt *.ps *.hlp
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
