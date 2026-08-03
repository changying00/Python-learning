"""
虚拟环境:  是 python 用来管理 第三方库的 一种 技术手段

    每一个项目 都应该提供 一个 虚拟环境、用来 存储 该项目 依赖的 第三方库

    优点:  可以 和 官方 自带的 库 进行分离、且不污染 官方库 、也可以 避免版本冲突 !


VSCode 配置 虚拟环境的 步骤

CTRL + SHIFT + P  --->  Python Select Interpreter


.venv  (该目录 不允许 手动更改)

    Scripts:

        - pip.exe :  管理 第三方依赖库的 核心命令
        - python.exe : 执行 python 的命令
        - activate.bat :  激活虚拟环境的命令
        - deactivate.bat : 退出虚拟环境的命令

    Lib/site-packages:
        - 存放 当前项目 依赖的 第三方库

    pyvenv.cfg :  虚拟环境的配置信息


安装 第三方依赖库

    # 安装 第三方依赖库
    pip install ollama==0.6.2   (如果不带版本号、默认安装最新版)
        (安装 会 同时安装 依赖的库)

    pip install <库> -i https://pypi.tuna.tsinghua.edu.cn/simple  (临时使用 指定镜像源下载依赖包)

    pip install -r requirements.txt :  将 requirements.txt 中 管理的依赖库 进行 批量下载 (方便后期项目迁移)

    # 卸载 第三方依赖库
    pip uninstall ollama
         (卸载 不会下载 依赖库)

    # 查看 已安装的 依赖库
    pip list

    # 将 当前虚拟环境下 安装的 第三方库 交给 requirements.txt 文件管理
    pip freeze > requirements.txt   (每次安装新的库后，执行一次)

"""