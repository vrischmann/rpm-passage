# RPM spec for passage

## Prerequisites

Setup your tree:
```
$ rpmdev-setuptree
```

## Building

```
$ spectool -C ~/rpmbuild/SOURCES -g passage.spec
$ rpmbuild -ba passage.spec
$ sudo dnf install ~/rpmbuild/RPMS/noarch/passage-10.0-1.fc36.noarch.rpm
```

Note that the version is arbitrary and doesn't match to any upstream version.
