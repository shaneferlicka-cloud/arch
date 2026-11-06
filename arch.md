# Arch Linux VM Installation Documentation

## Overview

For this assignment, I manually installed Arch Linux in a virtual machine using the official Arch Linux Installation Wiki and google when raging.

My completed VM uses:

- Arch Linux
- Xfce desktop environment
- SDDM display manager
- Bash
- OpenSSH
- Automatic graphical boot
- Terminal color coding
- Custom Bash aliases
- Additional Xfce utilities and themes

---

## 1. Verify the Installation Environment

```bash
ls /sys/firmware/efi/efivars
```

Checks that the VM booted using UEFI.

```bash
ping -c 4 archlinux.org
```

Checks network connectivity.

```bash
timedatectl
```

Checks system time and synchronization.

---

## 2. Identify and Partition the Disk

```bash
lsblk
```

Displays disks and partitions.

```bash
cfdisk /dev/sda
```

Used to create the EFI System Partition and Linux root partition.

> The exact disk name may be different depending on the VM configuration.

---

## 3. Format the Partitions

```bash
mkfs.fat -F 32 /dev/sda1
```

Formats the EFI partition as FAT32.

```bash
mkfs.ext4 /dev/sda2
```

Formats the root partition as ext4.

---

## 4. Mount the Filesystems

```bash
mount /dev/sda2 /mnt
```

Mounts the root filesystem.

```bash
mkdir -p /mnt/boot
```

Creates the boot directory.

```bash
mount /dev/sda1 /mnt/boot
```

Mounts the EFI partition.

```bash
lsblk
```

Verifies the partitions and mount points.

---

## 5. Install Arch Linux

```bash
pacstrap -K /mnt base linux linux-firmware
```

Installs the base Arch Linux system, kernel, and firmware.

---

## 6. Generate the Filesystem Table

```bash
genfstab -U /mnt >> /mnt/etc/fstab
```

Creates the filesystem configuration used during boot.

```bash
cat /mnt/etc/fstab
```

Checks the generated configuration.

---

## 7. Enter the New Arch System

```bash
arch-chroot /mnt
```

Changes into the newly installed Arch system.

---

## 8. Configure Time and Locale

```bash
ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime
```

Sets the time zone.

```bash
hwclock --systohc
```

Synchronizes the hardware clock.

```bash
nano /etc/locale.gen
```

I enabled:

```text
en_US.UTF-8 UTF-8
```

Then ran:

```bash
locale-gen
```

Created the locale configuration:

```bash
echo "LANG=en_US.UTF-8" > /etc/locale.conf
```

---

## 9. Configure the Hostname

My hostname is:

```text
archlinux
```

The hostname is configured with:

```bash
echo "archlinux" > /etc/hostname
```

---

## 10. Set the Root Password

```bash
passwd
```

Sets the password for the root account.

---

## 11. Install GRUB

```bash
pacman -S grub efibootmgr
```

Installs GRUB and EFI boot management tools.

```bash
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
```

Installs GRUB for UEFI.

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

Generates the GRUB configuration.

---

## 12. Create User Accounts

My normal user account is:

```text
mod
```

I also created the required `codi` account.

```bash
useradd -m -G wheel mod
passwd mod
```

```bash
useradd -m -G wheel codi
passwd codi
```

The `wheel` group is used for sudo access.

---

## 13. Configure sudo

```bash
pacman -S sudo
```

Installs sudo.

```bash
EDITOR=nano visudo
```

I enabled:

```text
%wheel ALL=(ALL:ALL) ALL
```

This allows users in the `wheel` group to use `sudo`.

---

## 14. Finish the Base Installation

```bash
exit
```

Exits the chroot environment.

```bash
umount -R /mnt
```

Unmounts the installed filesystems.

```bash
reboot
```

Reboots into the installed Arch system.

---

# Post-Installation Configuration

## 15. Update Arch Linux

```bash
sudo pacman -Syu
```

Updates installed packages and package databases.

---

## 16. Install Xfce

```bash
sudo pacman -S xorg-server xfce4 xfce4-goodies
```

Installs:

- Xorg graphical display system
- Xfce desktop environment
- Additional Xfce utilities and plugins

I chose **Xfce** because it is lightweight while still providing a complete desktop environment.

---

## 17. Install SDDM

```bash
sudo pacman -S sddm
```

Installs the SDDM graphical login manager.

```bash
sudo systemctl enable sddm.service
```

Configures SDDM to start automatically.

I also created an SDDM configuration directory:

```bash
sudo mkdir -p /etc/sddm.conf.d
```

Then edited the Xfce configuration:

```bash
sudo nano /etc/sddm.conf.d/10-xfce.conf
```

---

## 18. Boot Into the GUI Automatically

```bash
sudo systemctl set-default graphical.target
```

Sets the graphical environment as the default boot target.

I verified it with:

```bash
systemctl get-default
```

I also checked SDDM:

```bash
systemctl is-enabled sddm.service
```

Then rebooted:

```bash
sudo reboot
```

---

## 19. Install and Enable SSH

```bash
sudo systemctl enable --now sshd
```

Enables the SSH server at boot and starts it immediately.

I checked the VM's IPv4 address with:

```bash
ip addr
```

---

## 20. Configure Bash

I checked my current shell with:

```bash
echo $SHELL
```

I also checked whether Bash was installed with:

```bash
command -v bash
```

My shell configuration is stored in:

```text
~/.bashrc
```

I edited it using:

```bash
sudo nano ~/.bashrc
```

After making changes, I reloaded it with:

```bash
source ~/.bashrc
```

---

## 21. Add Terminal Color Coding

I configured Bash so commands such as `ls` display color output.

An example command I used while testing this was:

```bash
ls --color=auto /usr/bin | head -30
```

I also added color directly to my `ll` alias.

---

## 22. Add Bash Aliases

I added the following aliases to `~/.bashrc`:

```bash
# Custom Arch Linux aliases
alias update='sudo pacman -Syu'
alias ll='ls -lah --color=auto'
alias ..='cd ..'
alias ...='cd ../..'
alias c='clear'
alias myip='ip -br addr'
```

I then applied the changes:

```bash
source ~/.bashrc
```

I checked the configured aliases with:

```bash
alias
```

### Alias Purposes

| Alias | Command | Purpose |
|---|---|---|
| `update` | `sudo pacman -Syu` | Updates Arch Linux |
| `ll` | `ls -lah --color=auto` | Detailed colored file listing |
| `..` | `cd ..` | Move up one directory |
| `...` | `cd ../..` | Move up two directories |
| `c` | `clear` | Clears the terminal |
| `myip` | `ip -br addr` | Displays IP addresses in a short format |

---

## 23. VM Integration

I installed the SPICE guest agent:

```bash
sudo pacman -S spice-vdagent
```

This improves integration between the virtual machine and the host.

---

## 24. Customize Xfce

I attempted to install additional themes:

```bash
sudo pacman -S arc-gtk-theme papirus-icon-theme
```

I later tried:

```bash
sudo pacman -S materia-gtk-theme papirus-icon-theme
```

I also installed the Xfce Whisker Menu plugin:

```bash
sudo pacman -S xfce4-whiskermenu-plugin
```

---

## 25. Install Additional Utilities

```bash
sudo pacman -S fastfetch btop htop git vim
```

Installed several system and administration tools.

I tested Fastfetch with:

```bash
fastfetch
```

I also installed additional Xfce monitoring tools:

```bash
sudo pacman -S xfce4-systemload-plugin xfce4-taskmanager
```

---

# Problems and Recovery

## GUI Did Not Start Automatically

After installing Xfce and SDDM, I needed to make sure the system booted directly into the graphical environment.

I used:

```bash
sudo systemctl enable sddm.service
sudo systemctl set-default graphical.target
```

Then rebooted:

```bash
sudo reboot
```

---

## SDDM Configuration

I needed to create an SDDM configuration directory manually:

```bash
sudo mkdir -p /etc/sddm.conf.d
```

I then edited:

```bash
sudo nano /etc/sddm.conf.d/10-xfce.conf
```

I rebooted several times while testing the graphical login configuration.

---

## Theme Installation

I attempted to install:

```bash
sudo pacman -S arc-gtk-theme papirus-icon-theme
```

and later:

```bash
sudo pacman -S materia-gtk-theme papirus-icon-theme
```

This was part of customizing the Xfce desktop and testing which theme packages were available.

---

