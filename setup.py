from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.chimpdrill',
      version=version,
      description="Mailchimp & Mandrill Integration",
      long_description=open("README.md").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Jason Lantz',
      author_email='jasontlantz@gmail.com',
      url='http://github.com/collective/collective.chimpdrill',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
          'plone.namedfile [blobs]',
          'mailsnake',
          # -*- Extra requirements: -*-
      ],
      extras_require = {
        'test': [
          'plone.app.testing',
        ]
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,

      )
