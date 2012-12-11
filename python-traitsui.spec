%define module	traitsui

Summary:	Enthought Tool Suite - traitsui project
Name:		python-%{module}
Version:	4.2.0
Release:	1
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/traitsui/
BuildArch:	noarch
Obsoletes:	python-enthought-traits-ui
Obsoletes:	python-enthought-traitsgui
Requires:	python-traits >= 4.1.0
Requires:	python-pyface >= 4.1.0
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	python-sphinx

%description
The traitsui project contains a toolkit-independent GUI abstraction
layer (known as Pyface), which is used to support the "visualization"
features of the Traits package. Thus, you can write code in terms of
the Traits API (view, items, editors, etc.), and let TraitsGUI and
your selected toolkit and backend take care of the details of
displaying them.

The following GUI backends are supported:

- wxPython
- PyQt
- PySide

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build
pushd docs
make html
popd

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc *.txt *.rst examples/ docs/build/html



%changelog
* Tue Dec 27 2011 Lev Givon <lev@mandriva.org> 4.1.0-1
+ Revision: 745663
- Update to 4.1.0.

* Sun Jul 10 2011 Lev Givon <lev@mandriva.org> 4.0.1-1
+ Revision: 689412
- Update to 4.0.1.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-2
+ Revision: 689265
- Rebuild.
- Fix install dep.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 689188
- import python-traitsui


