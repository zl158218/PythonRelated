### Pyenv  安装
		
	sudo apt-get build-dep   #安装依赖包
	git clone https://github.com/pyenv/pyenv.git ~/.pyenv	
	echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
	启动shell时自动加载pyenv脚本  
	echo 'eval "$(pyenv init -)"' >> ~/.bashrc  
	exec $SHELL    #重启 shell 使脚本生效
	
