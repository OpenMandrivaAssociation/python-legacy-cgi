Name:		python-legacy-cgi
Version:	2.6.4
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/l/legacy_cgi/legacy_cgi-%{version}.tar.gz
Summary:	Fork of the standard library cgi and cgitb modules removed in Python 3.13
URL:		https://pypi.org/project/legacy-cgi/
License:	None
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

%description
Fork of the standard library cgi and cgitb modules removed in Python 3.13

This package is deprecated and for compatibility with previous versions
only. It may be removed from future releases without further notice.

%files
%{py_sitedir}/cgi.py
%{py_sitedir}/cgitb.py
%{py_sitedir}/legacy_cgi-*.*-info
%{py_sitedir}/__pycache__/*
