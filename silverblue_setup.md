# Silverblue post install

You can get the silverblue cheatsheet of Fedora's Team Silverblue [here](https://docs.fedoraproject.org/en-US/fedora-silverblue/_attachments/silverblue-cheatsheet.pdf).

## Update the system

After the system is up, Silverblue, or perhaps by Gnome software, automatically download updates of your system, so running `rpm-ostree upgrade` after boot would only give `stderr`. You can wait and reboot later, usually Gnome would give notifications after the update is done. Although you can check the packages with:

```bash
rpm-ostree upgrade
```

If you just want a summary of update, such as the added, removed and upgraded do: `rpm-ostree upgrade --check` or `rpm-ostree upgrade --preview`

Update your preinstalled flatpaks, this may also not be necessary, since this is automatically updated by Gnome software center, but if you want to be sure, do:

```bash
flatpak update
```

And reboot after to apply the updates (there is also no problem to do this in GUI).

```bash
systemctl reboot
```

## Mount external drives and perhaps add it to `/etc/fstab`

If you have an external drive, which you can find with `lsblk` or `fdisk -l`, you can mount it into a folder and add it to `/etc/fstab` for automount in boot.

```bash
sudo mount /dev/sdX <dir>
```

And you can add it into `/etc/fstab` using `sudo nano /etc/fstab` or `vi` if you want. List the drives and their `UUID` with `lsblk -f` and add it to `/etc/fstab` with format of:

```
# Ignore the comments, this is and example to fstab entry, don't copy and paste this, your system won't boot
# UUID                                      # mount point (full), also  # filesystem format   # options # dump # fsck
#                                           # no env variables such as
#                                           # $HOME
# UUID=e423cfe8-5e8a-419c-87d0-8abb39aa498c /var/home/iaacornus/Storage	ext4	              defaults	0       0
# UUID=<your device uuid>                   <mount point>               <filesystem format> <options> <dump>  <fsck>
```

Here I suggest using `defaults` for options, 0 for `dump` and `fsck` to disable the checking (increasing the boot time, and avoiding potential errors, and since you only do checking if the drive is part of the OS filesystem), refer to [archwiki - fstab](https://wiki.archlinux.org/title/fstab). Check `/etc/fstab` with `cat /etc/fstab`. Be sure to input the correct UUID and options, other wise your system won't boot.

## Install rpm-fusion and other repos you need, codecs and applications

### Setup flatpak

```bash
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

### RPMfusion

Nonfree: `rpm-ostree install https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm`

Free: `rpm-ostree install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm`

For both: `rpm-ostree install https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm`

### `Openh264`

Fedora disable the automatic install of `openh264` by default, for this reason:

> Upstream Firefox versions download and install the OpenH264 plugin by default automatically. Due to it's binary nature, Fedora disables this automatic download.

You can install it `mozilla-openh264` and `gstreamer1-plugin-openh264` to support codecs in Firefox. And do `CTRL` + `Shift` + `A` in Firefox to go into the add ons manager > Plugins, and enable the OpenH264* plugins.

```
rpm-ostree install mozilla-openh264 gstreamer1-plugin-openh264
```

### Codecs

**For older version of intel use (replace `intel-media-driver` with `libva-intel-driver`)**

For intel (`intel-media-driver`) and then the codecs:

```
rpm-ostree install ffmpeg gstreamer1-plugin-libav gstreamer1-plugins-bad-free-extras gstreamer1-plugins-bad-freeworld gstreamer1-plugins-ugly gstreamer1-vaapi intel-media-driver
```

For AMD users, refer [here](https://rpmfusion.org/Howto/OSTree)

Reboot again.

## Install the apps from repo

Every boot, the system automatically runs  `rpm-ostree upgrade --check`, so you don't need to run it again.

### Nvidia install

Check first if you have nvidia card with `/sbin/lspci | grep -e 3D`, it would show you something like this:

```
02:00.0 3D controller: NVIDIA Corporation GP108M [GeForce MX230] (rev a1)
```

Otherwise, you don't have nvidia card, and don't proceed here. If you have nvidia card, install it, assuming you already installed rpmfusion repo nonfree

```bash
rpm-ostree install akmod-nvidia
```

And after reboot, check your nvidia install with `modinfo -F version nvidia`, it should give the version number of your driver such as `510.60.02`, not `stderr`.

### Flatpak modifications

#### Theming

Since flatpaks are sandboxed, you can either install the flatpak version of GTK theme you are using as flatpak as well, which you can find via:

```bash
flatpak search gtk3
```

Or override the `$HOME/.themes/` dir, with either one of the commands:

```
sudo flatpak override --system --filesystem=$HOME/.themes # if installed in home dir
sudo flatpak override --system --filesystem=xdg-data/themes
sudo flatpak override --system --filesystem=/usr/share/themes # if installed via rpm-ostree

```
#### Permissions

Other reddit users suggested, such as [u/IceOleg](https://www.reddit.com/user/IceOleg/), to override the `home` and `host` dir as well with:

```bash
flatpak override --user --nofilesystem=home
flatpak override --user --nofilesystem=host
```

Which can be given back to some applications that need it later on. [Flatseal](https://github.com/tchx84/flatseal) is also a good utility for managing permissions as [u/GunnarRoxen](https://www.reddit.com/user/GunnarRoxen/) suggested, can be installed with `flatpak install flathub com.github.tchx84.Flatseal`

The flatpak modifcations made can be reset by `sudo flatpak override --system --reset`. The `--system` flag can also be ommited, and `--user` can be used for user-wide changes.

### Theming

In some cases, where themes do not apply, especially in GTK-4, it can be forced by including it in `$HOME/.profile`, as well as the settings of gtk 4.0:

```
echo "export GTK_THEME=<theme-name>" >> $HOME/.profile; if [ ! -d $HOME/.config/environment.d/ ]; then mkdir -p $HOME/.config/environment.d/; fi; echo "GTK_THEME=<theme-name>" >> $HOME/.config/environment.d/gtk_theme.conf; echo "GTK_THEME=<theme-name>" >> $HOME/.config/gtk-4.0/settings.ini
```

**Replace `<theme-name>` with the name of the theme**

Which does (explanation):

1. `echo "export GTK_THEME=<theme-name>" >> $HOME/.profile`, append `export GTK_THEME=<theme-name>` to `$HOME/.profile`
2. Create `$HOME/.config/environment.d/gtk_theme.conf` file:

```bash
if [ ! -d $HOME/.config/environment.d/ ]; then
    mkdir -p $HOME/.config/environment.d/
fi

echo "GTK_THEME=<theme-name>" >> $HOME/.config/environment.d/gtk_theme.conf
```

And append `GTK_THEME=<theme-name>` at the end of the `gtk_theme.conf`

3. And finally append `GTK_THEME=<theme-name>` to `settings.ini` config.

If this didn't sufficed, then, you can try `sudo flatpak override --system --env=GTK_THEME='<theme-name>'`

## System optimizations

### Mask `NetworkManager-wait-online.service`

You can also mask `NetworkManager-wait-online.service`. It is simply a ["service simply waits, doing absolutely nothing, until the network is connected, and when this happens, it changes its state so that other services that depend on the network can be launched to start doing their thing."](https://askubuntu.com/questions/1018576/what-does-networkmanager-wait-online-service-do/1133545#1133545)

> In some multi-user environments part of the boot-up process can come from the network. For this case `systemd` defaults to waiting for the network to come on-line before certain steps are taken.

Masking it can decrease the boot time of at least ~15s-20s: `sudo systemctl disable NetworkManager-wait-online.service && sudo systemctl mask NetworkManager-wait-online.service`.

### Remove unnecessary gnome flatpaks

There are also some preinstalled flatpak that you can safely remove. You can completely remove the flatpak with `flatpak uninstall --system --delete-data <app>`. Here are some you can remove:

1. Calculator `org.gnome.Calculator`
2. Calendar `org.gnome.Calendar`
3. Connections `org.gnome.Connections`
4. Contacts `org.gnome.Contacts`
5. PDF reader `org.gnome.Evince` if you plan to install another pdf reader
6. Logs `org.gnome.Logs`
7. Maps `org.gnome.Maps`
8. Weather apps `org.gnome.Weather`
9. Disk usage analyzer `org.gnome.baobab`

### Disable Gnome Software

You can remove from from the autostart in `/etc/xdg/autostart/org.gnome.Software.desktop`, by:

```
sudo rm /etc/xdg/autostart/org.gnome.Software.desktop
```

This will save at least 100mb of RAM.

### Set battery threshold for laptop users

I recommend setting battery threshold of at least 80% to decrease wear on the battery. This can be done by echoing the threshold to `/sys/class/power_supply/BAT0/charge_control_end_threshold`. However, this resets every reboot, so it is good idea to make a systemd service for it:

```
[Unit]
Description=Set the battery charge threshold
After=multi-user.target
StartLimitBurst=0

[Service]
Type=oneshot
Restart=on-failure
ExecStart=/bin/bash -c 'echo 80 > /sys/class/power_supply/BAT0/charge_control_end_threshold'

[Install]
WantedBy=multi-user.target
```
