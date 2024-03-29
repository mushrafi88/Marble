# My customization of arch linux

I have decided to name it **Marble**

### Detailed Desktop environment :

| Category                 | Packages/Programs                                                                                                      |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Distribution**         | Arch Linux                                                                                                             |
| **Window Manager**       | Bspwm																						|
| **Keybindings**          | Sxhkd                                                            | 
| **Shell**                | Zsh	                                                                                                                |
| **Terminal**             | [Kitty](https://sw.kovidgoyal.net/kitty/)                                                              				|
| **Display Manager**      | Lightdm																|
| **Wallpaper Setter**     | Feh                                                                                                               |
| **Qt Themer**            | Qt5ct                                                                                                                  |
| **GTK Themer**           | lxappearance                                                                                      |
| **Apps Launcher**        | [Rofi](https://github.com/davatorium/rofi)                                                                             |
| **Panel**                | Polybar                                                                             |
| **Text Editor**          | Neovim                                                                                                    |
| **File Manager**		   | lf, Pcmanfm                                                                                                             |
| **Sound Mixer**          | Pipewire                                                                                                             |
| **Brightness Control**   | Light                                                          |
| **Network Manager**      | Networkmanager,Networkmanager-dmenu                                                   |
| **Image Viewer**         | Mirage                                                                 |               |
| **Screenshot App**       | Flameshot                                                    |
| **System Monitor (CLI)** | htop,ps_mem,nvtop,bandwhich,btop                                                                                                                |
| **Notification-daemon**  | [Dunst](https://wiki.archlinux.org/index.php/Dunst)                    										        |
| **Music Player (CLI)**   | Mpd, Mpc and Ncmpcpp
| **Lockscreen**           | Betterlockscreen                                                                                                       |


# [Detailed applists and a proper guide to setup the environment ](#marble)

# Screenshots

![](Screenshots/1.png)


![](Screenshots/2.png)

![](Screenshots/3.png)

![](Screenshots/4.png)

![](Screenshots/6.png)

![](Screenshots/7.png) 
### Commonly used keybindings :

| Key stroke               | Program                                                                                                       |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Terminal**         | super + Return                                                                                                             |
| **Rofi app launcher**       | alt + F1																						|
| **Rofi network manager**          | super + n                                                            | 
| **Rofi powermenu**                | super + x	                                                                                                                |
| **Screenshot**             | ctrl + alt + p                                                              				|                                                                                                            |
| **Rofi youtube searcher**            | ctrl + alt + y                                                                                                                  |
| **Kill an application**           | ctrl + alt + k                                                                                      |
| **Mpd increase/decrease sound**        | ctrl + alt + i/o                                                                             |
| **LF**                | ctrl + alt + h                                                                             |
| **System monitor**          | ctrl + alt + c                                                                                                      |
| **LibreWolf**		   | ctrl + alt + f                                                                                                             |
| **Ncmpcpp**          | ctrl + alt + m                                                                                                             |
| **Lockscreen**   | ctrl + alt + l                                                          |
| **Reload Keybindings**      | super + escape                                                   |
| **Quite/restart bspwm**         | ctrl + alt + q/r                                                                 |               |
| **Close app**       | alt + F4                                                    |
| **Force close** | ctrl + alt + escape                                                                                                                |
| **Change-wallpaper** | alt + c                  |
|**Fullscreen or Monocle** |super + f  |
|**Split horizontal, vertical or cancel** | super + {h,v,c} |
|**Toggle beetwen floating & tiled** |super + space |
|**Pseudo Tiled & tiled mode**|super + {p,t}  |
|**Send the window to another edge of the screen**|super + {_,shift + }{Left,Down,Up,Right} |
|**Change focus to next window, including floating window**|alt + {_,shift + }Tab |
|**Switch workspace**| ctrl + alt + {Left,Right} |
|**Send focused window to another workspace**|super + {_,shift + }{1-8}|
|**Expanding windows**|super + control + {Left,Right,Up,Down}|
|**Shrinking windows**|super + alt + {Left,Right,Up,Down}|
|**Move floating windows**|alt + shift + {Left,Down,Up,Right}|



# SYSTEM HARDWARE

## Brightness
```
yay -S --needed light-git
```

## Bluetooth
```
yay -S --needed bluez bluez-libs bluez-utils
```

## Sound
```
yay -S --needed alsa-plugins alsa-tools alsa-utils pavucontrol pipewire pipewire-alsa pipewire-pulse soundwire lib32-pipewire  lib32-alsa-plugins
```

# SYSTEM ENVIRONMENT

## Grub
```
yay -S sekiro-grub-theme-git
sudo cp -r -u -v /usr/share/grub/themes/sekiro /boot/grub/themes/
grub-mkconfig -o /boot/grub/grub.cfg
```
Make the following adjustments
```
sudo nvim /etc/default/grub
GRUB_DEFAULT=4
GRUB_TIMEOUT=3
GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet splash"
GRUB_THEME="/boot/grub/themes/sekiro/theme.txt"
GRUB_DISABLE_SUBMENU=y
GRUB_DISABLE_OS_PROBER=false
```


## Disk management
```
yay -S --needed btrfs-progs xfsprogs dosfstools exfat-utils f2fs-tools gnome-disk-utility gparted gptfdisk nfs-utils nilfs-utils ntfs-3g reiserfsprogs fuseiso fuse2 fuse3 jfsutils mtpfs gvfs gvfs-mtp
```

## System-essentials

yay installation
```
pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```
```
yay -S --needed hdparm mc mtools traceroute dmidecode efibootmgr efitools intel-ucode grub fakeroot libsass linux-lts-headers intel-compute-runtime intel-gpu-tools intel-media-driver vulkan-intel mesa-vdpau libva-intel-driver libva-mesa-driver libva-utils libva-vdpau-driver libvdpau-va-gl lib32-vulkan-intel xf86-video-intel-git lib32-giflib lib32-gst-plugins-base-libs lib32-libxslt lib32-mesa lib32-mesa-demos lib32-mpg123 lib32-nvidia-utils lib32-ocl-icd lib32-opencl-nvidia lib32-vulkan-icd-loader libnewt libtool linux linux-atm linux-firmware linux-headers linux-lts lsb-release lshw lsof lzop m4 macchanger xf86-input-synaptics nvidia nvidia-lts nvidia-dkms xdg-user-dirs wget zsh usbutils openssh optimus-manager-qt-git os-prober pacman-contrib vdpauinfo virtualgl sudo ocl-icd patch pkgconf pptpclient pv python-pip python-pkgconfig speedtest-cli sshfs reflector rp-pppoe rsync sdparm sox numlockx tcpdump haveged dialog jq ffnvcodec-headers intel-media-sdk wimlib glib2-docs graphviz gts netpbm vala xorg-xhost gst-libav gst-plugins-bad gst-plugins-base gst-plugins-good gst-plugins-ugly inotify-tools lib32-alsa-plugins lib32-gnutls lib32-gtk3 lib32-libjpeg-turbo lib32-libldap lib32-libpulse lib32-libva lib32-libxcomposite lib32-openal lib32-sqlite lib32-v4l-utils linux-zen  linux-zen-headers libheif libvirt libwmf luajit poppler-data poppler-glib vulkan-headers udiskie parallel wpa_supplicant xdg-utils
```

## App builiding
```
yay -S --needed asciidoc atool cmake autoconf autofs automake base bind binutils bison bmon boost devtools extra-cmake-modules imake make meson npm nodejs man-db man-pages gcc go gobject-introspection git downgrade jre8-openjdk ninja
```

## Compression
```
yay -S --needed zip rar p7zip unzip
```

## Xorg
```
yay -S --needed xorg-font-util xorg-server xorg-xinit xorg-xinput xorg-xkill xorg-xwininfo xclip xscreensaver xprintidle xorg-fonts-type1 xorg-server-xephyr
```

## Internet-tools
```
yay -S --needed dhcpcd ethtool netctl network-manager-applet networkmanager networkmanager-dmenu-git nmap iwd ndisc6
```

## Python Packages

```
yay -S --needed python-blessings python-httplib2 python-pandas python-pycodestyle python-pylint python-pyx python-scapy python-seaborn python-xlrd python-adblock python-guessit python-levenshtein python-openpyxl python-pdfkit python-pynvim python-weasyprint python-pysmartdl
```

# Desktop environment

## Marble
```
yay -S --needed bspwm rofi-git picom-git polybar-git sxhkd feh ksuperkey ranger lxappearance qt5ct pcmanfm kitty dunst neovim-git qutebrowser-git zathura zathura-djvu zathura-ps zathura-pdf-poppler zscroll-git playerctl polybar-spotify-module nerd-fonts-jetbrains-mono noto-fonts-cjk ttf-material-design-icons-git ttf-material-design-icons ttf-font-awesome-4 arc-gtk-theme arc-icon-theme gtk-engine-murrine mpc mpd ncmpcpp-git mpv-git flameshot spotify-dev ueberzug networkmanager-dmenu-git cava ccache
```

```
git clone https://gitlab.com/mushrafi88/dotfiles.git ~/.config
git clone https://gitlab.com/mushrafi88/bin.git ~/.config/bin
rm -rf ~/config/bin/.git
cp -r -u -v ~/.config/{.zsh,.zshrc,.Xresources} ~/
chmod +x ~/.config/bin/*
chmod +x ~/bspwm/bspwmrc
touch ~/.config/mpd/{mpd.db,mpd.log,mpd.pid}
```
If rofi fonts not working check 
```
https://github.com/adi1090x/rofi.git
```
If polybar fonts not working install all the fonts given below
if mpd ncmpcpp causes trouble because of icu
```
yay -S raptor harfbuzz-icu mpd-git mpc ncmpcpp-git
```

## Menu
```
yay -S --needed dmenu-git rofi-git rofi-bluetooth-git
```

## System fonts
```
yay -S --needed awesome-terminal-fonts cozette-otb noto-fonts noto-fonts-emoji nerd-fonts-jetbrains-mono noto-fonts-cjk xorg-font-util nerd-fonts-hermit nerd-fonts-source-code-pro ttf-dejavu ttf-droid ttf-freebanglafont gucharmap noto-fonts-emoji ttf-font-awesome-4 ttf-dejavu ttf-droid ttf-jetbrains-mono ttf-liberation ttf-material-design-icons-git ttf-material-design-icons texinfo ttf-bitstream-vera ttf-all-the-icons siji-git ttf-comfortaa font-bh-ttf fontpreview-ueberzug-git gsfonts
```

## Display manager
```
yay -S --needed lightdm-gtk-greeter lightdm-webkit-theme-litarvan lightdm-webkit2-greeter
```
Setup
```
sudo nvim /etc/lightdm/lightdm.conf
greeter-session=lightdm-webkit2-greeter
sudo nvim /etc/lightdm/lightdm-webkit2-greeter.conf
webkit_theme=litarvan
user_image = /usr/share/pixmaps/.face
sudo cp -r -u -v ~/.face /usr/share/pixmaps/
sudo cp -r -u -v /home/venerable_white/Pictures/work /usr/share/backgrounds/
```

## Lockscreen

# Zsh shell Setup
```
yay -S zsh 
sudo chsh -s /bin/zsh
chsh -S /bin/zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
yay -S fzf zsh-completions zsh-syntax-highlighting
```


# Nvim setup

install vim-plug
```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```
In nvim
```
PlugInstall
```

# Scientific Computing
First install cuda,cudnn,nvidia,nvidia-utils.

```
yay -S --needed nvidia nvidia-utils cuda cudnn miniconda3
```
Then use conda environment
add this to .zshrc
```
[ -f /opt/miniconda3/etc/profile.d/conda.sh ]  && source /opt/miniconda3/etc/profile.d/conda.sh 
```
For cpu just omit -gpu
```
conda create –name tf2.0_gpu
conda activate tf2.0
conda install pip
conda install tensorflow-gpu pandas numpy
conda install -c conda-forge jupyterlab
```
Test if its working
```
python
from tensorflow.python.client import device_lib
device_lib.list_local_devices()
```
Install list
```
yay -S --needed miniconda3 gcc-fortran cuda cudnn julia gnuplot
```
secondary option 
import whole environment in conda
```
conda create -n tf2.0_gpu --file conda_env_setup.txt
```
for cpu remove tensorflow-gpu with just tensorflow
# Pip
```
pip install youtube_search manga-py
```
```
pip install youtube-dl
pip3 install -U git+https://github.com/vn-ki/anime-downloader.git
```

# Flatpak
Install list
```
yay -S flatpak
```
```
flatpak install okular
flatpak install kdenlive
flatpak install kdeapps kdeconnect
```
add this to .zshrc
```
export PATH="${PATH}:/var/lib/flatpak/exports/bin"
```
Flatpak app config location

```
~/.var/app/APP/config
```
dark mode
```
flatpak install flathub org.kde.KStyle.Adwaita
```
add this line below to allow qt applications to run a specific theme 
```
echo QT_STYLE_OVERRIDE=Adwaita-dark >> /etc/environment
```
for gtk use this
```
flatpak run --env=GTK_THEME=Arc-Dark APP
```
to run the flatpak package with darkmode only in qt
```
flatpak override --user --env=QT_STYLE_OVERRIDE=Adwaita-Dark org.kde.okular
flatpak override --user --env=QT_STYLE_OVERRIDE=Adwaita-Dark org.kde.kdeconnect
```
Overrides are stored in ~/.local/share/flatpak/overrides 


# Non-Essential Applications to make life better
```
yay -S --needed  mirage mpc ncmpcpp-git mpd mpv-git mugshot stremio-beta scrot cheese feh tumbler flameshot cava spotify-dev firefox-beta-bin qutebrowser-git google-chrome-beta pcmanfm which ncdu perl-rename filezilla ranger zoom telegram-desktop discord atomicparsley ffmpegthumbnailer epub-thumbnailer-git timeshift-bin droidcam obs-studio fbreader pdfjs zathura zathura-ps zathura-pdf-poppler zathura-djvu transmission-gtk-git megasync-bin wget  aria2 freedownloadmanager youtube-dl-git gdown anime-downloader-git autojump ncdu pfetch-git neofetch fd expac gn zsh-syntax-highlighting ueberzug tdrop-git kitty tmux ripgrep mlocate wps-office neovim-git groff pandoc texlive-most android-tools htop powertop nvtop kmon bandwhich ps_mem at cronie evernote-beta-bin tldr upwork ccache sfeed
```
Package list for non-essential applications


## Media
might need to add this to ~/.xinitrc or ~/.config/bspwm/bspwmrc
xhost +
Package list

* mirage
* mpc
* ncmpcpp-git
* mpd
* mpv-git
* mugshot
* stremio-beta
* scrot
* cheese
* feh
* tumbler
* flameshot
* cava
* spotify-dev

## Browser
* firefox-beta-bin
* qutebrowser-git
* google-chrome-beta

## File manager
Package list
* pcmanfm
* which
* ncdu
* perl-rename
* filezilla
* ranger

## Social 

* zoom
* telegram-desktop
* discord

## Thmbnail writer
* atomicparsley
* ffmpegthumbnailer
* epub-thumbnailer-git

## Backup
* timeshift-bin

## Camera
Package list
* droidcam
* obs-studio

## Pdf reader
Package list
* fbreader
* pdfjs
* zathura
* zathura-djvu
* zathura-ps
* zathura-pdf-poppler

## Downloaders
Package list
* transmission-gtk-git
* megasync-bin
* wget 
* aria2
* freedownloadmanager
* youtube-dl-git
* gdown
* anime-downloader-git

## Terminal-utility
Package list
* autojump
* ncdu
* pfetch-git
* neofetch
* fd
* expac
* gn
* zsh-syntax-highlighting
* ueberzug
* tdrop-git
* kitty
* tmux
* ripgrep
* mlocate

## Editor
Package list 
* wps-office
* neovim-git
* groff
* pandoc
* texlive-most

## Android
* android-tools

## Showinfo
Package list
* htop
* powertop
* nvtop
* kmon
* bandwhich
* ps_mem

## Periodic task manager
* at
* cronie
* evernote-beta-bin

## Cheat sheet
* tldr

## Work
* upwork

## System cleaner
* ccache

## RSS-feed
* sfeed
