%define	upstream_name    DBD-CSV
%define upstream_version 0.30

%define _requires_exceptions /pro/bin/perl

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl module to access CSV files through DBI
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JZ/JZUCKER/%{upstream_name}-%{upstream_version}.tgz

Buildrequires:	perl(DBI)
BuildRequires:  perl(SQL::Statement) >= 0.1011
BuildRequires:	perl(Text::CSV_XS) >= 0.16

Buildarch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
DBD::CSV is a Perl module that provides yet another driver for the DBI
(Database independent interface for Perl).  This one is based on the SQL
"engine" SQL::Statement and the abstract DBI driver DBD::File, and implements
access to so-called CSV files (comma seperated values).  Such files are
mostly used for exporting MS Access and MS Excel data.

%prep 
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/Bundle/DBD/*
%{perl_vendorlib}/DBD/*
%{_mandir}/*/*
