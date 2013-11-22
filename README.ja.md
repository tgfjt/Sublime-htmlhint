Sublime-htmlhint
================

htmlhint plugin for Sublime Text

**via Node.js**

* node.jsを経由します。
* nodeのパス設定が必要な場合は[設定](#%E8%A8%AD%E5%AE%9A%E5%A4%89%E6%9B%B4)してください。

[README for Japanese](/tgfjt/Sublime-htmlhint/blob/master/README.ja.md)

**DEV NOTE:**

* Linux, Windowsで試してない
* Htmlhintがfork版

## 始め方

お使いの SublimeText "Packages" ディレクトリに `git clone`してください。

例.

* ST2 `~/Library/Application Support/Sublime Text 2/Packages/`
* ST3 `~/Library/Application Support/Sublime Text 3/Packages/`


## 使い方

**Htmlhint**

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

例:

 `/usr/local/bin/node`, `/Users/NAME/.nodebrew/current/bin/node`

```
{
	"node_path": "/path/to/your/usr/node"
}
```

* ショートカットキー

`Preferences > Package Settings > Sublime-htmlhint > Key Bindings - User`

OSXでの初期設定は、`shift+ctrl+j`

```
[{
  "keys": ["shift+ctrl+j"], "command": "htmlhint"
}]
```
