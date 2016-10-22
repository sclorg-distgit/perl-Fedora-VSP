%{?scl:%scl_package perl-Fedora-VSP}

Name:           %{?scl_prefix}perl-Fedora-VSP
Version:        0.001
Release:        4%{?dist}
Summary:        Perl version normalization for RPM
License:        GPLv3+
Group:          Development/Libraries
URL:            https://ppisar.fedorapeople.org/Fedora-VSP/
Source0:        %{url}Fedora-VSP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
%if !%{defined perl_bootstrap}
# Break build cycle: perl-Fedora-VSP → perl-generators → perl-Fedora-VSP
BuildRequires:  %{?scl_prefix}perl-generators
%endif
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(version)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
%if %{defined perl_bootstrap}
# Break build cycle: perl-Fedora-VSP → perl-generators → perl-Fedora-VSP
Requires:       %{?scl_prefix}perl(strict)
Requires:       %{?scl_prefix}perl(warnings)
Provides:       %{?scl_prefix}perl(Fedora::VSP) = %{version}
%endif

%description
This module provides functions for normalizing Perl version strings for
Red Hat Package (RPM) based Linux distributions.

%prep
%setup -q -n Fedora-VSP-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc COPYING
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon May 30 2016 Petr Pisar <ppisar@redhat.com> - 0.001-4
- Break build cycle when bootstrapping: perl-Fedora-VSP → perl-generators
  → perl-Fedora-VSP

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Petr Pisar <ppisar@redhat.com> 0.001-1
- First package
