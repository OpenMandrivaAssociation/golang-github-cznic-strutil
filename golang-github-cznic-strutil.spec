# https://github.com/cznic/strutil
%global goipath github.com/cznic/strutil
%global commit  529a34b1c186b483642a7a230c67521d9aa4b0fb

%gometa

Name:           golang-github-cznic-strutil
Version:        0
Release:        0.9%{?dist}
Summary:        Supplemental utilities for Go's strings package
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(github.com/cznic/mathutil)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTORS AUTHORS README


%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.9.20171016git529a34b
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.8.20171016git529a34b
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.7.20171016git529a34b
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git529a34b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git529a34b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.4.git529a34b
- Bump to commit 529a34b.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git43a8959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git43a8959
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.git43a8959
- First package for Fedora

