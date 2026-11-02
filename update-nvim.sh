echo Updating nvim

TMPDIR=$(mktemp -d)
echo Using temp dir $TMPDIR

pushd $TMPDIR
NVIM_FILE=nvim-linux-x86_64.appimage

DOWNLOAD_URL=$(curl -s https://api.github.com/repos/neovim/neovim/releases | grep browser_download_url | cut -d '"' -f 4 | grep "$NVIM_FILE$" | head -n 1)

curl -LO $DOWNLOAD_URL
chmod u+x $NVIM_FILE
./$NVIM_FILE --appimage-extract

./squashfs-root/AppRun --version

sudo rm -rf /squashfs-root
sudo mv squashfs-root /
rm $NVIM_FILE
popd
rmdir $TMPDIR

sudo ln -s /squashfs-root/AppRun /usr/bin/nvim || true

echo Done.
