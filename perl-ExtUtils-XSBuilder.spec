#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
			# there are no tests defined currently, so
			# don't bother
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	XSBuilder
Summary:	ExtUtils::XSBuilder - Automatic XS glue code generation
Summary(pl):	ExtUtils::XSBuilder - automatyczne generowanie kodu ��cz�cego XS
Name:		perl-ExtUtils-XSBuilder
Version:	0.23
Release:	1
# same as Perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b6c8dee223cc9772ed6288ab223cfa54
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl
ExtUtils::XSBuilder to zbi�r modu��w do analizy plik�w nag��wkowych C
i tworzenia z nich kodu ��cz�cego XS oraz dokumentacji. W idealnej
sytuacji pozwala to na "napisanie" interfejsu do biblioteki C bez
kodowania ani jednej linii. Ale jako �e �adne API w C nie jest
idealne, w wi�kszo�ci przypadk�w potrzebne s� pewne poprawki - tak
wi�c aby u�ywa� tego modu�u nadal trzeba zna� si� na programowaniu w C
oraz XS, ale zapobiega on du�ej ilo�ci g�upiej pracy i copy-paste.
Tak�e kiedy API w C si� zmienia, wi�kszo�� roboty to ponowne
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/XSBuilder.pm
%{perl_vendorlib}/ExtUtils/XSBuilder
%{_mandir}/man3/*
