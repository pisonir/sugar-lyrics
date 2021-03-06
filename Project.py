from dataclasses import dataclass
from pathlib import Path

@dataclass
class Project:
    """
    This class represents our project. It stores useful information about
    the structure, e.g. paths.
    """
    base_dir: Path = Path(__file__).parents[0]
    data_dir = base_dir / 'data'
    dataset_dir = data_dir / 'dataset'
    result_dir = base_dir / 'results'
    log_dir = base_dir / 'log'

    def __post_init__(self):
        # create the directories if they don't exist
        self.data_dir.mkdir(exist_ok=True)
        self.dataset_dir.mkdir(exist_ok=True)
        self.result_dir.mkdir(exist_ok=True)
        self.log_dir.mkdir(exist_ok=True)

