from setuptools import find_packages, setup

package_name = 'py_topic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    # console_scriptsに登録すると、ros2 runから実行できるコマンドを作成できます。
    entry_points={
        'console_scripts': [
            # 「ros2 run py_topic talker」でpy_talker.pyのmain関数を実行します。
            'talker=py_topic.py_talker:main',
            # 「ros2 run py_topic listener」でpy_listener.pyのmain関数を実行します。
            'listener=py_topic.py_listener:main'
        ],
    },
)
