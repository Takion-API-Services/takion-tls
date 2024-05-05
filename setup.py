from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='takion-tls',
    version='0.1.0',
    author='GlizzyKingDreko',
    author_email='glizzykingdreko@protonmail.com',
    description='A Python TLS client for auto-updating, customizable secure connections, ideal for advanced web scraping and reverse engineering. By TakionAPI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Takion-API-Services/takion-tls',
    packages=find_packages(),
    install_requires=read_requirements(),  # Use the function to read requirements
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    keywords='tls client, web scraping, reverse engineering, takion api',
    project_urls={
        'Documentation': 'https://github.com/Takion-API-Services/takion-tls',
        'Source': 'https://github.com/Takion-API-Services/takion-tls',
        'Tracker': 'https://github.com/Takion-API-Services/takion-tls/issues',
    },
)
