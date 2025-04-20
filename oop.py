# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.__brand = brand  # Encapsulated (private) attribute
        self.__model = model
        self.__storage = storage
        self.__battery_life = battery_life

    # Getter methods
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_storage(self):
        return self.__storage

    def get_battery_life(self):
        return self.__battery_life

    # Setter methods
    def set_storage(self, storage):
        if storage > 0:
            self.__storage = storage
        else:
            print("Storage must be positive!")

    def set_battery_life(self, battery_life):
        if battery_life > 0:
            self.__battery_life = battery_life
        else:
            print("Battery life must be positive!")

    def show_specs(self):
        return f"Brand: {self.__brand}, Model: {self.__model}, Storage: {self.__storage}GB, Battery Life: {self.__battery_life} hours"

# Subclass for Gaming Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system, graphics_performance):
        super().__init__(brand, model, storage, battery_life)
        self.__cooling_system = cooling_system
        self.__graphics_performance = graphics_performance

    def show_specs(self):  # Polymorphism - overriding the method
        basic_specs = super().show_specs()
        return f"{basic_specs}, Cooling System: {self.__cooling_system}, Graphics Performance: {self.__graphics_performance}"

# Subclass for Camera Smartphone
class CameraSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, camera_quality, optical_zoom):
        super().__init__(brand, model, storage, battery_life)
        self.__camera_quality = camera_quality
        self.__optical_zoom = optical_zoom

    def show_specs(self):  # Polymorphism - overriding the method
        basic_specs = super().show_specs()
        return f"{basic_specs}, Camera Quality: {self.__camera_quality} MP, Optical Zoom: {self.__optical_zoom}x"

# Example usage
gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 256, 18, "Liquid Cooling", "Ultra High")
print(gaming_phone.show_specs())

camera_phone = CameraSmartphone("Samsung", "Galaxy S21 Ultra", 128, 20, 108, 10)
print(camera_phone.show_specs())

