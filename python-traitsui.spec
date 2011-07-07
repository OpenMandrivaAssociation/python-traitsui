%define module	traitsui
%define name	python-%{module}
%define version 4.0.0
%define release	%mkrel 1

Summary:	Enthought Tool Suite - traitsui project
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://code.enthought.com/projects/traits_gui/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Obsoletes:	python-enthought-traits-ui
Obsoletes:	python-enthought-traitsgui
Requires:	python-traits >= 4.0.0
Requires:	python-pyface >= 4.0.0
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
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt *.rst examples/ docs/build/html

