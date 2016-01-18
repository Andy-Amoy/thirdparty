Name: zookeeper
Version: 1.0.1
Release: 1
Summary: zookeeper server
License:
Group:
Packager: cangkui@yoyi.com.cn
BuildArch: x86_64
AutoReq: no

%description
zookeeper server

%prep

%build

%install
rm -fr $RPM_BUILD_ROOT
work_dir=$RPM_BUILD_ROOT/usr/local/zookeeper
mkdir -p $work_dir
mkdir -p $work_dir/bin
mkdir -p $work_dir/conf
mkdir -p $work_dir/lib
mkdir -p $work_dir/logs
mkdir -p $work_dir/data

source_root_dir=$OLDPWD/..
cp -r $source_root_dir/bin/*.sh $work_dir/bin
cp -r $source_root_dir/conf/* $work_dir/conf
cp -r $source_root_dir/lib/* $work_dir/lib
cp -r $source_root_dir/*.jar $work_dir/lib

%post

%files
%defattr(-,anybody,anybody)
/usr/local/zookeeper
%config(noreplace) /usr/local/zookeeper/conf/zoo.cfg

%debug_package %{nil}
%changelog
* Wed Jul 1k 2014 cangkui <cangyingzhijia@126.com>
- create this spec file
