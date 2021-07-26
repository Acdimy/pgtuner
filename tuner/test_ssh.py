import logging

from tuner.character import OpenGaussMetric
from tuner.exceptions import DBStatusError, SecurityError, ExecutionError, OptionError
from tuner.executor import ExecutorFactory
from tuner.knob import RecommendedKnobs, Knob
from tuner.utils import clip
from tuner.utils import construct_dividing_line
from tuner.utils import to_tuples

ssh = ExecutorFactory() \
            .set_host('127.0.0.1') \
            .set_user('postgres') \
            .set_pwd('Itsinghua,2021') \
            .set_port(5432) \
            .get_executor()

stdout, stderr = ssh.exec_command_sync('which psql', timeout=60)
print(stdout, stderr)