class Distance:
    _TO_METERS = {
        "mm": 0.001,
        "millimeters": 0.001,
        "cm": 0.01,
        "centimeters": 0.01,
        "m": 1.0,
        "meters": 1.0,
        "km": 1000.0,
        "kilometers": 1000.0,
    }

    def __init__(self, value: float, unit: str = "meters"):
        unit_normalized = unit.strip().lower()
        if unit_normalized not in self._TO_METERS:
            raise ValueError(f"Неподдерживаемая единица измерения: '{unit}'")
        self.value = value
        self.unit = unit_normalized

    def _to_meters(self) -> float:
        """Конвертирует текущую дистанцию в метры."""
        return self.value * self._TO_METERS[self.unit]

    def _from_meters(self, meters: float, target_unit: str) -> float:
        """Конвертирует значение из метров в целевую единицу измерения."""
        return meters / self._TO_METERS[target_unit]

    def __str__(self) -> str:
        return f"{self.value:g} {self.unit}"

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_meters = self._to_meters() + other._to_meters()
        new_value = self._from_meters(total_meters, self.unit)
        return Distance(round(new_value, 6), self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        diff_meters = self._to_meters() - other._to_meters()
        new_value = self._from_meters(diff_meters, self.unit)
        return Distance(round(new_value, 6), self.unit)


if __name__ == "__main__":
    d1 = Distance(10, "meters")
    d2 = Distance(2, "kilometers")
    d3 = Distance(500, "centimeters")
    d4 = Distance(1500, "m")

    print("Экземпляры:")
    print("d1 =", d1)
    print("d2 =", d2)
    print("d3 =", d3)
    print("d4 =", d4)
    print("-" * 35)

    print("Сложение:")
    print(f"{d1} + {d2} = {d1 + d2}")   # 10 meters + 2 kilometers = 2010 meters
    print(f"{d2} + {d1} = {d2 + d1}")   # 2 kilometers + 10 meters = 2.01 kilometers
    print(f"{d1} + {d3} = {d1 + d3}")   # 10 meters + 500 centimeters = 15 meters
    print("-" * 35)

    print("Вычитание:")
    print(f"{d2} - {d1} = {d2 - d1}")   # 2 kilometers - 10 meters = 1.99 kilometers
    print(f"{d4} - {d3} = {d4 - d3}")   # 1500 m - 500 centimeters = 1495 m