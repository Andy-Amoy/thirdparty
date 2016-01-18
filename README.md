# thirdparty介绍
对常用的第三方库进行汇总整理，便于以后项目中使用。
部分库是通过网上收集而来，在里面已经提供了blade BUILD文件，
而更多的是在以往的项目中引用到而添加BUILD文件。
因此，全部第三方库都已经配套有blade BUILD文件可以直接拿来使用，
省却依赖库的编译依赖配置细节，并且全都在linux centos 7测试通过。

# 使用方式
* 1、在项目源码树root下checkout thirdparty,例如根目录为foo:
```
  mkdir foo
  cd foo
  git init
  git clone https://github.com/cangyingzhijia/thirdparty
```

* 2、如果blade环境还没有构建好，可以从git clone:
```
  git clone https://github.com/cangyingzhijia/builder
  cp builder/blade/BLADE_ROOT.example BLADE_ROOT
  cp builder/blade/CPPLINT.cfg.example CPPLINT.cfg
  builder/blade/install
```
* 3、随后整个工作空间即建立起来，可以进行工作了:
```
  git clone https://github.com/cangyingzhijia/helloworld
  blade run helloword:
```
