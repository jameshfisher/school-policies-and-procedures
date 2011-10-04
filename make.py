#!/usr/bin/env python

import subprocess
import os
import os.path
import sys

srcdir = 'src'
dstdir = {
	'html': 'html',
	'latex': 'latex'
	}

suffix = {
	'html': '.html',
	'latex': '.tex'
	}

cmd = {
	'html': [
		'rst2html',
		'--no-generator',
		"--no-datestamp",
		"--no-source-link",
		"--strip-comments",
		"--link-stylesheet",
		"--footnote-references=superscript",
		"--table-style=defaulttable",
		'--stylesheet-path=css/html4css1.css,css/main.css',
		],
	'latex': [
		'rst2latex.py',
		]
	}

target = "html"

files = sys.argv[1:] if len(sys.argv)>1 else filter(lambda x: x[-4:] == '.rst', os.listdir(srcdir))

for f in files:
	p = os.path.join(srcdir, f)
	target_file = os.path.join(dstdir[target], f[:-4] + suffix[target])
	print target_file
	proc = subprocess.Popen(
		cmd[target] + [p],
		stdout=subprocess.PIPE)
	open(target_file, 'w').write(proc.communicate()[0])

