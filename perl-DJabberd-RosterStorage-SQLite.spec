%define realname   DJabberd-RosterStorage-SQLite

Name:		perl-%{realname}
Version:	1.00
Release:	8
License:	GPL or Artistic
Group:		Development/Perl
Summary:	DJabber plugin to store your jabber roster in SQLite
Source0:	http://search.cpan.org/CPAN/authors/id/B/BR/BRADFITZ/DJabberd-RosterStorage-SQLite-%{version}.tar.bz2
# patch submitted upstream : http://lists.danga.com/pipermail/djabberd/2007-September/000401.html
# not applied however, i have been using it since 1 year
Patch0:		DJabberd-RosterStorage-SQLite-fixutf8.diff
Url:		http://search.cpan.org/dist/%{realname}

BuildRequires:	perl-devel
BuildRequires:	perl(DJabberd)
BuildRequires:	perl(DBI)
# for testing, maybe one day
# BuildRequires: perl-DBD-SQLite
Requires:	perl(DBD::SQLite)
BuildArch:	noarch

%description
DJabber plugin to store your jabber roster in SQLite.

%prep
%setup -q -n DJabberd-RosterStorage-SQLite-%{version}
%patch -p0

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# without this, djabberd try to write to its log file
export LOGLEVEL=WARN
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/DJabberd/
%{_mandir}/man3/*

%changelog
* Fri Sep 26 2008 Michael Scherer <misc@mandriva.org> 1.00-5mdv2009.0
+ Revision: 288538
- add old fix for utf8 roster

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.00-4mdv2009.0
+ Revision: 256689
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.00-2mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Michael Scherer <misc@mandriva.org> 1.00-2mdv2008.0
+ Revision: 90842
- add missing requires


* Mon Nov 13 2006 Michael Scherer <misc@mandriva.org> 1.00-1mdv2007.0
+ Revision: 83882
- fix test when djabberd is installed
- Import perl-DJabberd-RosterStorage-SQLite

* Sun Nov 05 2006 Michael Scherer <misc@mandriva.org> 1.00-1mdv2007.1
- First Mandriva package

