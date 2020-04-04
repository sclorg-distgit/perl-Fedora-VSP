%{?scl:%scl_package perl-Fedora-VSP}

Name:           %{?scl_prefix}perl-Fedora-VSP
Version:        0.001
Release:        18%{?dist}
Summary:        Perl version normalization for RPM
License:        GPLv3+
URL:            https://ppisar.fedorapeople.org/Fedora-VSP/
Source0:        %{url}Fedora-VSP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-interpreter
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
* Tue Jan 07 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-18
- Re-rebuild of bootstrapped packages

* Thu Dec 19 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-17
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-15
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-11
- Perl 5.28 re-rebuild of bootstrapped packages

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-7
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 30 2016 Petr Pisar <ppisar@redhat.com> - 0.001-4
- Break build cycle when bootstrapping: perl-Fedora-VSP → perl-generators
  → perl-Fedora-VSP

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Petr Pisar <ppisar@redhat.com> 0.001-1
- First package
