"""QIIME 2 plugin for gatk."""

from q2_types.feature_table import FeatureTable, Frequency
from qiime2.plugin import Bool, Float, Plugin

import q2_fail

from . import __version__

plugin = Plugin(
    name="fail",
    version=__version__,
    description="QIIME 2 plugin for testing plugin failures",
    package="q2_fail",
    user_support_text=("I'm sorry you're having problems"),
    website="",
)

plugin.methods.register_function(
    function=q2_fail.task_fail,
    inputs={"table": FeatureTable[Frequency]},
    parameters={"fail": Bool},
    outputs=[("new_table", FeatureTable[Frequency])],
    input_descriptions={"table": "The feature table"},
    parameter_descriptions={},
    output_descriptions={"new_table": "The resulting feature table."},
    name="Fail Task",
    description=("Task made to fail"),
)

plugin.methods.register_function(
    function=q2_fail.memory_fail,
    inputs={"table": FeatureTable[Frequency]},
    parameters={"delay": Float},
    outputs=[("output_table", FeatureTable[Frequency])],
    input_descriptions={"table": "The feature table"},
    parameter_descriptions={},
    output_descriptions={"output_table": "The resulting feature table."},
    name="Memory Failure",
    description=("Memory Failure"),
)
