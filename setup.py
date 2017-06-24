from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()
		
setup(name='setbadge',
			version='0.0.1',
			description='Set the Pythonista app\'s badge value to a custom text string!',
			long_description=readme(),
			classifiers=[
				'Development Status :: 3 - Alpha',
				'License :: OSI Approved :: MIT License',
				'Programming Language :: Python :: 3.5',
				'Topic :: Text Processing :: Linguistic'
			],
			keywords='pythonista objc ios badge notification',
			url='https://github.com/GhostHackzDev/setbadge',
			author='Ghost Hackz',
			author_email='ghosthackz@pginteractive.ml',
			license='MIT',
			packages=['setbadge'],
			include_package_data=True,
			zip_safe=False)
