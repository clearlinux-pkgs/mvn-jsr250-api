#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jsr250-api
Version  : 1.0
Release  : 2
URL      : https://repo1.maven.org/maven2/javax/annotation/jsr250-api/1.0/jsr250-api-1.0.jar
Source0  : https://repo1.maven.org/maven2/javax/annotation/jsr250-api/1.0/jsr250-api-1.0.jar
Source1  : https://repo1.maven.org/maven2/javax/annotation/jsr250-api/1.0/jsr250-api-1.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CDDL-1.0
Requires: mvn-jsr250-api-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-jsr250-api package.
Group: Data

%description data
data components for the mvn-jsr250-api package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/annotation/jsr250-api/1.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/javax/annotation/jsr250-api/1.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/annotation/jsr250-api/1.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/javax/annotation/jsr250-api/1.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/javax/annotation/jsr250-api/1.0/jsr250-api-1.0.jar
/usr/share/java/.m2/repository/javax/annotation/jsr250-api/1.0/jsr250-api-1.0.pom
