from datetime import datetime
from enum import Enum
from typing import Dict, Any

from pydantic import BaseModel, Field


class EnergyData(BaseModel):
    id: int = Field(..., description="The unique identifier for the data entry")
    period: datetime = Field(..., description="The period of the data entry")
    respondent: str = Field(..., description="The respondent for the data entry")
    respondent_name: str = Field(..., description="The name of the respondent")
    type: str = Field(..., description="The type of data entry")
    type_name: str = Field(..., description="The name of the type of data entry")
    value: float = Field(..., description="The value of the data entry")
    value_units: str = Field(
        ..., description="The units of the value of the data entry"
    )


class EnergyType(Enum):
    D = "Demand"
    NG = "Generation"


class StreamChartDataRequest(BaseModel):
    respondent: str
    category: EnergyType
    start_date: str
    end_date: str


class EnergyDataRequest(BaseModel):
    params: Dict[str, Any]
