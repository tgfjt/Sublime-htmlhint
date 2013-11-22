Sublime-htmlhint
================

htmlhint plugin for Sublime Text

[README for Japanese](/tgfjt/Sublime-htmlhint/blob/master/README.ja.md)

**via Node.js**

* Be sure your `Node.js` is installed.
* If you need, please [Set](#settings) your Node Path.

**DEV NOTE:**

* This is beta now
* I don't check on Windows, Linux
* take care version of htmlhint

## Getting Started

clone this repo to your SublimeText "Packages" directory

Ex.

* ST2 `~/Library/Application Support/Sublime Text 2/Packages/`
* ST3 `~/Library/Application Support/Sublime Text 3/Packages/`

## Usage

**Htmlhint**

run `Htmlhint` on HTML file

* `Ctrl+Shift+J` on OS X
* `Alt+Shift+J` on Win, Linux

### Settings

`Preferences > Package Settings > Sublime-htmlhint > Setting - User`


* .htmlhintrc path
 
```
{
	"htmlhintrc": "/path/to/your/.htmlhintrc"
}
```

* node path

Ex:

 `/usr/local/bin/node`, `/Users/NAME/.nodebrew/current/bin/node`

```
{
	"node_path": "/path/to/your/usr/node"
}
```
