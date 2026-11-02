REPO_DIR="$HOME/.local/share/nvim/site/pack/packer/start/packer.nvim"
REPO_URL="git@github.com:wbthomason/packer.nvim.git"

if [ -d "$REPO_DIR" ]; then
	cd $REPO_DIR
	REMOTE_URL=$(git remote get-url origin)
	if [ "$REMOTE_URL" = "$REPO_URL" ]; then
		echo "Directory already exists and contains the correct git repository. Pulling instead."
		git pull --ff-only
	else
		echo "Directory exists but does not contain the correct git repository. Please check the directory."
		exit 1
	fi
else
	git clone --depth 1 $REPO_URL $REPO_DIR
fi
