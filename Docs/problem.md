#### 1：AttributeError: module 'lxml' has no attribute 'etree'；
```
原因：anaconda中base环境中如果有lxml包的话，虚拟环境就会报错。
解决方案：在base环境中执行: pip uninstall -y lxml。
```
