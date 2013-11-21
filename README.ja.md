Sublime-htmlhint
================

htmlhint plugin for Sublime Text


**NOTE:**

* Linux, Windowsで試してない
* Htmlhintがfork版

## Getting Started

clone this repo to your SublimeText "Packages" directory

Ex.

* ST2 `~/Library/Application Support/Sublime Text 2/Packages/`
* ST3 `~/Library/Application Support/Sublime Text 3/Packages/`


## Usage

** Htmlhint **

`Htmlhint`コマンドを実行する

* `Ctrl+Shift+J` on OS X
* `Alt+Shift+J` on Win, Linux

### 設定変更

`Preferences > Package Settings > Sublime-htmlhint > Setting - User`

* .htmlhintrcのパス

```
{
	"htmlhintrc": "/path/to/your/.htmlhintrc"
}
```

* nodeのパス

Ex: `/usr/local/bin/node`, `/Users/NAME/.nodebrew/current/bin/node`

```
{
	"node_path": "/path/to/your/usr/node"
}
```