{
	'includes':[
		'lib/context/def.gypi',
		'lib/numbro/def.gypi',
		'lib/static/def.gypi',
		'lib/traverse/traverse.gypi',
		'plank/def/plank.gypi',
	],#includes
	'target_defaults': {
		'target_name': 'test', 
		'type': 'executable',
		'sources': [
			'src/main.cpp',
		], #sources
		'include_dirs': [
			'plank/src/',
			'.'
		], #include_dirs		
	}, #target_defaults
}