#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	RBLClient
Summary:	Net::RBLClient - Queries multiple Realtime Blackhole Lists in parallel
Summary(pl):	Net::RBLClient - odpytywanie wielu list RBL równolegle
Name:		perl-Net-RBLClient
Version:	0.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4691f4a80b31c83491dcbc53fc4c1e02
URL:		http://search.cpan.org/dist/Net-RBLClient/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is used to discover what RBLs are listing a particular
IP address. It parallelizes requests for fast response.

An RBL, or Realtime Blackhole List, is a list of IP addresses meeting
some criteria such as involvement in Unsolicited Bulk Email. Each RBL
has its own criteria for addition and removal of addresses. If you
want to block email or other traffic to/from your network based on one
or more RBL's, you should carefully study the behavior of those RBL's
before and during such blocking.

%description -l pl
Ten modu³ s³u¿y do ustalania, które RBL zawieraj± dany adres IP.
Zrównolegla on zapytania w celu otrzymania odpowiedzi szybciej.

RBL (Realtime Blackhole List) to lista adresów IP spe³niaj±cych pewne
kryteria, takie jak udzia³ w wysy³aniu spamu. Ka¿dy RBL ma w³asne
kryteria dodawania i usuwania adresów. Aby zablokowaæ pocztê lub inny
ruch z/do w³asnej sieci w oparciu o jeden lub wiêcej RBL, nale¿y
uwa¿nie zaznajomiæ siê z zachowaniem danego RBL przed i w czasie
takiego blokowania.

%prep
%setup -q -n RBLCLient-%{version}

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
%doc README
%{perl_vendorlib}/Net/*.pm
%{_mandir}/man3/*
