# baidu dict

命令行下中日英文翻译工具（Chinese and English and Japanese translation tools in the command line）

PS: 在基础上增加了日语翻译，并将有道翻译替换成了百度翻译【仅供学习】https://github.com/FeeiCN/dict(wufeifei)


## 安装(Install)

```bash
sudo pip install dict-cli
```

## 用法(Usage)

#### 中译日(Chinese To Japanese)
```bash
$ dict 早上好
###################################
#  早上好 (phonetic: -)
#
#
#  おはよう (phonetic: -)
###################################
```

#### 英译中(English To Chinese)

```bash
$ dict thank you
###################################
#  thank you (phonetic: 谢 谢 您 )
#
#
#  谢谢您 (phonetic: xiè xie nín )
###################################
```
#### 日译中(Japanese To Chinese)
```bash
$ dict どうもありがとうございました
###################################
#  どうもありがとうございました (phonetic: 谢 谢 您 的 关 照 )
#
#
#  谢谢您的关照 (phonetic: xiè xie nín de guān zhào )
###################################