%global debug_package   %{nil}

Name:           rhvoice
Version:        1.8.0
Release:        7%{?dist}
Summary:        Free and open source speech synthesizer

License:        LGPLv2.1+
URL:            https://github.com/Olga-Yakovleva
Source0:        https://github.com/RHVoice/RHVoice/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        dict-from-libreoffice.txt
Source2:        dict-from-biglinux.txt
Source3:		cuintle-dict.txt
Source4:		talktext.sh

ExclusiveArch:  x86_64

BuildRequires:  gcc-c++
BuildRequires:  python3-scons
    
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libao-devel
BuildRequires:  portaudio-devel
  
BuildRequires:  speech-dispatcher-devel
BuildRequires:  python3-lxml

Requires:       speech-dispatcher
Requires:       libao

# Extra Requires
# Using this to provide extra functionalities
Requires:		speech-dispatcher-utils
Requires:		wl-clipboard
Requires:		xclip
Requires:       orca

Suggests:       pipewire-pulseaudio
Suggests:       portaudio
Suggests:       pulseaudio

Requires:       %{name}-american-english 
Requires:       %{name}-utils
Requires:       %{name}-speech-dispatcher-plugin

%description
RHVoice is a free and open source speech synthesizer by Olga Yakovleva.

%package        american-english
Summary:        American English voices for RHVoice
BuildArch:      noarch
    
Requires:       %{name}

%description    american-english
This package contains American English voices resources for RHVoice.

%package        scottish-english
Summary:        Scottish English voices for RHVoice
BuildArch:      noarch
    
Requires:       %{name}

%description    scottish-english
This package contains Scottish English voices resources for RHVoice.

%package        russian
Summary:        Russian voices for RHVoice
BuildArch:      noarch
    
Requires:       %{name}

%description    russian
This package contains Russian voices resources for RHVoice.

%package        ukrainian
Summary:        Ukrainian voices for RHVoice
BuildArch:      noarch
    
Requires:       %{name}

%description    ukrainian
This package contains Ukrainian voice resources for RHVoice.

%package        kyrgiz
Summary:        Kyrgiz voices for RHVoice
BuildArch:      noarch

Requires:       %{name}

%description    kyrgiz
This package contains Kyrgiz voices resources for RHVoice.

%package        esperanto
Summary:        Esperanto voices for RHVoice
BuildArch:      noarch

Requires:       %{name}

%description    esperanto
This package contains Esperanto voices resources for RHVoice.

%package        brazilian-portuguese
License:        CC-BY-SA-4.0
Summary:        Brazilian Portuguese voices for RHVoice
BuildArch:      noarch
    
Requires:       %{name}-brazilian-portuguese-extra-dictionaries

%description    brazilian-portuguese
This package contains Brazilian Portuguese voices resources for RHVoice.


%package        brazilian-portuguese-extra-dictionaries
License:        CC-BY-SA-4.0
Summary:        Brazilian Portuguese extra dictionaries for RHVoice
BuildArch:      noarch
    
Requires:       %{name}-brazilian-portuguese

%description    brazilian-portuguese-extra-dictionaries
This package contains Brazilian Portuguese extra dictionaries for RHVoice

%package        albanian
License:        CC-BY-SA-4.0
Summary:        Albanian voices for RHVoice
BuildArch:      noarch
    
Requires:       %{name}

%description    albanian
This package contains Albanian voices resources for RHVoice.

%package        tatar
License:        CC-BY-SA-4.0
Summary:        Tatar voices for RHVoice
BuildArch:      noarch
    
Requires:       %{name}

%description    tatar
This package contains Tatar voices resources for RHVoice.

%package        macedonian
License:        CC-BY-SA-4.0
Summary:        Macedonian voices for RHVoice
BuildArch:      noarch
    
Requires:       %{name}

%description    macedonian
This package contains Macedonian voices resources for RHVoice.

%package        polish
License:        CC-BY-SA-4.0
Summary:        Polish voices for RHVoice
BuildArch:      noarch
    
Requires:       %{name}

%description    polish
This package contains Polish voices resources for RHVoice.

%package        utils
Summary:        Helper utilities for RHVoice
Requires:       %{name}
    
%description    utils
This package contains helper utilities for RHVoice

%package        devel
Summary:        Development files for RHVoice

%description    devel
This package contains necessary header files for RHVoice-based applications development.

%package        speech-dispatcher-plugin
Summary:        Speech dispatcher plugin based on RHVoice
Requires:      %{name}

%description    speech-dispatcher-plugin
This package contains speech dispatcher plugin based on RHVoice.

%prep
%setup -q -n %{name}-%{version}

%build
scons prefix=%{_prefix} \
      bindir=%{_bindir} \
      libdir=%{_libdir} \
      localedirname=locale \
      extra_flags_release="$RPM_OPT_FLAGS $RPM_LD_FLAGS" %{?_smp_mflags}
  
%install
rm -rf $RPM_BUILD_ROOT
scons DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/RHVoice/languages/Brazilian-Portuguese/userdict/src

install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/RHVoice/languages/Brazilian-Portuguese/userdict/src/dict-from-libreoffice.txt
install -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/RHVoice/languages/Brazilian-Portuguese/userdict/src/dict-from-biglinux.txt
install -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/RHVoice/languages/Brazilian-Portuguese/userdict/src/cuintle-dict.txt

install -m 755 %{SOURCE4}  %{buildroot}/%{_bindir}/talktext.sh

%files
%doc README.md
%license LICENSE.md

%{_bindir}/talktext.sh

%{_libdir}/libRHVoice.so
%{_libdir}/libRHVoice.so.*
%{_libdir}/libRHVoice_core.so
%{_libdir}/libRHVoice_core.so.*
%{_libdir}/libRHVoice_audio.so
%{_libdir}/libRHVoice_audio.so.*
%config %{_prefix}/etc/RHVoice/RHVoice.conf

#TODO: changed sd_rhvoice Speech Dispatcher plugin to
# /usr/libexec instead of /lib64 
%files speech-dispatcher-plugin
%{_libdir}/speech-dispatcher-modules/sd_rhvoice

%files american-english
%{_datadir}/RHVoice/languages/English/*
%{_datadir}/RHVoice/voices/clb/*
%{_datadir}/RHVoice/voices/slt/*
%{_datadir}/RHVoice/voices/bdl/*
%{_datadir}/RHVoice/voices/lyubov/*
%{_datadir}/RHVoice/voices/evgeniy-eng/*

%files russian
%{_datadir}/RHVoice/languages/Russian/*
%{_datadir}/RHVoice/voices/aleksandr/*
%{_datadir}/RHVoice/voices/aleksandr-hq/*
%{_datadir}/RHVoice/voices/anna/*
%{_datadir}/RHVoice/voices/elena/*
%{_datadir}/RHVoice/voices/irina/*
%{_datadir}/RHVoice/voices/tatiana/*
%{_datadir}/RHVoice/voices/evgeniy-rus/*
%{_datadir}/RHVoice/voices/artemiy/*
%{_datadir}/RHVoice/voices/pavel/*
%{_datadir}/RHVoice/voices/vitaliy/*
%{_datadir}/RHVoice/voices/victoria/*
%{_datadir}/RHVoice/voices/yuriy/*
%{_datadir}/RHVoice/voices/arina/*
%{_datadir}/RHVoice/voices/mikhail/*

%files ukrainian
%{_datadir}/RHVoice/languages/Ukrainian/*
%{_datadir}/RHVoice/voices/anatol/*
%{_datadir}/RHVoice/voices/natalia/*
%{_datadir}/RHVoice/voices/marianna/*
%{_datadir}/RHVoice/voices/volodymyr/*

%files kyrgiz
%{_datadir}/RHVoice/languages/Kyrgyz/*
%{_datadir}/RHVoice/voices/azamat/*
%{_datadir}/RHVoice/voices/nazgul/*

%files esperanto
%{_datadir}/RHVoice/languages/Esperanto/*
%{_datadir}/RHVoice/voices/spomenka/*

%files brazilian-portuguese
%{_datadir}/RHVoice/languages/Brazilian-Portuguese/*
%{_datadir}/RHVoice/voices/Leticia-F123/*

%files brazilian-portuguese-extra-dictionaries
%{_datadir}/RHVoice/languages/Brazilian-Portuguese/userdict/src/dict-from-libreoffice.txt
%{_datadir}/RHVoice/languages/Brazilian-Portuguese/userdict/src/dict-from-biglinux.txt
%{_datadir}/RHVoice/languages/Brazilian-Portuguese/userdict/src/cuintle-dict.txt

%files scottish-english
%{_datadir}/RHVoice/voices/alan/*

%files albanian
%{_datadir}/RHVoice/languages/Albanian/*
%{_datadir}/RHVoice/voices/hana/*

%files tatar
%{_datadir}/RHVoice/languages/Tatar/*
%{_datadir}/RHVoice/voices/talgat/*

%files macedonian
%{_datadir}/RHVoice/languages/Macedonian/*
%{_datadir}/RHVoice/voices/suze/*
%{_datadir}/RHVoice/voices/kiko/*

%files polish
%{_datadir}/RHVoice/languages/Polish/*
%{_datadir}/RHVoice/voices/magda/*
%{_datadir}/RHVoice/voices/natan/*

%files devel
%{_includedir}/RHVoice.h
%{_includedir}/RHVoice_common.h

%files utils
%{_bindir}/RHVoice-test

# Excluded due to licensing issues
# https://github.com/RHVoice/RHVoice/pull/290
%ghost %{_datadir}/RHVoice/languages/Georgian/*
%ghost %{_datadir}/RHVoice/voices/natia/*

%changelog
* Tue Dec 27 2022 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.8.0-7
- talktext.sh script: Added missing pipe in SELECTION_CMD variable

* Tue Dec 27 2022 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.8.0-6
- fix typos on help function
- Changed default shell to bash

* Tue Dec 27 2022 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.8.0-5
- Added package brazilian-portuguese-extra-dictionaries with extra dictionaries for Brazilian Portuguese
- Added talktext script to read text from clipboard or selection using RHVoice

* Thu Aug 18 2022 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.8.0-4
- Dropped pipewire-pulseaudio as required dependency

* Thu Aug 18 2022 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.8.0-3
- Changed license to LGPLv2.1 or later
- Split Scottish English and American English
- Added new American English Evgeniy-eng voice
- Added new American English Lyubov voice
- Added new Albanian language and voice
- Added new Macedonian language and voice
- Added new Polish language and voice
- Added new Tatar language and voice
- Added new Russian Pavel voice
- Added new Russian Arina voice
- Added new Russian Artemiy voice
- Added new Russian Aleksandr-hq voice
- Added new Russian Vitaliy voice
- Added new Russian Victoria voice
- Added new Russian Mikhail voice
- Added new Russian Yuriy voice
- Added new Ukrainian Volodymyr voice
- Added new Ukrainian Marianna voice

* Wed Aug 17 2022 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.8.0-2
- Dropped nonfree sub-package in favor of brazilian-portuguese sub-package

* Wed Aug 17 2022 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.8.0-1
- New version
- New (out of laziness) new-voices-and-languages-bundle sub-package

* Tue Sep 29 2020 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.2.3-1
- New version

* Thu Sep 10 2020 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.2.2-2
- 1.2.2
- Regression due to audio issues (clipping) on master branch

* Thu Sep 10 2020 Xoloitzcuintle <xoloitzcuintle_god@protonmail.com> - 1.2.2-1
- New version (git version)
- Brazilian Portuguese language support (LetÃ­cia-F123 voice)
- License and Readme files
- New Russian voice (Artemiy)
- nonfree sub-package

* Tue Aug 21 2018 Alex <alex@linuxonly.ru> - 0.7.2-1
- Update version

* Mon Aug 20 2018 Alex <alex@linuxonly.ru> - 0.7.0-2
- Split voices, plugins and helper utilities

* Wed May 16 2018 Alex <alex@linuxonly.ru> - 0.7.0-1
- New version

* Thu Mar 29 2018 Alex <alex@linuxonly.ru> - 0.6.0-2
- Fix development package requirement

* Tue Oct 10 2017 Alex <alex@linuxonly.ru> - 0.6.0-1
- New version

* Sat Aug 27 2016 Alex <alex@linuxonly.ru> - 0.6.0-1
- First package for Fedora

