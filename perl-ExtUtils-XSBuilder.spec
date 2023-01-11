#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	XSBuilder
Summary:	ExtUtils::XSBuilder - automatic XS glue code generation
Summary(pl.UTF-8):	ExtUtils::XSBuilder - automatyczne generowanie kodu łączącego XS
Name:		perl-ExtUtils-XSBuilder
Version:	0.28
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1d33ddeacc01426a02e23c71c2e4cd04
URL:		http://search.cpan.org/dist/ExtUtils-XSBuilder/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Tie-IxHash
%endif
Requires:	perl-Tie-IxHash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::XSBuilder is a set modules to parse C header files and
create XS glue code and documentation out of it. Idealy this allows to
"write" an interface to a C library without coding a line. Since no
C-API is ideal, some adjuments are necessary most of the time. So to
use this module you must still be familar with C and XS programming,
but it removes a lot of stupid work and copy&paste from you. Also when
the C API changes, most of the time you only have to rerun XSBuilder
to get your new Perl API.

%description -l pl.UTF-8
ExtUtils::XSBuilder to zbiór modułów do analizy plików nagłówkowych C
i tworzenia z nich kodu łączącego XS oraz dokumentacji. W idealnej
sytuacji pozwala to na "napisanie" interfejsu do biblioteki C bez
kodowania ani jednej linii. Ale jako że żadne API w C nie jest
idealne, w większości przypadków potrzebne są pewne poprawki - tak
więc aby używać tego modułu nadal trzeba znać się na programowaniu w C
oraz XS, ale zapobiega on dużej ilości głupiej pracy i copy-paste.
Także kiedy API w C się zmienia, większość roboty to ponowne
uruchomienie XSBuildera dla uzyskania nowego perlowego API.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/XSBuilder.pm
%{perl_vendorlib}/ExtUtils/XSBuilder
%{_mandir}/man3/ExtUtils::XSBuilder*.3pm*
%{_mandir}/man3/ExtUtils::xsbuilder.osc2002.3pm*
