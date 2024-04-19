import logging
from pathlib import Path
from typing import List, Union

from packaging.requirements import Requirement

logger = logging.getLogger(__name__)

try:
    from pip._internal.network.session import PipSession
    from pip._internal.req import parse_requirements
    from pip._internal.req.req_file import ParsedRequirement
    from pip._internal.utils.packaging import get_requirement
except ImportError as e:
    logger.error(f"pip version is outdated, please upgrade, {e}")

from urllib.parse import urlparse

__all__ = ["get_requirements_from_file"]


def get_reqed(req: ParsedRequirement) -> Requirement:
    req_ = req.requirement

    if req.is_editable:  # parse out egg=... fragment from VCS URL
        parsed = urlparse(req_)
        egg_name = parsed.fragment.partition("egg=")[-1]
        if not egg_name:
            egg_name = parsed.path.split("/")[-1]
        without_fragment = parsed._replace(fragment="").geturl()
        req_parsed = f"{egg_name} @ {without_fragment}"
    else:
        req_parsed = req_

    logger.info(f"{req_parsed=}")

    try:
        return get_requirement(req_parsed)
    except:
        return None


def get_requirements_from_file(
    file_path: Union[str, Path], session: Union[str, PipSession] = "test"
) -> List[Requirement]:
    """Turn requirements.txt into a list"""
    if isinstance(file_path, Path):
        file_path = str(file_path)

    parsed_reqs = [
        get_reqed(ir) for ir in parse_requirements(file_path, session=session)
    ]

    logger.info(f"{parsed_reqs=}")

    return [p for p in parsed_reqs if p]


if __name__ == "__main__":
    print(
        get_requirements_from_file(
            Path(__file__).parent.parent.parent / "requirements.txt"
        )
    )
