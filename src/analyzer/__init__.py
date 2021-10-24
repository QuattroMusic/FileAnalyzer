import importlib
from pathlib import Path
from typing import Tuple, Dict, cast, List, Union, Optional


class AnalyzerNotFoundError(Exception):
	pass


class Analyzer:
	def should_analyze( self, file: str ) -> bool:
		pass

	def analyze( self, file: str ) -> None:
		pass

	def get_data(self) -> Union[ Tuple[dict, dict], dict ]:
		pass


_contentAnalyzers: Dict[ str, List[Analyzer] ] = {}


def init_analyzers() -> None:
	for package in [ path for path in Path(__file__).parent.glob('*') if path.is_dir() ]:
		_contentAnalyzers[ package.name ] = []
		for analyzer in package.glob('*.py'):
			# ignore __init__.py and private modules
			if analyzer.name.startswith('_'):
				continue

			mod: Analyzer = cast(
				Analyzer,
				importlib.import_module(
					str(
						analyzer.relative_to(
							Path('.').resolve()
						)
					).replace('\\', '.')[:-3]
				)
			)

			_contentAnalyzers[package.name] += [mod]


def get_compatible_analyzer( ext: str ) -> Optional[Analyzer]:
	for analyzers in _contentAnalyzers.values():
		for analyzer in analyzers:
			if analyzer.should_analyze( ext ):
				return analyzer

	return None  # raise AnalyzerNotFoundError(f'An analyzer for "{ext}" cannot be found!' )


def get_analyzers_for_package(name: str) -> List[Analyzer]:
	return _contentAnalyzers[name]
