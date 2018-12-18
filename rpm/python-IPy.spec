# based on work by The Fedora Project (2017)
# Copyright (c) 1998, 1999, 2000 Thai Open Source Software Center Ltd
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

%define python3_sitelib /%{_libdir}/python3.?/site-packages

Summary:        Python module for handling IPv4 and IPv6 Addresses and Networks
Name:           python3-IPy
Version:        0.83
Release:        21
URL:            https://github.com/haypo/python-ipy
Source:         %{name}-%{version}.tar.gz
License:        BSD
BuildRequires:  python3-devel
BuildArch:      noarch
Patch0:         Remove-broken-test.patch

%description
IPy is a Python 3 module for handling IPv4 and IPv6 Addresses and Networks 
in a fashion similar to perl's Net::IP and friends. The IP class allows 
a comfortable parsing and handling for most notations in use for IPv4 
and IPv6 Addresses and Networks.

%prep
%setup -q -n %{name}-%{version}/python-IPy
%patch0 -p1


%build
%{__python3} setup.py build

%check
PYTHONPATH=$PWD %{__python3} test/test_IPy.py
PYTHONPATH=$PWD %{__python3} test_doc.py


%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%doc COPYING
%doc AUTHORS ChangeLog README.rst
%{python3_sitelib}/IPy*
%{python3_sitelib}/__pycache__/IPy*
