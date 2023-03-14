import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        masks_to_buy = 1
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("OutdatedVaccine")
        if visitor.get("wearing_a_mask") is False:
            raise NotWearingMaskError(
                f"Friends should buy {masks_to_buy} masks"
            )

        return f"Welcome to {self.name}"
