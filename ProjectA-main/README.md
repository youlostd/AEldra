# ProjectA

# ----- Setup Root ----- #
Recommand: Freebsd 13.1 64bit

pkg install -y nano htop boost-all devil cryptopp openssl gmake makedepend python python2 python27 mariadb105-server gdb protobuf



# ----- Setup mysql server ----- #
ee /etc/rc.conf
Add:
mysql_enable="YES"

-------------------
mysql -u root -p






# ----- Setup game server ----- #
Enter /usr and create "home"
Enter /usr/home
Linking: ln -s /usr/home /home

Unzip the game.tgz: "tar xf game.tgz"
Give it the permissioons: "chmod -R 777 game"
