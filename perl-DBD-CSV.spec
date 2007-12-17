%define	realname    DBD-CSV
%define	name	    perl-%{realname}
%define	version	    0.22
%define	release	    %mkrel 2

Name:		%{name}
Summary:	Perl module to access CSV files through DBI
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}
Source:		http://search.cpan.org/CPAN/authors/id/J/JZ/JZUCKER/%{realname}-%{version}.tar.bz2
Buildrequires:	perl-devel perl-DBI
BuildRequires:	perl-Text-CSV_XS >= 0.16, perl-SQL-Statement >= 0.1011
Buildarch:	noarch


%description
DBD::CSV is a Perl module that provides yet another driver for the DBI
(Database independent interface for Perl).  This one is based on the SQL
"engine" SQL::Statement and the abstract DBI driver DBD::File, and implements
access to so-called CSV files (comma seperated values).  Such files are
mostly used for exporting MS Access and MS Excel data.


%prep 
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

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

