# Upstream does not maintain a soversion so we define one here.
# abi-compliance-checker will be used to determine if an abi breakage occurs
# and the soversion will be incremented.
%global sover                            1.6

%define libbuffer                        %mklibname buffer %{sover}
%define libftoa                          %mklibname ftoa %{sover}
%define libgeneratedsaxparser            %mklibname generatedsaxparser %{sover}
%define libmathmlsolver                  %mklibname mathmlsolver %{sover}
%define libopencolladabaseutils          %mklibname opencolladabaseutils %{sover}
%define libopencolladaframework          %mklibname opencolladaframework %{sover}
%define libopencolladasaxframeworkloader %mklibname opencolladasaxframeworkloader %{sover}
%define libopencolladastreamwriter       %mklibname opencolladastreamwriter %{sover}
%define libutf                           %mklibname utf %{sover}
%define devname                          %mklibname %{name} -d

%global upname  OpenCOLLADA

%global uname   openCOLLADA

%define rel	1

Name:           opencollada
Version:        1.6.68
Release:        %mkrel %{rel}
License:        MIT
Summary:        Collada 3D import and export libraries
Group:          System/Libraries
Url:            https://collada.org/mediawiki/index.php/OpenCOLLADA

Source0:        https://github.com/KhronosGroup/OpenCOLLADA/archive/v%{version}/%{upname}-%{version}.tar.gz
# based from Gentoo: https://github.com/KhronosGroup/OpenCOLLADA/pull/561
Patch0:         opencollada-1.6.62-cmake-fixes.patch
# don't build DAEvalidator app
Patch1:         opencollada-1.6.62-no-daevalidator.patch
# fix build against pcre 8.42
Patch2:         opencollada-1.6.62-pcre-8.42.patch

BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(lib3ds)
BuildRequires:  pkgconfig(libpcreposix)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zziplib)

%description
COLLADA is a royalty-free XML schema that enables digital asset
exchange within the interactive 3D industry.
OpenCOLLADA is a Google summer of code opensource project providing
libraries for 3D file interchange between applications like blender.
COLLADABaseUtils          Utils used by many of the other projects
COLLADAFramework          Datamodel used to load COLLADA files
COLLADAStreamWriter       Sources (Library to write COLLADA files)
COLLADASaxFrameworkLoader Library that loads COLLADA files in a sax
                          like manner into the framework data model
COLLADAValidator          XML validator for COLLADA files, based on
                          the COLLADASaxFrameworkLoader
GeneratedSaxParser        Library used to load xml files in the way
                          used by COLLADASaxFrameworkLoader

%package        doc
Summary:        Developer documentation for %{uname}
Group:          Documentation
BuildArch:      noarch

%description    doc
This package provides documentation for %{name}.

%package -n     %{libbuffer}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries
# ease upgrade mga7
Conflicts:      %{_lib}opencollada0.3 < 0-6

%description -n %{libbuffer}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

%package -n     %{libftoa}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries
# ease upgrade mga7
Conflicts:      %{_lib}opencollada0.3 < 0-6

%description -n %{libftoa}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

%package -n     %{libgeneratedsaxparser}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries
# ease upgrade mga7
Conflicts:      %{_lib}opencollada0.3 < 0-6

%description -n %{libgeneratedsaxparser}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

GeneratedSaxParser is the library used to load xml files in the way
used by COLLADASaxFrameworkLoader.

%package -n     %{libmathmlsolver}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries
# ease upgrade mga7
Conflicts:      %{_lib}opencollada0.3 < 0-6

%description -n %{libmathmlsolver}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

%package -n     %{libopencolladabaseutils}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries
# ease upgrade mga7
Conflicts:      %{_lib}opencollada0.3 < 0-6

%description -n %{libopencolladabaseutils}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

COLLADABaseUtils is the package of utilitie used by many of the other
projects.

%package -n     %{libopencolladaframework}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries
# ease upgrade mga7
Conflicts:      %{_lib}opencollada0.3 < 0-6

%description -n %{libopencolladaframework}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

COLLADAFramework is the datamodel used to load COLLADA files.

%package -n     %{libopencolladasaxframeworkloader}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries
# ease upgrade mga7
Conflicts:      %{_lib}opencollada0.3 < 0-6

%description -n %{libopencolladasaxframeworkloader}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

COLLADASaxFrameworkLoader is a library that loads COLLADA files in a
SAX-like manner into the data framework model and is used by
COLLADASaxFrameworkLoader.

%package -n     %{libopencolladastreamwriter}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries
# ease upgrade mga7
Conflicts:      %{_lib}opencollada0.3 < 0-6

%description -n %{libopencolladastreamwriter}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

COLLADAStreamWriter contains the library to write COLLADA files.

%package -n     %{libutf}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries
# ease upgrade mga7
Conflicts:      %{_lib}opencollada0.3 < 0-6

%description -n %{libutf}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

%package -n     %{devname}
Summary:        Include files for openCOLLADA development
Group:          Development/C
Requires:       %{libbuffer} = %{version}-%{release}
Requires:       %{libftoa} = %{version}-%{release}
Requires:       %{libgeneratedsaxparser} = %{version}-%{release}
Requires:       %{libmathmlsolver} = %{version}-%{release}
Requires:       %{libopencolladabaseutils} = %{version}-%{release}
Requires:       %{libopencolladaframework} = %{version}-%{release}
Requires:       %{libopencolladasaxframeworkloader} = %{version}-%{release}
Requires:       %{libopencolladastreamwriter} = %{version}-%{release}
Requires:       %{libutf} = %{version}-%{release}
Provides:       %{uname}-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the include files necessary to build and
develop with the %{uname} export and import libraries.

%package        utils
Summary:        XML validator for COLLADA files
Group:          Development/Tools

%description    utils
XML validator for COLLADA files, based on the COLLADASaxFrameworkLoader.


%prep
%setup -q -n %{upname}-%{version}
%autopatch -p1

# Remove unused bundled libraries
rm -rf Externals/{Cg,expat,lib3ds,LibXML,MayaDataModel,pcre,zlib,zziplib}

# Add some docs, need to fix eol encoding with dos2unix in some files.
find ./ -name .project -delete
cp -pf COLLADAStreamWriter/README README.COLLADAStreamWriter
cp -pf COLLADAStreamWriter/LICENSE ./

iconv -f ISO_8859-1 -t utf-8 COLLADAStreamWriter/AUTHORS > \
  COLLADAStreamWriter/AUTHORS.tmp
touch -r COLLADAStreamWriter/AUTHORS COLLADAStreamWriter/AUTHORS.tmp
mv COLLADAStreamWriter/AUTHORS.tmp COLLADAStreamWriter/AUTHORS

dos2unix -f -k README.COLLADAStreamWriter
dos2unix -f -k LICENSE
dos2unix -f -k README
find htdocs/ -name *.php -exec dos2unix -f {} \;
find htdocs/ -name *.css -exec dos2unix -f {} \;


%build
%cmake -DUSE_STATIC=OFF \
       -DUSE_SHARED=ON \
       -DCMAKE_SKIP_RPATH=ON

%make_build


%install
%make_install -C build

# Manually install binary
mkdir -p %{buildroot}%{_bindir}/
install -p -m 0755 build/bin/* %{buildroot}%{_bindir}/

# Install MathMLSolver headers
mkdir -p %{buildroot}%{_includedir}/MathMLSolver
cp -a Externals/MathMLSolver/include/* %{buildroot}%{_includedir}/MathMLSolver/

%files doc
%doc htdocs/

%files -n %{libbuffer}
%{_libdir}/libbuffer.so.%{sover}

%files -n %{libftoa}
%{_libdir}/libftoa.so.%{sover}

%files -n %{libgeneratedsaxparser}
%{_libdir}/libGeneratedSaxParser.so.%{sover}

%files -n %{libmathmlsolver}
%{_libdir}/libMathMLSolver.so.%{sover}

%files -n %{libopencolladabaseutils}
%{_libdir}/libOpenCOLLADABaseUtils.so.%{sover}

%files -n %{libopencolladaframework}
%{_libdir}/libOpenCOLLADAFramework.so.%{sover}

%files -n %{libopencolladasaxframeworkloader}
%{_libdir}/libOpenCOLLADASaxFrameworkLoader.so.%{sover}

%files -n %{libopencolladastreamwriter}
%doc README README.COLLADAStreamWriter COLLADAStreamWriter/AUTHORS
%license LICENSE
%{_libdir}/libOpenCOLLADAStreamWriter.so.%{sover}

%files -n %{libutf}
%{_libdir}/libUTF.so.%{sover}

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/cmake/%{upname}/
%{_includedir}/*

%files utils
%doc README README.COLLADAStreamWriter COLLADAStreamWriter/AUTHORS
%license LICENSE
%{_bindir}/*
