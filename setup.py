from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='espnet-streaming-decoder',
    version='0.1',
    author='Shinji Watanabe, Benjamin Milde',
    author_email='bmilde@users.noreply.github.com',
    description='Espnet streaming ASR decoder with smaller footprint and fewer requirements, extracted from "ESPnet: end-to-end speech processing toolkit"',
    url='https://github.com/speechcatcher-asr/espnet_streaming_decoder',
    packages=find_packages(),
    package_data={"espnet_streaming_decoder.espnet": ["version.txt"]},
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'espnet_streaming_decoder=espnet_streaming_decoder.asr_inference_streaming:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
