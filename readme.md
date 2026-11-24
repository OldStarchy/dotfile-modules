This is an example dotfiles repo based on my own.

You may fork it and customize it however you like. It uses submodules to other branches in this repo so that you may get updates if/when I update them (I have been steadily adding things to the `git` branch/submodule).

To configure this for use in devcontainers in VSCode add the following settings (replace the url with your own fork):

```jsonc
{
  "dotfiles.repository": "git@github.com:OldStarchy/dotfile-modules.git",
  "dotfiles.targetPath": "~/.dotfiles",
}
```

and optionally if you want to sync these settings (as they don't sync by default)

```jsonc
{
  "settingsSync.ignoredSettings": [
    "-dotfiles.repository",
    "-dotfiles.targetPath",
  ],
}
```

## configure gpg pinentry

1. Download and install Gpg4win https://gpg4win.org/download.html
2. configure gpg in wls to use the pinentry.exe that comes with Gpg4win
	```bash
	echo "pinentry-program /mnt/c/Program Files (x86)/Gpg4win/bin/pinentry.exe" >> ~/.gnupg/gpg-agent.conf
	```
3. restart gpg-agent
	```bash
	gpg-connect-agent reloadagent /bye
	gpgconf --reload gpg-agent # this may be optional
	```
4. Follow the github instructions on
	1. [creating a gpg key](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key)
	2. [adding it to your github account](https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-gpg-key-to-your-github-account)
	3. and [adding it to your git config](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key)
5. Tell git to sign all commits by default
	```bash
	git config --global commit.gpgsign true
	```
