from .tool_registry import tool_registry

from .database_tool import DatabaseTool
from .metadata_tool import MetadataTool
from .weather_tool import WeatherTool
from .chart_tool import ChartTool
from .pipeline_tool import PipelineTool


tool_registry.register(DatabaseTool)
tool_registry.register(MetadataTool)
tool_registry.register(WeatherTool)
tool_registry.register(ChartTool)
tool_registry.register(PipelineTool)