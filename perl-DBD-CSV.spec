%define	upstream_name    DBD-CSV
%define upstream_version 0.41

%if %{_use_internal_dependency_generator}
%define __noautoreq '/pro/bin/perl'
%else
%define _requires_exceptions /pro/bin/perl
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl module to access CSV files through DBI
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JZ/JZUCKER/%{upstream_name}-%{upstream_version}.tgz

BuildRequires:	perl-devel
BuildRequires:	perl(DBI)
BuildRequires:	perl(SQL::Statement) >= 0.1011
BuildRequires:	perl(Text::CSV_XS) >= 0.16

BuildArch:	noarch

%description
DBD::CSV is a Perl module that provides yet another driver for the DBI
(Database independent interface for Perl).  This one is based on the SQL
"engine" SQL::Statement and the abstract DBI driver DBD::File, and implements
access to so-called CSV files (comma seperated values).  Such files are
mostly used for exporting MS Access and MS Excel data.

%prep 
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/Bundle/DBD/*
%{perl_vendorlib}/DBD/*
%{_mandir}/*/*

%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.300.0-2mdv2011.0
+ Revision: 681351
- mass rebuild

* Wed Jul 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.300.0-1mdv2011.0
+ Revision: 553079
- update to 0.30

* Wed Mar 17 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.280.0-1mdv2010.1
+ Revision: 523431
- update to 0.28

* Thu Feb 18 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.1
+ Revision: 507585
- update to 0.27

* Sun Nov 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.1
+ Revision: 471048
- update to 0.26

* Sun Nov 08 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.250.0-2mdv2010.1
+ Revision: 462973
- forgot to bump mkrel
- sanitized spec file
- removing dependency on /pro/bin/perl, used as shebang in a file (!?)

* Sat Nov 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.1
+ Revision: 462448
- update to 0.25.tgz

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.1
+ Revision: 461729
- update to 0.22

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.0
+ Revision: 403091
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.22-4mdv2009.0
+ Revision: 241202
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.22-2mdv2008.0
+ Revision: 67485
- buildrequires obsoletes buildprereq


* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.22-2mdk
- remove -q

* Mon May 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.22-1mdk
- 0.22
- spec cleanup

* Wed May 19 2004 Michael Scherer <misc@mandrake.org> 0.21-1mdk
- new version
- rpmbuildupdate aware
- new url
- automatic requires

* Tue Aug 12 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2002-6mdk
- rebuild
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- use %%makeinstall_std macro

* Wed Jul 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2002-5mdk
- buildrequires from Michael Scherer

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2002-4mdk
- rebuild for new auto{prov,req}

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2002-3mdk
- buildrequires

* Fri Jan 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2002-2mdk
- rebuild

* Wed Jul 24 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2002-1mdk
- 0.2002

* Fri Mar 01 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.1030-1mdk
- 0.1030

* Thu Aug 23 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1027-1mdk
- updated to 0.1027

* Tue Sep 12 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.1023-1mdk
- updated to 0.1023

* Sat Jul 22 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.1022-3mdk
- build for new perl
- macroization

* Mon May 01 2000 Vincent Danen <vdanen@linux-mandrake.com> 0.1022-2mdk
- fix group

* Wed Mar 08 2000 Vincent Danen <vdanen@linux-mandrake.com>
- 0.1022

* Tue Mar 07 2000 Vincent Danen <vdanen@linux-mandrake.com>
- initial specfile
- bzip sources

