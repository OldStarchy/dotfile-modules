Manually configure git to include the \*.gitconfig files you want via

```
[include]
	path = ~/.dotfiles/git/alias.gitconfig
	path = ~/.dotfiles/git/template.gitconfig
	path = ~/.dotfiles/git/etc.gitconfig
```

Be sure to include the correct relative path to the files.

## `ll` and `llf` alias' link configuration

The `ll` and `llf` alias' look for an `Issue: ` trailer and print ansi urls to your ticketing platform.
This requires you to configure the base url to your ticketing platform using the `ll.base` config value.

`git config ll.base https://tickets.example.com/browse/`

The trailer will be appended to that config value to make the full link.

eg. with the following config

```gitconfig
[ll]
    base = https://tickets.example.com/browse/
```

will yield the following, assuming each commit message has a `Issue: WORK-001` trailer.

`WORK-001` are (ctrl+)clickable ansi links

```bash
$ git ll
f555627 G test: add back some of the more useful tests WORK-001
e2101bf G refactor: name and move some more things WORK-001
6ed8985 G refactor: rename test methods WORK-001
...
```

```bash
$ git llf
f555627 G test: add back some of the more useful tests https://tickets.example.com/browse/WORK-001
e2101bf G refactor: name and move some more things https://tickets.example.com/browse/WORK-001
6ed8985 G refactor: rename test methods https://tickets.example.com/browse/WORK-001
...
```

Note that gits format setting doesn't have conditional rendering, so if the trailer does not exist, you will still get the following output:

```bash
$ git ll
f555627 G test: add back some of the more useful tests
e2101bf G refactor: name and move some more things
6ed8985 G refactor: rename test methods
...
```

```bash
$ git llf
f555627 G test: add back some of the more useful tests https://tickets.example.com/browse/
e2101bf G refactor: name and move some more things https://tickets.example.com/browse/
6ed8985 G refactor: rename test methods https://tickets.example.com/browse/
...
```

The output from `ll` has a 0-width ansi link (making it invisible) but the `llf` still shows the base path.
