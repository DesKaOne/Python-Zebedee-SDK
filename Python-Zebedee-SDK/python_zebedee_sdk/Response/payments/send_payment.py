from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Data(BaseModel):
    id: str
    fee: str
    unit: str
    amount: str
    invoice: str
    preimage: str
    internal_id: str = Field(..., alias='internalId')
    status: str
    processed_at: str = Field(..., alias='processedAt')
    confirmed_at: str = Field(..., alias='confirmedAt')
    description: str


class PaymentResponse(BaseModel):
    success: Optional[bool] = None
    message: Optional[str] = None
    data: Optional[Data] = None
