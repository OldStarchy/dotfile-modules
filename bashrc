export USER=$(whoami)

function ..() {
	local path="${1%/}"
	if [ -z "$path" ]; then
		explorer.exe .
	else
		explorer.exe "$path"
	fi
}


export PATH="$HOME/.dotfiles/bin:$PATH"
