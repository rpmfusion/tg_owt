%undefine __cmake_in_source_build
%global debug_package %{nil}

%global commit0 25c8637f5975db830cc5d74477641a8b609e248d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20220201

# Git revision of libyuv...
%global commit1 ad890067f661dc747a975bc55ba3767fe30d4452
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name: tg_owt
Version: 0
Release: 16.%{date}git%{shortcommit0}%{?dist}

# Main project - BSD
# abseil-cpp - ASL 2.0
# libsrtp - BSD
# libyuv - BSD
# openh264 - BSD
# pffft - BSD
# rnnoise - BSD
License: BSD and ASL 2.0
Summary: WebRTC library for the Telegram messenger
URL: https://github.com/desktop-app/%{name}

Source0: %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Source1: https://chromium.googlesource.com/libyuv/libyuv/+archive/%{commit1}.tar.gz#/libyuv-%{shortcommit1}.tar.gz

# https://github.com/desktop-app/tg_owt/pull/90
Patch100: %{name}-gcc12-fixes.patch

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(usrsctp)
BuildRequires: pkgconfig(vpx)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xtst)

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: yasm

# Disabling all low-memory architectures.
ExclusiveArch: x86_64 aarch64

%description
Special fork of the OpenWebRTC library for the Telegram messenger.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: bundled(abseil-cpp) = 0~git39f46fa
Provides: bundled(base64) = 0~git
Provides: bundled(fft) = 0~git
Provides: bundled(g711) = 1.1~git
Provides: bundled(g722) = 1.14~git
Provides: bundled(libsrtp) = 2.2.0~git94ac00d
Provides: bundled(libyuv) = 1767~git%{shortcommit1}
Provides: bundled(ooura) = 0~git
Provides: bundled(openh264) = 1.10.0~git6f26bce
Provides: bundled(pffft) = 0~git483453d
Provides: bundled(portaudio) = 0~git
Provides: bundled(rnnoise) = 0~git91ef40
Provides: bundled(sigslot) = 0~git
Provides: bundled(spl_sqrt_floor) = 0~git
Requires: pkgconfig(alsa)
Requires: pkgconfig(epoxy)
Requires: pkgconfig(gbm)
Requires: pkgconfig(libavcodec)
Requires: pkgconfig(libavformat)
Requires: pkgconfig(libavutil)
Requires: pkgconfig(libdrm)
Requires: pkgconfig(libjpeg)
Requires: pkgconfig(libpipewire-0.3)
Requires: pkgconfig(libpulse)
Requires: pkgconfig(libswresample)
Requires: pkgconfig(libswscale)
Requires: pkgconfig(openssl)
Requires: pkgconfig(opus)
Requires: pkgconfig(usrsctp)
Requires: pkgconfig(vpx)
Requires: pkgconfig(x11)
Requires: pkgconfig(xcomposite)
Requires: pkgconfig(xdamage)
Requires: pkgconfig(xext)
Requires: pkgconfig(xfixes)
Requires: pkgconfig(xrandr)
Requires: pkgconfig(xrender)
Requires: pkgconfig(xtst)

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{commit0} -p1
tar -xf %{SOURCE1} -C src/third_party/libyuv

mkdir legal
cp -f -p src/third_party/abseil-cpp/LICENSE legal/LICENSE.abseil-cpp
cp -f -p src/third_party/abseil-cpp/README.chromium legal/README.abseil-cpp
cp -f -p src/third_party/libsrtp/LICENSE legal/LICENSE.libsrtp
cp -f -p src/third_party/libsrtp/README.chromium legal/README.libsrtp
cp -f -p src/third_party/libyuv/LICENSE legal/LICENSE.libyuv
cp -f -p src/third_party/libyuv/PATENTS legal/PATENTS.libyuv
cp -f -p src/third_party/libyuv/README.chromium legal/README.libyuv
cp -f -p src/third_party/openh264/src/LICENSE legal/LICENSE.openh264
cp -f -p src/third_party/openh264/README.chromium legal/README.openh264
cp -f -p src/third_party/pffft/LICENSE legal/LICENSE.pffft
cp -f -p src/third_party/pffft/README.chromium legal/README.pffft
cp -f -p src/third_party/rnnoise/COPYING legal/LICENSE.rnnoise
cp -f -p src/third_party/rnnoise/README.chromium legal/README.rnnoise
cp -f -p src/common_audio/third_party/ooura/LICENSE legal/LICENSE.ooura
cp -f -p src/common_audio/third_party/ooura/README.chromium legal/README.ooura
cp -f -p src/common_audio/third_party/spl_sqrt_floor/LICENSE legal/LICENSE.spl_sqrt_floor
cp -f -p src/common_audio/third_party/spl_sqrt_floor/README.chromium legal/README.spl_sqrt_floor
cp -f -p src/modules/third_party/fft/LICENSE legal/LICENSE.fft
cp -f -p src/modules/third_party/fft/README.chromium legal/README.fft
cp -f -p src/modules/third_party/g711/LICENSE legal/LICENSE.g711
cp -f -p src/modules/third_party/g711/README.chromium legal/README.g711
cp -f -p src/modules/third_party/g722/LICENSE legal/LICENSE.g722
cp -f -p src/modules/third_party/g722/README.chromium legal/README.g722
cp -f -p src/modules/third_party/portaudio/LICENSE legal/LICENSE.portaudio
cp -f -p src/modules/third_party/portaudio/README.chromium legal/README.portaudio
cp -f -p src/rtc_base/third_party/base64/LICENSE legal/LICENSE.base64
cp -f -p src/rtc_base/third_party/base64/README.chromium legal/README.base64
cp -f -p src/rtc_base/third_party/sigslot/LICENSE legal/LICENSE.sigslot
cp -f -p src/rtc_base/third_party/sigslot/README.chromium legal/README.sigslot

%build
# CMAKE_BUILD_TYPE should always be Release due to some hardcoded checks.
# Warning: Building as a shared library is not supported by upstream.
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DTG_OWT_USE_PROTOBUF:BOOL=OFF \
    -DTG_OWT_PACKAGED_BUILD:BOOL=ON
%cmake_build

%install
%cmake_install

%files devel
%doc src/AUTHORS src/OWNERS legal/README.*
%license LICENSE src/PATENTS legal/LICENSE.* legal/PATENTS.*
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.a

%changelog
* Tue Feb 01 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0-16.20220201git25c8637
- Updated to latest Git snapshot.
- Switched to packaged version of libvpx.
- Switched to packaged version of usrsctp.

* Thu Dec 09 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0-15.20211207gitd5c3d43
- Updated to latest Git snapshot.
- Build with OpenSSL 3.0 on Fedora 36+.

* Tue Nov 16 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0-14.20211021gitd578c76
- Build with OpenSSL 1.1 on Fedora 36+.

* Mon Nov 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0-13.20211021gitd578c76
- Updated to latest Git snapshot.

* Mon Aug 02 2021 Alexey Gorgurov <alexfails@fedoraproject.org> - 0-12.20210627git91d836d
- Revert to upstream libvpx/livyuv commits

* Thu Jul 29 2021 Alexey Gorgurov <alexfails@fedoraproject.org> - 0-11.20210627git91d836d
- Fixed depedencies from libpipewire-0.3, libpulse, x11 components and ALSA.

* Tue Jul 27 2021 Leigh Scott <leigh123linux@gmail.com> - 0-10.20210627git91d836d
- Updated to latest Git snapshot.

* Mon Mar 22 2021 Alexey Gorgurov <alexfails@fedoraproject.org> - 0-9.20210321git2d804d2
- Converted to static-only library as the upstream doesn't support shared builds.

* Sat Mar 20 2021 Alexey Gorgurov <alexfails@fedoraproject.org> - 0-8.20210321git2d804d2
- Updated to latest Git snapshot.

* Wed Feb 24 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0-7.20210203gita198773
- Updated to latest Git snapshot.

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0-6.20210124gitbe23804
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Feb 01 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0-5.20210124gitbe23804
- Updated to latest Git snapshot.

* Wed Dec 23 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-4.20201218git6eaebec
- Updated to latest Git snapshot.

* Fri Nov 20 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-3.20201112git10b988a
- Updated to latest Git snapshot.
