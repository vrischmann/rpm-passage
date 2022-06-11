%global commit 1262d308f09db9b243513a428ab4b8fb1c30d31d

Summary:	A fork of password-store (https://www.passwordstore.org) that uses age (https://age-encryption.org) as backend.
Name:		passage
Version:	10.0
Release:	1%{?dist}
BuildArch:	noarch

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
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/passage
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/passage.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_passage

%license COPYING

%changelog

* Sat Jun 11 2022 Vincent Rischmann <vincent@rischmann.fr> - 10.0-1
- First version
