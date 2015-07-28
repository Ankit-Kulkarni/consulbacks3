from setuptools import setup

setup(name='consulbacks3',
      version='0.0.1.0',
      description='Backup the consul key value pair directory wise in  yml files and uploads to an s3 bucket ',
      packages=['consulbacks3'],
      install_requires = ['tinys3'],
      url='http://github.com/Ankit-Kulkarni/consulbacks3',
      scripts = ["consulbacks3/consulbacks3", "consulbacks3/consulbacks3-configure"],
      author='Ankit Kulkarni',
      author_email='ankit.kul1890@gmail.com',
      license='ISC',
      keywords = ["consul", "backup", "yml", "key-value", "boto", "s3", "s3bucket", "bucket", "cli", "command"],
      classifiers = [
        "Intended Audience :: DevOps",
        "Natural Language :: English",
        "Environment :: Console",
        "Topic :: Utilities"
        ],
      zip_safe=False)
