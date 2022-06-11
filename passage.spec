%global commit 1262d308f09db9b243513a428ab4b8fb1c30d31d

Summary:	A fork of password-store (https://www.passwordstore.org) that uses age (https://age-encryption.org) as backend.
Name:		passage
Version:	10.0
Release:	1%{?dist}

License:	GPL
URL:		https://github.com/FiloSottile/passage
Source0:	https://github.com/FiloSottile/passage/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:	make
BuildRequires:	gcc

%description
A fork of password-store (https://www.passwordstore.org) that uses age (https://age-encryption.org) as backend.

%prep
%autosetup -n %{name}-%{commit}

%build

%install
%{__rm} -rf %{buildroot}
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/*
%{_mandir}/man1/*

%license LICENSE

%changelog

* Sat, 11 Jun 2022 Vincent Rischmann <vincent@rischmann.fr> - 10.0-1
- First version
