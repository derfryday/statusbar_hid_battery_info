from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Device:
    is_bluetooth: bool
    vendor_id: int
    product_id: int
    product_name: str
    has_battery: bool = False
    device_address: str | None = None

    def __repr__(self) -> str:
        return f"{self.product_name}.{self.device_address}"
