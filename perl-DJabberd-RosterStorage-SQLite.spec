%define realname   DJabberd-RosterStorage-SQLite

Name:		perl-%{realname}
Version:    1.00
Release:    %mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
Summary:    DJabber plugin to store your jabber roster in SQLite
Source0:    http://search.cpan.org/CPAN/authors/id/B/BR/BRADFITZ/DJabberd-RosterStorage-SQLite-%{version}.tar.bz2
# patch submitted upstream : http://lists.danga.com/pipermail/djabberd/2007-September/000401.html
# not applied however, i have been using it since 1 year
Patch0:     DJabberd-RosterStorage-SQLite-fixutf8.diff
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:	perl-DJabberd
# for testing, maybe one day
# BuildRequires: perl-DBD-SQLite
Requires:       perl-DBD-SQLite
BuildArch: noarch

%description
DJabber plugin to store your jabber roster in SQLite.

%prep
%setup -q -n DJabberd-RosterStorage-SQLite-%{version}
%patch -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# without this, djabberd try to write to its log file
export LOGLEVEL=WARN
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{perl_vendorlib}/DJabberd/
%{_mandir}/man3/*


