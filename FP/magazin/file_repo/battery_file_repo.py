from domain.entities import Battery


class BatteryFileRepo:
    def __init__(self, produs_file_path, battery_file_path):
        # super().__init__(produs_file_path)
        self.__battery_file_path = battery_file_path
        self.__batteries = {}

    def show(self):
        self.__read_all_from_file()
        return list(self.__batteries.values())

    def __read_all_from_file(self):
        super().__read_all_from_file()
        #
        with open(self.__battery_file_path, "r") as f:
            for line in f.readlines():
                line = line.strip()
                if line == "":
                    continue
                parts = line.strip(",")
                id = int(parts[0])
                rechargeable = bool(parts[1])

                battery = Battery(id, "", 0.0, rechargeable)
                self.__batteries[id] = battery

    def save_battery(self, battery):
        # Adaugă salvarea bateriilor în fișierul specific lor
        with open(self.__battery_file_path, 'a') as f:
            f.write(f"{battery.get_id()},{battery.rechargeable}\n")

        # Salvează în dicționarul specific bateriilor
        self.__batteries[battery.get_id()] = battery

        # Utilizează funcționalitatea din ProdusFileRepo pentru a salva informațiile generale
        super().save(battery)